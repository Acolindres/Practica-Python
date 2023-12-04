def calcular_operacion(num1, num2, operacion):
    try:
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            resultado = num1 / num2
        else:
            raise ValueError("Operación no válida. Las operaciones válidas son 'suma', 'resta', 'multiplicacion', 'division'.")
        
        return resultado
    
    except ZeroDivisionError:
        return "Error: División por cero no permitida."
    
    except Exception as e:
        return f"Error: {str(e)}"

print(calcular_operacion(5, 2, "suma"))           # Resultado esperado: 7
print(calcular_operacion(5, 2, "resta"))          # Resultado esperado: 3
print(calcular_operacion(3, 4, "multiplicacion"))  # Resultado esperado: 12
print(calcular_operacion(8, 2, "division"))        # Resultado esperado: 4.0
print(calcular_operacion(10, 0, "division"))       # Resultado esperado: "Error: División por cero no permitida."
print(calcular_operacion(5, 2, "potencia"))        # Resultado esperado: "Error: Operación no válida. Las operaciones válidas son 'suma', 'resta', 'multiplicacion', 'division'."
