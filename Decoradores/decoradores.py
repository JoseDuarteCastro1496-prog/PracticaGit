#Funcion original

def saludar ():
    print("hola")
    

def docador (funcion):
    def nueva():
        print("Saludo")
        funcion ()
        print("Adios")
    return funcion ();