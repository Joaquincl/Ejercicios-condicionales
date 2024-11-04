# Programa que pida dos números ´nota´ y ´edad´ y un carácter ´sexo´
# y muestre el mensaje ´ACEPTADA´ si no la nota se mayor o igual a cinco, la edad es mayor o igual a diciocho y el sexo es ´f´.
# En caso de que se cumpla lo mismo, pero el sexo sea ´m´, debe imprimir ´POSIBLE´.
# si no se cumple dichas condiciones se debe mostrar ´NO ACEPTADA´.
nota = float(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (f/m): ").lower()

# Comprobar las condiciones y mostrar el mensaje correspondiente.
if nota >= 5 and edad >= 18:
    if sexo == 'f':
        print("ACEPTADA")
    elif sexo == 'm':
        print("POSIBLE")
    else:
        print("Sexo no reconocido")
else:
    print("NO ACEPTADA")