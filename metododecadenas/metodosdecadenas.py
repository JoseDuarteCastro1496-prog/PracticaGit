 # Dir devuelve los atributos validos del objeto se necesita print para mostrarlos
 
cadena =  "hola mundo";
print(dir(cadena));

#UPPER Convierte en mayuscula
Resultado = cadena.upper ();
print(Resultado);
#Lower  hace minusculas los textos
Resultado1 = cadena.lower ();
print(Resultado1);
 #Capitalize primera en mayuscula
Resultado2 = cadena.capitalize ();
print (Resultado2);


#####################Busqueda en cadenas #########################3
#find me devuelve el indice donde se encuentra el inicio de la palabra
#Este metodo devuelve -1 sino encuentra coincidencias
Cadena1 = "Hola mundo de saturno"
Resultado3 = Cadena1.find ("mundo");

if Resultado3 <= 3:
    print("no esta")
else:
    print("El texto esta despues de Hola")
    
#Metodo index si no encuentra coincidencia se cae el programa devuelve excepcion
# hace lo mismo que find 
Resultado4 = Cadena1.index ("mundo")
print( Resultado4);



###Metodos de numeros  isnumeric
# Devuelve true si es numero o false sino.
cantidad = 78;
Resultado5 = cantidad.is_integer()
print(Resultado5)


###Contar coincidencias 
cadena6 = "hola hola mundo hola"
Resultado7 = cadena6.count("hola")
print(Resultado7);



###################Funcion len cuenta cuantos caracteres hay en una cadena
cadena7 = "Hola mundo"
Resultado8 = len (cadena7)
print(Resultado8)
    
###########startwid y endwidth
cadena8 ="hola"
resultado9 = cadena8.startswith("ho");
resultado10 = cadena8.endswith("do");

######################## REMPLACE cambia un valor por otro en la cadena
cadena11 = "Hola mundo de papel"
resultado11 = cadena11.replace("Hola", "Adios");
print(resultado11);


####################SPLIT ME SEPARA UNA CADENA EN UN ARREGLO SEGUN LO QUE LE PASE .,-

cadena16 = "Hola, mundo, trece,doce";
resultado12 = cadena16.split(",")
###Me devuelve arreglo se parado
print(resultado12)


