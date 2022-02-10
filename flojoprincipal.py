from persona import Persona
from zommbies import Zombi
import os

os.system("cls")

print()
print("""
la ciudad ah sido invadida por ZOOMBIES
estas en la calle 1 debes llegar a la calle 40
solo puedes avanzar 1, 2 0 3 calles
los zombies pueden avanzar 1, 2 o 3 calles buajajaja

si te topas con uno de estos te muerden 
mueres y peor aun pierdes
""")
print()

nombre = input ("estas listo? cual es tu nombre: ").capitalize()

jugador = Persona(nombre)


horda = []
for i in range (10):
    z = Zombi()
    horda.append(z)

while True:

    os.system("cls")
    print()
    print(jugador.situacion())
    print()

    calles = []
    for zombi in horda:   
        calles.append(Zombi().calle)
    calles.sort()
    print("hay zombies en las calles: ")
    print()
    print(" ", end="")
    for elemento in calles:
        print(elemento, end=" ")
    print()
    print()

    if jugador.calle > 40:
        print()
        print("""Felcidades haz ganado
        tu recompensa es la gratificacion de haber echo estoo """)
        print()
        break


    comido = False
    for zombi in horda:
        if Zombi().calle == jugador.calle:
            perdiste = True
    
    if comido:
        print(""" 
        un zombi te vio
        te ataco te mordio te moriste y perdiste :(""")
        print()
        break
    
    velocidad = ""
    while velocidad not in("1", "2", "3"):
        velocidad = input("cuanto quieres avanzar 1/2/3: ")
    jugador.moverse(velocidad)

    for z in horda:
        Zombi().moverse()
    if z.eliminar_z():
        horda.remove(z)
        

        




    
        





