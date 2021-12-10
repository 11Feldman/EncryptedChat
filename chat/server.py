import socket
import os
from dh import parameters
import pickle
import random

# A
class Server:
    """docstring for Server"""
    def __init__(self, host, port, user, param_p , param_g, clave_publica,clave_privada):
        self.userServer = user
        self.p = param_p
        self.g = param_g
        self.clave_publica = clave_publica
        self.clave_privada = clave_privada
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clave_publica_B = None
        self.sock.bind((str(host),int(port)))
        self.sock.listen(10)
        print("""
        *****************
        * SERVER ACTIVO *
        *****************
        """)        
        conn,addr = self.sock.accept()
        self.sock.setblocking(False)

        self.EnviarClavePublica(conn)
        
        while True:
            self.MensajeRecibido(conn)
            self.EnviarMensaje(conn)
        
    def claveFinal(self):
        clave = pow(self.clave_publica_B,self.clave_privada)
        clave = clave % self.p
        return clave

    def EnviarClavePublica(self,conn):
        buffer = (1,self.g,self.p,self.clave_publica)
        conn.send(pickle.dumps(buffer))

    def EncriptarMensaje(self,msg):
        clave = self.claveFinal()
        mensaje_encriptado = ''
        for c in msg:
            mensaje_encriptado += chr( ord(c) + clave)
        return mensaje_encriptado
        
    def DesencriptarMensaje(self,msgEncr):
        clave = self.claveFinal()
        mensaje = msgEncr
        mensaje_desencriptado = ''
        for c in mensaje:
            mensaje_desencriptado += chr( ord(c) - clave)
        return mensaje_desencriptado
    
    def EnviarMensaje(self,conn):
        enviar = input("[Server: {}]-> ".format(self.userServer))
        mensaje_encriptado = self.EncriptarMensaje(enviar)
        buffer = (self.userServer,mensaje_encriptado,self.clave_publica)
        conn.send(pickle.dumps(buffer))
    
    def MensajeRecibido(self,conn):
        mensajerecibido= pickle.loads(conn.recv(2048))
        print("\nMensaje del cliente: (usuario, mensaje encriptado, clave publica)",  mensajerecibido,'\n')
        self.clave_publica_B = mensajerecibido[2]
        mensaje_desencriptado = self.DesencriptarMensaje(mensajerecibido[1])
        if mensaje_desencriptado =='Salir' or mensaje_desencriptado == 'salir':
            print('Cerrando chat...')
            print('Adios')
            conn.close()
            exit()
        else:
            print("[Cliente: {}]-> {}".format(mensajerecibido[0],mensaje_desencriptado))

    
# Instanciamos el servidor y los datos para diffie hellman.
clave_privada = random.randint(a=2,b=1000)
g,p,clave_publica = parameters(privada=clave_privada).clavePublica()


if __name__ == '__main__':
    s = Server(
        host='localhost',
        port=8000,
        user= os.getenv('USERDOMAIN'),
        param_g=g,
        param_p=p,
        clave_publica=clave_publica,
        clave_privada=clave_privada
    )