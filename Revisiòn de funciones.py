def analizar_datos(datos):
    try:
        if not datos:
            raise ValueError("La lista de datos está vacía. No se pueden realizar operaciones.")

        # Validar que todos los elementos sean números
        numeros = [float(dato) for dato in datos]

        # Clasificación
        positivos = [num for num in numeros if num > 0]
        negativos = [num for num in numeros if num < 0]
        ceros = [num for num in numeros if num == 0]

        # Análisis estadístico
        suma = sum(numeros)
        promedio = suma / len(numeros)
        maximo = max(numeros)
        minimo = min(numeros)

        return {
            'positivos': positivos,
            'negativos': negativos,
            'ceros': ceros,
            'suma': suma,
            'promedio': promedio,
            'maximo': maximo,
            'minimo': minimo
        }

    except ValueError as ve:
        return f"Error: {str(ve)}"

    except Exception as e:
        return f"Error inesperado: {str(e)}"

# Ejemplos de uso
try:
    datos_ingresados = input("Ingrese una lista de datos separados por comas: ").split(",")
    resultado = analizar_datos(datos_ingresados)

    if isinstance(resultado, dict):
        print("Resultados:")
        print(f"Positivos: {resultado['positivos']}")
        print(f"Negativos: {resultado['negativos']}")
        print(f"Ceros: {resultado['ceros']}")
        print(f"Suma: {resultado['suma']}")
        print(f"Promedio: {resultado['promedio']}")
        print(f"Máximo: {resultado['maximo']}")
        print(f"Mínimo: {resultado['minimo']}")
    else:
        print(resultado)

except Exception as e:
    print(f"Error inesperado: {str(e)}")
