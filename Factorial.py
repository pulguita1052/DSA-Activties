def factorial(n):
    if n == 1: 
        return 1
    return n * factorial(n-1)

num = int(input("Porfavor ingrese un número del 1 al 15: "))

while (num > 15 or num < 1):
    num = int(input("El numero q ingreso no es valido, ingrese su numero nuevamente: "))

print("El factorial de " + str(num) + " es " + str(factorial(num)))
