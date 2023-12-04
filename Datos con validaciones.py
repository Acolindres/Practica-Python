def realizar_operaciones_con_lista(lista):
    try:
        if not lista:
            raise ValueError("La lista está vacía. No se pueden realizar operaciones.")
        
        numeros = [float(num) for num in lista]
        
        maximo = max(numeros)
        minimo = min(numeros)
        promedio = sum(numeros) / len(numeros)
        
        return maximo, minimo, promedio
    
    except ValueError as ve:
        return f"Error: {str(ve)}"
    
    except Exception as e:
        return f"Error inesperado: {str(e)}"

# Pedir al usuario que ingrese números
try:
    numeros_ingresados = input("Ingrese una lista de números separados por comas: ").split(",")
    resultado = realizar_operaciones_con_lista(numeros_ingresados)

    if isinstance(resultado, tuple):
        print(f"Maximo: {resultado[0]}, Minimo: {resultado[1]}, Promedio: {resultado[2]}")
    else:
        print(resultado)

except Exception as e:
    print(f"Error inesperado: {str(e)}")
