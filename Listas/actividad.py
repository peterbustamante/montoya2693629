import random

def llenarlista(tam,rango):
    lista=[random.randrange(rango)for i in range(tam)]
    return lista
def sumalista(lista):
    sum=0
    for x in lista:
        sum+=x
        return sum
def promediolista(lista):
    return sumalista(lista)/len(lista)

def ascendente(lista,tam):
#print(tam)
    for i in range(tam):
        for j in range(i+1,tam):
            if lista[i]>lista[j]:
                aux=lista[i]
                (parameter)lista: Any

print(lista)

for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux            

print(lista)

