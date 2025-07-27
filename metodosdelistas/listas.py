lista = ["jose", 20,13,3];
#numero de elmentos en la lista
print(len(lista));
###############################AGREGACION METODOS###################
#agregar elementos al final de la lista, hay ir a la lista a ver los cambios
lista.append("hola")
print(lista);

#para agregar al inicio debo usar insert [indice, elmento]
lista.insert(0,"nuevo elemento")
print(lista)

#extend permite arregra otra lista o iterable a la lista actual
lista1 = [1,2,3]
lista2 = [4,5,6]

resultado = lista1.extend(lista2)
print(lista1)


######################Eliminacion en la lista#################################
#Clear () limpia la lista
#remove (2) elimina el primer elemento con coincidencia

#pop elimina con indice 
lista7 = [1,2,3,4,5]
lista7.pop(0)

####Metodos para reordenar y copiar 
#Invierte los elementos en la lista
print("lista invertida")
lista.reverse ();
print(lista);

######Copiar lista #################
copia = lista.copy();

#############################################################
#######Ejercicio 1 ##########
frutas  = ["manzana","banana","cereza"];
frutas.insert(2,"uva");
#Obtener indice de banana
indice = frutas.index("banana");

#Eliminar ese elementos
fruta_removida = frutas.pop (indice);
#imprimir fruta removida
print(fruta_removida)
print(frutas);
#######Ejercicio 2 ##########
pares = [2,4,6]
impares = [1,3,5]
pares.extend(impares)

#agregar numeros impares al final 
print(pares)
numeros_ordenados = pares.copy ();
numeros_ordenados.sort ()
print(numeros_ordenados)

###############Ejercicio 3
numeros_repetidos = [10,20,30,40,50,20]
conteo_veinte = numeros_repetidos.count(20)
print(conteo_veinte);

#Devolver la primera coincidencia del numero 30
numero_treinta = numeros_repetidos.index (30)
print(numero_treinta);

######ejercicio 4#########
palabras = ["Python", "es", "divertido", "programar", "con"]
palabras.sort()

















