#3. Funcion para llenar una lista con la serie de fibonacci

def fib(x):
    a=0
    b=1
    for y in range(x):
        c=a+b
        a = b 
        b =c   
    return b

num=int(input("Ingrese la cantidad de digitos: "))
lista1=[]

for z in range(num):
    lista1.append(fib(z))
    
print("Serie de Fibonacci: ",lista1)

#4. Funcion para llenar una lista de numeros aleatorios pero que no sean repetidos 

def noRepetidos(lista2,tam):
    lista2=[]
    contador=0
    for i in range(tam):
        while contador!=tam:
            num=int(random.randrange(20))
            if num not in lista2:
                lista2.append(num)
                contador=contador+1
            else:
                print(f"El numero {num} ya esta en la lista")
    return lista2

norp=[]
norp=noRepetidos(l1,10)
print("No repetidos",norp)