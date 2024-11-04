## Crea un programa que pida al usuario dos números y muestre su división. 
## Si el segundo no es cero, o un mensaje de aviso en caso contrario.

numero1=float(input(f"Ingresa el PRIMER numero a DIVIDIR: "))
numero2=float(input(f"Ingresa el SEGUNDO numero a DIVIDIR: "))

if numero2 != 0:
  division= numero1 / numero2
  print(f"La division de {numero1} entre {numero2} es igual a: {division}")
else:
  print(f"El numero que ingresaste es 0, INGRESA otro numero")
