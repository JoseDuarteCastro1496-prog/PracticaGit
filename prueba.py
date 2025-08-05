#datos vacios 
lista = list();
lista1 = [];


#tuplas
# tupla = tuple();
# tupla1 = ();

# #conjunto
# conjunto  = set(); 
# conjunto1 = {"hola",334}
# print(type(conjunto1))

# # diccionario
# diccionario1 = dict ();
# diccionario  = {}
# print(type(diccionario))

#####################################################
class Persona :
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def toString (self):
        print (f"Nombre : {self.nombre} y la edad es : {self.edad}");
        
class Estudiante (Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def imprime_el_grado(self):
        print(f"El grado es: {self.grado}")

estudiante1 = Estudiante ("jose", 29 , 6);
estudiante1.imprime_el_grado ();
estudiante1.toString (); 

###################################Provando polimorfismo ver que se puede crear un metodo 
#con una llamada de funcion generica como objecto.sonido ();
class perro ():
    def sonido (self):
        print ("Ladra");    
    
class gato ():
    def sonido (self):
        print("Maulla");
        
def sonar (objeto):
    objeto.sonido();
    
perro1 = perro ();
sonar (perro1)

def nueva_funcion ():
    print("En git")
    
def otra_funcion ():
    print ("funcion 2")
    
def funcion_3():
    print ("funcion 3")
    
def funcion_4():
    print ("funcion 4")

def funcion_5():
    print ("funcion 5")
    