def suma(num1, num2):
    try:
        resultado = num1 + num2
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def resta(num1, num2):
    try:
        resultado = num1 - num2
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def producto(num1, num2):
    try:
        resultado = num1 * num2
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None

def division(num1, num2):
    try:
        if num2 == 0:
            raise ZeroDivisionError("No es posible dividir entre cero.")
        resultado = num1 / num2
        return resultado
    except TypeError:
        print("Error: Tipo de dato no válido.")
        return None
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
