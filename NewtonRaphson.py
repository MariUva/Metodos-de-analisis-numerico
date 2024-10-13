import sympy as sp
import math

# Función para evaluar f(x)
def funcion(expr, x):
    return expr.evalf(subs={x_var: x})

# Función para evaluar la derivada de f(x)
def derivada(expr, x):
    return expr.diff(x_var).evalf(subs={x_var: x})

if __name__ == "__main__":
    # Solicitar la función desde la consola
    funcion_str = input("Introduce la función en términos de x (usa ** para potencias y atan(x) para arco tangente, ejemplo: 1 - x**2 - atan(x)): ")
    
    # Reemplazar ^ con ** para compatibilidad
    funcion_str = funcion_str.replace('^', '**')
    
    # Definir la variable
    x_var = sp.symbols('x')
    expr = sp.sympify(funcion_str)

    # Solicitar el valor inicial
    x0 = float(input("Introduce el valor inicial x0: "))

    # Solicitar la tolerancia
    tol = float(input("Introduce la tolerancia (por ejemplo, 0.001): "))

    # Encabezado de la tabla
    print(f"{'Iteración':<10}{'x':<15}{'f(x)':<20}{'f\'(x)':<20}{'Error':<10}")

    i = 0
    while True:
        f_x0 = funcion(expr, x0)
        f_prime_x0 = derivada(expr, x0)

        # Calcular el nuevo valor usando la fórmula de Newton-Raphson
        x1 = x0 - f_x0 / f_prime_x0
        # Calcular el error usando la fórmula: e = |(x1 - x0) / x1|
        error = abs((x1 - x0) / x1)

        # Imprimir la fila de la tabla
        print(f"{i+1:<10}{x0:<15.6f}{f_x0:<20.10f}{f_prime_x0:<20.10f}{error:<10.6f}")

        # Verificar la condición de convergencia
        if error < tol:
            print(f"La solución ha convergido en la iteración {i+1}: x = {x1}")
            break

        # Actualizar el valor para la siguiente iteración
        x0 = x1
        i += 1
