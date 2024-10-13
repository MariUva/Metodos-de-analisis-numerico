import sympy as sp

def funcion(expr, x):
    return expr.evalf(subs={x_var: x})

if __name__ == "__main__":
    # Solicitar la función desde la consola
    funcion_str = input("Introduce la función en términos de x (usa ** para potencias y exp(x) para exponentes, ejemplo: sqrt(x**2 + 1) - tan(x)): ")
    
    # Reemplazar ^ con ** para compatibilidad
    funcion_str = funcion_str.replace('^', '**')
    
    # Definir la variable
    x_var = sp.symbols('x')
    expr = sp.sympify(funcion_str)

    # Solicitar los valores iniciales de a y b
    a = float(input("Introduce el valor inicial de a: "))
    b = float(input("Introduce el valor inicial de b: "))

    # Solicitar la tolerancia
    tol = float(input("Introduce la tolerancia (por ejemplo, 0.001): "))

    # Encabezado de la tabla
    print(f"{'Iteración':<10}{'a':<12}{'b':<12}{'x_falsa':<15}{'f(x_falsa)':<20}{'b - a':<12}")

    # Algoritmo de falsa posición
    i = 0
    while True:
        # Calcular x_falsa usando la fórmula
        f_a = funcion(expr, a)
        f_b = funcion(expr, b)
        x_falsa = b - (f_b * (a - b)) / (f_a - f_b)
        f_xfalsa = funcion(expr, x_falsa)

        # Imprimir la fila de la tabla
        print(f"{i+1:<10}{a:<12.6f}{b:<12.6f}{x_falsa:<15.6f}{f_xfalsa:<20.10f}{(b - a):<12.6f}")

        # Verificar la condición de tolerancia
        if abs(f_xfalsa) < tol or abs(b - a) < tol:
            print(f"La solución ha convergido en la iteración {i+1}")
            print(f"Solución aproximada: x = {x_falsa:.6f}")
            break

        # Actualizar los valores de a o b según el signo de f(x_falsa)
        if f_xfalsa * f_a < 0:
            b = x_falsa
        else:
            a = x_falsa

        i += 1
