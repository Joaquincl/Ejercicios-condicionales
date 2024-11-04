## Programa que pida un número y diga si es positivo, negativo o 0.

numero = float(input("Ingresa un número: "))

# Verifica si el número es positivo, negativo o 0.
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("·l número de negativo.")
else:
    print("El número es 0.")