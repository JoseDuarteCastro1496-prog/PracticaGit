from .Carro import Carro
 
class Deportivo (Carro):
    def __init__(self, marca, color, velocidad):
        super().__init__(marca, color)
        self.velocidad = velocidad
        
    

