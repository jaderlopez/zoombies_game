# import random

# class Zoombies:

#     def __init__(self):
#         self.calle = random.randint(10,20)
#         self.direccion = random.choice(["izquierda", "derecha"])

#     def moverse(self):
#         if self.direccion == "izquierda":
#             self.calle -= random.randint(1,3)
#         else:
#             self.calle += random.randint(1,3)
    
#     def eliminar_z(self):
#         if self.calle < 0 or self.calle > 40:
#             return True
#         else:
#             return False

import random

class Zombi2:

    def __init__(self):
        self.nombre = "manolo"
        self.calle = random.randint(10, 20)
        self.velocidad = random.randint(1,3)
        self.direccion =    random.choice(["izquierda", "derecha"])
    
    def movimiento(self):
        if self.direccion == "izquierda" :
            self.calle -= self.velocidad
        else:
            self.calle += self.velocidad

    def eliminar_z(self):
        if self.calle < 0 or self.calle > 40:
            return True
        else:
            return False
    
    movimiento = input("cuanto quieres avanzar 1, 2 o 3 : ")


