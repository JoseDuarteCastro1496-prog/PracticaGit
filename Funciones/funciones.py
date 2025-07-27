def mi_primera_funcion ():
    a = 12
    b = 14
    c = a + b
    print(c)
    
mi_primera_funcion ();


####Primer primera funcion
def clasificador_de_Frutas ():
    valor1 = input ("Ingresa una fruta");
    
    if valor1 == "Manzana": 
        print ("La fruta es una manzana")
    else: 
            print  ("Es cualquier otra: fruta")
    
clasificador_de_Frutas ();
    
##Segunda funcion con parametros
#hay que convertir texto a numeros para sumar
def suma_de_dos_numeros (numero1, numero2):
    a = int (numero1)
    b= int (numero2)
    
    resultado = a + b
    return resultado

numero1 = input ("Ingresa el numero 1: ");
numero2 = input ("Ingresa el numero 2: ");
suma = suma_de_dos_numeros (numero1, numero2);
print(suma)



######Recursividad 
def cuenta_atras(n):
    
    if n == -5 :
        return
    
    if n == 0:
        print ("Despegando!")
    else:
        print (n)
    cuenta_atras(n-1)
    
    
cuenta_atras (3)

