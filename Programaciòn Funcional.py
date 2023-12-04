from functools import reduce

def calcular_promedio(numeros):
    if not numeros:
        raise ValueError("La lista de números está vacía. No se puede calcular el promedio.")
    return sum(numeros) / len(numeros)

def elevar_al_cuadrado(numero):
    return numero ** 2

def filtrar_numeros_pares(numero):
    return numero % 2 == 0

def funcion_principal(datos):
    try:
        # Validar que todos los elementos sean números
        numeros = list(map(float, datos))

        # Calcular el promedio
        promedio = calcular_promedio(numeros)

        # Elevar al cuadrado cada número
        cuadrados = list(map(elevar_al_cuadrado, numeros))

        # Filtrar números pares
        pares = list(filter(filtrar_numeros_pares, numeros))

        # Sumar todos los cuadrados
        suma_cuadrados = reduce(lambda x, y: x + y, cuadrados)

        return {
            'promedio': promedio,
            'cuadrados': cuadrados,
            'pares': pares,
            'suma_cuadrados': suma_cuadrados
        }

    except ValueError as ve:
        return f"Error: {str(ve)}"

    except Exception as e:
        return f"Error inesperado: {str(e)}"

# Pruebas de la función principal
try:
    datos_ingresados = input("Ingrese una lista de números separados por comas: ").split(",")
    resultado = funcion_principal(datos_ingresados)

    if isinstance(resultado, dict):
        print("Resultados:")
        print(f"Promedio: {resultado['promedio']}")
        print(f"Números al cuadrado: {resultado['cuadrados']}")
        print(f"Números pares: {resultado['pares']}")
        print(f"Suma de los cuadrados: {resultado['suma_cuadrados']}")
    else:
        print(resultado)

except Exception as e:
    print(f"Error inesperado: {str(e)}")
