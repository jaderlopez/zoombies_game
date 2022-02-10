
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
        self.calle = 1
    
    def situacion(self):
        return "{}, estas en la calle {}".format(self.nombre, self.calle)
    
    def moverse(self, velocidad):
        if velocidad == "1":
            self.calle += 1
        elif velocidad == "2":
            self.calle += 2
        else:
            self.calle +=3













# class persona:
#     def __init__(self, nombre, calle=1):
#         self.nombre = nombre
#         self.calle = calle

#     def moverse(self, velocidad):
#         if velocidad == 1:
#             self.calle += 1
#         elif velocidad == 2:
#             self.calle += 2
#         else: 
#             self.calle +=3

# jose = persona("jose_martinez")
# juan = persona("juan_peralta", 3)

# print(jose.nombre)
# jose.moverse(3)
# print(jose.calle)


# print(juan.nombre)
# juan.moverse(2)
# print(juan.calle)

###////////////////////////////////////

# class pasaporte(object):
#     def __init__(self, nombre, categoria_edad, anos, pais_origin, pais_actual):
#         self.nombre = nombre
#         self.anos = anos 
#         self.pais_origin = pais_origin
#         self.pais_actual = pais_actual
#         self.categoria_edad = categoria_edad

# def mayor_edad(self, edad):
#     edad = 18
#     if self.anos >= edad:
#         self.categoria_edad == "es mayor de edad"
#     elif self.anos < edad:
#         self.categoria_edad == "es menor  de edad"

# def nacionailidad(self):
#     if self.pais_origin == "colombia":
#         print("es colombiano")

# jader = pasaporte.nombre("jader")

# //////////////////////////

# class pasaporte():
#     def __init__(self, nombre_dueno, edad):
#         self.nombre_dueno = nombre_dueno
#         self.edad = edad

# pasport_1 = pasaporte.nombre_dueno("jader")
# print(pasport_1.nombre_dueno)

#///////////////////////////
    
# class Persona():
#     def __init__(self, name, edad):
#         self.name = name
#         self.edad = edad
    
#     def adulto(self):
#         if self.edad > 18:
#             print("es un adulto")
#         else:
#             print("aun no es mayor de edad")

# jader = Persona("jader", 14)

# print(jader.adulto())





