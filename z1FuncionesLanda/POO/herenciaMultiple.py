class Persona :
    def __init__(self, nombre,apellido,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
    def toString (self) :
        print(f"Nombre: {self.nombre} /n Nombre: {self.apellido} /n Telefono: {self.telefono}")
        
class Artista :
    def __init__(self):
        self.habilidad = "Bailar"
        
class EmpleadoArtista (Persona, Artista):
    def __init__(self, nombre, apellido, telefono,Salario):
        Persona.__init__(nombre, apellido, telefono)
        Artista.__init__()
        self.Salario = Salario