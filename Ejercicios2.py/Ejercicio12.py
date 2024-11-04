#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".
# Pedir el resultado del dado
resultado = int(input("Introduce el resultado del dado (1-6): "))

# Diccionario con las caras opuestas del dado
caras_opuestas = {
    1: "seis",
    2: "cinco",
    3: "cuatro",
    4: "tres",
    5: "dos",
    6: "uno"
}

# Verificar si el número es válido
if 1 <= resultado <= 6:
    cara_opuesta = caras_opuestas[resultado]
    print(f"La cara opuesta al número {resultado} es: {cara_opuesta}")
else:
    print("ERROR: número incorrecto.")