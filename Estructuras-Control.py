while True:
    # Solicitar al usuario que ingrese un número
    numero = int(input("Ingrese un número (o un número negativo para salir): "))

    # Verificar si el número es negativo para salir del bucle
    if numero < 0:
        print("¡Programa finalizado!")
        break

    # Determinar si el número es par o impar
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")
