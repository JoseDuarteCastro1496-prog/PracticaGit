from abc import ABC, abstractmethod 

class Persona (ABC):
     def __init__(self, nombre, edad ):
          self.nombre = nombre
          self.edad = edad

     @abstractmethod 
     def actividad_realizada(self):
          pass
      
class Estudiante(Persona):
    def __init__(self, nombre, edad,actividad):
         super().__init__(nombre, edad)
         self.actividad = actividad

    def actividad_realizada(self):
         return self.actividad

estudiante = Estudiante("jose", 28, "Estudiar")
actividades = estudiante.actividad_realizada();
print(actividades);