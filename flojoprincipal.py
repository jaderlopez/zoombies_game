from persona import Persona
from zommbies import Zombi2
import os

os.system("cls")

print()
print("""
la ciudad ah sido invadida por ZOOMBIES
estas en la calle 1 debes llegar a la calle 40
solo puedes avanzar 1, 2 0 3 calles
los zombies pueden avanzar 1, 2 o 3 calles buajajaja

si te topas con uno destos te muerden 
""")
print()

nombre = input ("listo? cual es tu nombre: ").capitalize()

jugador = Persona(nombre)

horda = []
for i in range (10):
    z = Zombi2()
    horda.append(z)


while True:

    os.system("cls")

    print(jugador.situacion())

    calles = []
    for Zombi2 in horda:
        calles.append(Zombi2.calle)
    calles.sort()
    print("hay zombies en las calles: ")
    for elemento in calles:
        print(elemento, end=" ")
    print()

    if jugador.calle > 40:
        print()
        print("""Felcidades haz ganado
        tu recompensa es la gratificacion de haber echo estoo """)
        print()
        break

    movimiento = input("cuanto quieres avanzar 1/2/3: ")
    jugador.moverse(movimiento)


    if jugador.calle == Zombi2.calle:
        print("te comieron y no de buena forma: ")
        break

    for z in horda:
        Zombi2.movimiento()


        




    
        





