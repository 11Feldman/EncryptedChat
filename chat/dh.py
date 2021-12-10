class parameters(object):
    """ Constructor """
    def __init__(self, privada):
        self.clave_privada = privada
        self.g = 5
        self.p = 23
        self.clave_publica = None
        self.clave_final = None

    """ Generador de clave publica """
    def clavePublica(self):
        clave_publica = pow(base=self.g,exp=self.clave_privada) % self.p
        self.clave_publica = clave_publica
        return self.g,self.p,clave_publica