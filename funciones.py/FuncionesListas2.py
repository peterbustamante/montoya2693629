import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista
l1=llenarLista(10,10)
print("La lista es: ",l1)
l2=llenarLista(10,10)
print("La lista es: ",l2)

suma_l1 = (l1)  # calculamos la suma de la primera lista
suma_l2 = (l2)  # calculamos la suma de la segunda lista

def sumaLista(lista):
    sumatoria=0
    for x in lista:
        sumatoria += x
        return sumatoria

suma_l1=sumaLista(8,10)
print(l1)
suma_l2=sumaLista(4,10)
print(l2)

if suma_l1 > suma_l2:
    print(f"La primera lista tiene la suma más alta: {suma_l1}")
elif suma_l1 < suma_l2:
    print(f"La segunda lista tiene la suma más alta: {suma_l2}")
else:
    print("la suma son iguales ")

menor_l1 = (l1)
mayor_l2 = (l2)

if menor_l1 > mayor_l2:
    print("La primera lista tiene el numero mayor")

else:
    print("Las dos tienen los mismos numeros")

menor_l1 = (l1)
menor_l2 = (l2)

if menor_l1 < menor_l2:
    print("La primera lista tiene el numero menor")

else:
    print("Las dos tienen el numero menor")

