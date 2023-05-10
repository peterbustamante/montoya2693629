import random
def llenarLista(lista,tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

L1=[]
L1=llenarLista(L1,5,100)
print(llenarLista(L1,5,100))