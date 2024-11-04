# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta
# Función para determinar el resultado del juego
def determinar_ganador(jugador1, jugador2):
    opciones_validas = ["piedra", "papel", "tijera"]

    # Verificar que las opciones sean válidas
    if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
        return "Opción incorrecta"

    # Determinar el resultado del juego
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        return "Gana el jugador 1"
    else:
        return "Gana el jugador 2"

# Leer las opciones de los jugadores
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

# Mostrar el resultado
resultado = determinar_ganador(jugador1, jugador2)
print(resultado)