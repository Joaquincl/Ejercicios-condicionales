## Programa que lee un número y determina si es par o impar.
numero = int(input("Introduce un número: "))

# Determinar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
