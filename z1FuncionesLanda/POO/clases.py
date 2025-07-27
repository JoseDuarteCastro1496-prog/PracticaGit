
# # se crea la clase
# class Celular: 
#     marca="samsung"
#     color="rojo"
#     tamaño="Grande"
# Celular1 = Celular ();
# print(Celular1.color) 

######################Herencia##################################
###Creacion de clases y objectos con parametros y argumentos
class Carro:
    def __init__(self, Marca, Color,Tamaño):
        self.Marca = Marca
        self.Color = Color
        self.Tamaño = Tamaño
        
    def Mostrar_Marca (self) :
       return  self.Marca
        
class Deportivo (Carro) :
    def __init__(self,Marca,Color,Tamaño, velocidad, frenos):
        super().__init__(Marca,Color,Tamaño)
        self.velocidad =velocidad
        self.frenos=frenos
        
    def driff ():
       return print("Haciendo driff")
  
Deportivo1 = Deportivo("Honda","Rojo","Mediano",120,"no tiene");

print(Deportivo1);
print (Deportivo1.Mostrar_Marca())
