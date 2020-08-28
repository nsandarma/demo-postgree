#Desarrollado por Mahonri Mtz.
#Este programa es un tipo de juego en ql que tienes que adivinar un numero entre el 0 al 10
import random
print("Intenta adivinar un numero entre el 0 al 10")
numero= random.randint(0,11)
op=0
while op<10:
    x=int(input("ingresa tu numero"))
    if x>numero:
        print("El numero es mas pequeño")
    if x<numero:
        print("El numero es mas grande")
    elif x==numero:
        print("Le atinaste al numero")
        break
op=op+1



