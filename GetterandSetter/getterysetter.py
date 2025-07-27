##Privado esta malvisto acceder directamente
class Pagina:
    def __init__(self, numero):
        self._numero = numero

###Getter ahora con property puedo llamar con . y nombre en este caso llame getter
    @property
    def numero (self):
        return self._numero
 ###Setter con el mismo nombre 
    @numero.setter 
    def numero (self, nuevo_numero):
        self._numero = nuevo_numero;   
    
    ####Me permite eliminar propiedades privadas
    @numero.deleter
    def numero (self):
        del self.numero    

##Nos devuelve con property el numero nuevo sin tener que usar parentisis
Pagina1 = Pagina (9);
print (Pagina1.numero)

Pagina1.numero = 19
print (Pagina1.numero)


        
#Muy privado 
# class hoja: 
#     def __init__(self, apellido):
#         self.__nombre = "jose"
#         self.__apellido = apellido
# ########################  Pueden existir metodo _privados y muy __Privados
# #Privado 
# def _imprimir ():
#     print("Hola mundo");
# #Muy privado
# def __ocultar ():
#     print("Ocultando");



