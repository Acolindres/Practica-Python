# Paso 1 solicitar al usuario que ingrese diferentes tipos de datos
entero_usuario = int(input("Ingrese un número entero: "))
flotante_usuario = float(input("Ingrese un número flotante: "))
cadena_usuario = input("Ingrese una cadena de texto: ")
booleano_usuario = bool(input("Ingrese un valor booleano (True/False): "))

# Paso 2 realizar conversiones de tipos de datos
flotante_a_entero = int(flotante_usuario)
entero_a_flotante = float(entero_usuario)
cadena_a_booleano = bool(cadena_usuario)

# Paso 3imprimir los resultados en diferentes formatos
print("\nValores ingresados:")
print("Número entero:", entero_usuario)
print("Número flotante:", flotante_usuario)
print("Cadena de texto:", cadena_usuario)
print("Valor booleano:", booleano_usuario)

print("\nConversiones de tipos de datos:")
print("Flotante a entero:", flotante_a_entero)
print("Entero a flotante:", entero_a_flotante)
print("Cadena a booleano:", cadena_a_booleano)
