def calcular_promedio(notas):
    if not notas:
        return 0  # Devolver 0 si la lista de notas está vacía
    else:
        return sum(notas) / len(notas)

# Inicializar una lista para almacenar las notas ingresadas
notas_ingresadas = []

# Permitir al usuario ingresar notas una por una
while True:
    nota_str = input("Ingrese una nota (o ingrese -1 para terminar): ")

    # Verificar si el usuario quiere salir
    if nota_str == "-1":
        break

    # Convertir la entrada a un número flotante
    try:
        nota = float(nota_str)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    # Agregar la nota a la lista
    notas_ingresadas.append(nota)

# Calcular el promedio utilizando la función calcular_promedio
promedio = calcular_promedio(notas_ingresadas)

# Imprimir el promedio calculado
print(f"\nEl promedio de las notas ingresadas es: {promedio}")
