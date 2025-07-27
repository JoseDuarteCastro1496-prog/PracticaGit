 
 #publico definicion normal
class Libro :
    def __init__(self, nombre):
        self.nombre = nombre

##Privado esta malvisto acceder directamente
class Pagina:
    def __init__(self, numero):
        self._numero = numero
        
#Muy privado 
class hoja: 
    def __init__(self, apellido):
        self.__nombre = "jose"
        self.__apellido = apellido
########################  Pueden existir metodo _privados y muy __Privados

#Privado 
def _imprimir ():
    print("Hola mundo");
#Muy privado
def __ocultar ():
    print("Ocultando");

