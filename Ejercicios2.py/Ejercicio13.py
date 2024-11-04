#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.
# Pedir al usuario el número del día de la semana
dia_numero = int(input("Introduce un número del 1 al 7 para el día de la semana: "))

# Diccionario con los días de la semana
dias_semana = {
    1: "lunes",
    2: "martes",
    3: "miércoles",
    4: "jueves",
    5: "viernes",
    6: "sábado",
    7: "domingo"
}

# Verificar si el número es válido
if 1 <= dia_numero <= 7:
    dia_nombre = dias_semana[dia_numero]
    print(f"El día correspondiente al número {dia_numero} es: {dia_nombre}")
else:
    print("El número introducido no es correcto.")