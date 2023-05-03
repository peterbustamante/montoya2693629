# Inicializar la variable maximo con un valor muy pequeño
maximo = -float("inf")

x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el valor de n: "))

# Inicializar el resultado con 1
resultado = 1

# Calcular la operación x^n s
if n > 0:
    i = 1
    while i <= n:
        resultado *= x
        i += 1
elif n < 0:
    i = 1
    while i <= abs(n):
        resultado /= x
        i += 1
else:
    resultado = 1


print("El resultado de la operación", x, "^", n, "es:", resultado)