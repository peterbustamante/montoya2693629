#Lo primero que se debe hacer es importar la biblioteca random para llenar la listas con numeros aleatorios segun el rango
def parImpar(num):
    if num%2==0:
        #print('par')
        return 'par'
    else:
        #print('impar')
        return 'impar'

print(parImpar(36))
parImpar(5)
#Mostramos el resultado determinando el numero que ponga la funcion
parImpar(2)
parImpar(7)

def perfecto(num):
#codigo para saber si un numero es perfecto
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        #print('perfecto')
        return 'perfecto'
    else:
        #print('no esperfecto')
        return 'no es perfecto'

perfecto(6)   
perfecto(10)   
print(perfecto(28))
perfecto(21)   