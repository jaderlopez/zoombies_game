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
        zombi = Zombi().calle
        calles.append(zombi)
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
    for zombi in calles:
        if zombi == jugador.calle:
            comido = True
            
    
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
        Zombi().movimiento()
    if Zombi().no_visible():
        horda.remove(z)





#/////////////////////////



# horda = []
# for z in range(10):
#     z = Zombi()
#     horda.append(z)

# while True:

#     calles = []
#     for i in horda:
#         i = Zombi().calle
#         calles.append(i)
#     calles.sort()
#     print()
#     print(jugador.situacion())
#     print()
#     print(""" en la calle hay mucho zoombi
#     estan en las calles: """)
#     print()
#     print(calles, end=" ")
#     print()

#     movimiento = input("cuanto quieres moverte? (1/2/3)  ")
#     jugador.moverse(movimiento)

#     if jugador.calle > 40 :
#         print("felicidades haz ganado")
#         break

#     for i in horda:
#         if i == jugador.calle:
#             print("te han comido amigo")
#             break
    

        





    
        





