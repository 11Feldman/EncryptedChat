import socket
import pickle
import random

# B
class Client():
    def __init__(self,host,port,user,clave_privada):
        self.localhost = host
        self.port = port
        self.username = user        
        self.clave_privada = clave_privada
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.localhost,self.port))
        self.clave_publica = None
        self.p=None
        self.g=None
        self.clave_publica_A=None

        mensajerecibido= pickle.loads(self.sock.recv(2048))
        if mensajerecibido[0] == 1:
            self.g = mensajerecibido[1]
            self.p = mensajerecibido[2]
            self.clave_publica_A = mensajerecibido[3]
            self.clave_publica = pow(base=self.g, exp=self.clave_privada)%self.p
            print("""
            ------------------------------------
            >    p: {},                        <
            >    g: {},                        <
            >    Publica A: {},                <
            >    Privada B: {},                <
            >    Publica B: {},                <
            >    Clave para encriptar: {}      < 
            ------------------------------------
            """.format(
                self.p,
                self.g,
                self.clave_publica_A,
                self.clave_privada,
                self.clave_publica,
                pow(
                    base=self.clave_publica_A,
                    exp=self.clave_privada
                )% self.p
                )
            )

        print(
            """
             *************************************************
             * Para salir del chat ingrese "Salir" o "salir" *
             *************************************************
            """
        )
        
        while True:
            
            msg = input('[Yo]->')
            self.EnviarMensaje(msg)
            self.MensajeRecibido()
    
    def ClaveFinal(self):
        clave = pow(self.clave_publica_A,self.clave_privada)
        clave = clave % self.p
        return clave
    
    def DesencriptarMensaje(self,msgEncr):
        clave = self.ClaveFinal()
        mensaje_desencriptado = ''
        for c in msgEncr:
            mensaje_desencriptado += chr( ord(c) - clave)
        return mensaje_desencriptado
        
    def EncriptarMensaje(self,msg):
        clave = self.ClaveFinal()
        mensaje_encriptado = ''
        for c in msg:
            mensaje_encriptado += chr( ord(c) + clave)        
        return mensaje_encriptado
                
    def EnviarMensaje(self,mensaje):
        mensaje_encriptado = self.EncriptarMensaje(mensaje)
        buffer = (self.username,mensaje_encriptado,self.clave_publica)
        self.sock.send(pickle.dumps(buffer))

    def MensajeRecibido(self):
        mensajerecibido= pickle.loads(self.sock.recv(2048))
        print("\nMensaje del Server: (usuario, mensaje encriptado, clave publica)",  mensajerecibido,'\n')
        self.clave_publica_A = mensajerecibido[2]
        mensaje_desencriptado = self.DesencriptarMensaje(mensajerecibido[1])
        if mensaje_desencriptado == 'Salir' or mensaje_desencriptado== 'salir':
            print('Cerrando el chat...')
            print('Adios.')
            exit()
        else:
            print('[Server]->', mensaje_desencriptado)
        
        

# Instanciamos el cliente y los datos para diffie hellman.
num = random.randint(a=1,b=1000)
clave_privada = 15
username = input('Ingrese su usuario:')

# saveClaves(username,clave_privada)

if __name__ == '__main__':
    c = Client(
        host='localhost',
        port=8000,
        user=username,
        clave_privada=clave_privada
    )        
