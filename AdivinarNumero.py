import random

def adivinar_numero():
    numero_secreto = random.randint(1, 100)  # Generar un número aleatorio entre 1 y 100
    intentos = 0
    
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break

# Iniciar el juego
adivinar_numero()