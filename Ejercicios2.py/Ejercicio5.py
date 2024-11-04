## Escribe un programa que pida un nombre de usuario y una contraseña.
## Y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", sino se da un error. 
# Solicitar nombre de usuario y contraseña
usuario = input("Introduce tu nombre de usuario: ")
contraseña = input("Introduce tu contraseña: ")

# Verificar si el usuario y la contraseña son correctos
if usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error: Usuario o contraseña incorrectos")