## Programa que lea un cadadena por teclado y compruebe si es una letra mayúscula.
# Leer una cadena por teclado
cadena = input("Introduce una cadena: ")

# Comprobar si es una letra mayúscula
if len(cadena) == 1 and cadena.isalpha() and cadena.isupper():
    print("La cadena es una letra mayúscula.")
else:
    print("La cadena no es una letra mayúscula.")