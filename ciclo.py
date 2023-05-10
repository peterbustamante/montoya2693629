import random

def nummat(x):
    suma=0
    n=1
    while suma<= maximo:
        suma=suma+n
        n=n+suma
        return n-1
    maximo= int (input("introduce un numero  maximo"))
lista=nummat(-1)

print("El numero natural mas pequeño necesario para superar el maximo es:",lista)