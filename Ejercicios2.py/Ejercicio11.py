#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un programa para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.
# Solicitar la duración de la llamada y el día de la semana
duracion = int(input("Introduce la duración de la llamada en minutos: "))
dia = input("Introduce el día de la semana (domingo/otro): ").lower()
turno = None

# Si el día no es domingo, pedir el turno
if dia != "domingo":
    turno = input("Introduce el turno (mañana/tarde): ").lower()

# Calcular el costo base de la llamada
costo = 0
if duracion <= 5:
    costo = duracion * 1  # 1 euro por minuto los primeros 5 minutos
elif duracion <= 8:
    costo = 5 * 1 + (duracion - 5) * 0.8  # 80 céntimos por minuto para los siguientes 3 minutos
elif duracion <= 10:
    costo = 5 * 1 + 3 * 0.8 + (duracion - 8) * 0.7  # 70 céntimos por minuto para los siguientes 2 minutos
else:
    costo = 5 * 1 + 3 * 0.8 + 2 * 0.7 + (duracion - 10) * 0.5  # 50 céntimos por minuto a partir del décimo minuto

# Calcular el impuesto
impuesto = 0
if dia == "domingo":
    impuesto = costo * 0.03  # Impuesto del 3 % si es domingo
elif turno == "mañana":
    impuesto = costo * 0.15  # Impuesto del 15 % en turno de mañana
elif turno == "tarde":
    impuesto = costo * 0.10  # Impuesto del 10 % en turno de tarde

# Calcular el costo total
costo_total = costo + impuesto

# Mostrar los resultados
print(f"Costo base de la llamada: {costo:.2f} euros")
print(f"Impuesto aplicado: {impuesto:.2f} euros")
print(f"Costo total de la llamada: {costo_total:.2f} euros")