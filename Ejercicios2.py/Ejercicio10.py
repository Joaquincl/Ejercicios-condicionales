#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
#de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
#sin importar el número de alumnos. 
#Realice un programa que permita determinar el pago a la compañía de autobuses 
#y lo que debe pagar cada alumno por el viaje.

## Solicitar el número de alumnos al director
num_alumnos = int(input("Introduce el número de alumnos que van al viaje: "))

# Determinar el costo por alumno y el costo total a la compañía
if num_alumnos >= 100:
    costo_por_alumno = 65
    total_pago_compañía = num_alumnos * costo_por_alumno
elif 50 <= num_alumnos <= 99:
    costo_por_alumno = 70
    total_pago_compañía = num_alumnos * costo_por_alumno
elif 30 <= num_alumnos <= 49:
    costo_por_alumno = 95
    total_pago_compañía = num_alumnos * costo_por_alumno
else:
    # Costo total fijo si son menos de 30 alumnos
    total_pago_compañía = 4000
    costo_por_alumno = total_pago_compañía / num_alumnos

# Mostrar el resultado
print(f"El pago total a la compañía de autobuses es de: {total_pago_compañía} euros")
print(f"Cada alumno debe pagar: {costo_por_alumno:.2f} euros")