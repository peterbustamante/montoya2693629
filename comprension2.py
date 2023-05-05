import random
count=0
posc=[]
tam=random.randint(15,20)
lista=[random.randrange(0,9) for _ in range (tam)]
print(lista)
num =int(input("ingrese numero ingresado en la lista"))

if num in lista:
    print("El numero si esta")
else:
    print("El numero no esta")
if count>1:
    print("El numero se repite",count,"veces")
for i in range (len(lista)):
    if num == lista[i]:
        posc.append (i)
print("el numero esta en la posicion:", posc)

print(lista)
