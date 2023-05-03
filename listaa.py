import random

sum=0
max=0
min=1000
prom=0
lista= []
tam=int(random.randit(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    sum+=num
    prom=sum/tam
    if num>max: 
        max=num
    if num<min and num!=0:
        min=num
print ("la lista de numeros es",lista)
print ("la suma de los numeros es", sum)
print ("El promedio es",prom)
print ("El numero maximo es", max)
print ("El numero minimo es", min)