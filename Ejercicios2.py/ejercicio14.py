# Escribe un programa que pida un número entero entre uno y doce e imprima el 
# número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
# Pedir al usuario el número del mes
# Pedir al usuario el número del mes
mes_numero = int(input("Introduce un número entre 1 y 12 para el mes: "))

# Diccionario con el número de días de cada mes
dias_por_mes = {
    1: "Enero y tiene 31",  
    2: "Febrero y tiene 28",  # (sin considerar años bisiestos)
    3: "Marzo y tiene 31",   
    4: "Abril  y tiene 30",  
    5: "Mayo y tiene 31",  
    6: "Junio y tiene 30",  
    7: "Julio y tiene 31",  
    8: "Agosto y tiene 31",  
    9: "Septiembre y tiene 30",  
    10: "Octubre y tiene 31",
    11: "Noviembre y tiene 30", 
    12: "Diciembre y tiene 31",
}

# Verificar si el número es válido
if 1 <= mes_numero <= 12:
    dias = dias_por_mes[mes_numero]
    print(f"El mes {mes_numero} es {dias} días.")
else:
    print("ERROR: El número introducido no es correcto.")

