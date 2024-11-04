# Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir 3 cosas:
# El exponente es positivo, sólo tienes que imprimir la potencia.
# El exponente es 0, el resultado es 1.
# El exponente es negativo, el resultado es 1/potencia con el exponente positivo.
## Pedir la base y el exponente al usuario
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calcular la potencia según el valor del exponente
if exponente > 0:
    resultado = base ** exponente
    print(f"El resultado de {base} elevado a {exponente} es: {resultado}")
elif exponente == 0:
    print("El resultado es: 1")
else:
    resultado = 1 / (base ** abs(exponente))
    print(f"El resultado de {base} elevado a {exponente} es: {resultado}")