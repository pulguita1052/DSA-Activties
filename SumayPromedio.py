largoLista = int(input("Cuantos numeros deseas ingresar? "))
miLista = []

for i in range(largoLista):
    num = int(input(f"Ingresa el numero {i+1}: "))
    miLista.append(num)

longitud = len(miLista)
sumito = sum(miLista)
promedio = sumito / longitud

print("La suma de tus numeros es " + str(sumito) + ", y el promedio es " + str(promedio) )
