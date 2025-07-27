#  Listas de datos si se pueden modificar
lista = ["nombre",9,True, 1.43,1.43]
# print(lista); 
# print (lista[0]);

#Tuplas no se pueden modificar
tupla = ("hola", 12);

# CONJUNTOS NO SE PUEDE ALTERAR
#no permite repetir valores no los muestra
#no muestra por indice solo muestra todo  
conjunto = {"jose",23,23.3}
###o tambien convertir  iterables en set o conjuntos
nueva_conjunto = set (lista);



#Diccionario se escribe igual que un JSON
diccionario = {
    "nombre": "jose",
    "edad": 23,
    "altura": 1.70
    }
# asi se acceden a las propiedades de un diccionario
# print(diccionario["nombre"]);
##lo ideal es acceder con get sino encuentra valor no devuelve excepcion como si lo haria metod anterior

diccionario.pop("edad");
# print (diccionario)


#Te eliminar todos los datos
# diccionario.clear ()


nuevo_diccionario = {
    "nombre": "jose",
    "apellido": "Duarte"
}

##con items ()
for clave, valor in nuevo_diccionario.items() :
    print(clave, valor)
    
##Con values () solo valores me tira los dos valores de nombre y apellido
for  valor in nuevo_diccionario.values() :
    print(valor)
