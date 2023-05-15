import random
lista = []

while len(lista) > 15:
    lista.append(random.randint(15,125))
    for i in range(len(lista)):
        lista[i] = round(random.uniform(1.5))
print(lista)

