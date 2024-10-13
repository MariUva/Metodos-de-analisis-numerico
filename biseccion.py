import sympy as sp

def funcion(expr, x):
    return expr.evalf(subs={x_var: x})

if __name__ == "__main__":
    # Solicitar la función desde la consola
    funcion_str = input("Introduce la función en términos de x (ejemplo: x**3 - x - 4): ")
    
    # Definir la variable
    x_var = sp.symbols('x')
    expr = sp.sympify(funcion_str)

    # Solicitar los valores iniciales de a y b
    a = float(input("Introduce el valor inicial de a: "))
    b = float(input("Introduce el valor inicial de b: "))

    # Solicitar la tolerancia
    tol = float(input("Introduce la tolerancia (por ejemplo, 0.001): "))

    # Calcular el número de iteraciones necesarias
    iteraciones_max = int(sp.log((b - a) / tol, 2)) + 1
    print(f"Número estimado de iteraciones: {iteraciones_max}")

    # Encabezado de la tabla
    print(f"{'Iteración':<10}{'a':<10}{'b':<10}{'x_medio':<15}{'f(x_medio)':<20}{'b - a':<10}")

    # Algoritmo de bisección
    for i in range(1, iteraciones_max + 1):
        # Calcular x_medio
        x_medio = (a + b) / 2
        f_xmedio = funcion(expr, x_medio)

        # Imprimir la fila de la tabla
        print(f"{i:<10}{a:<10.6f}{b:<10.6f}{x_medio:<15.6f}{f_xmedio:<20.10f}{b - a:<10.6f}")

        # Verificar la condición de tolerancia
        if abs(b - a) < tol:
            print(f"La solución ha convergido en la iteración {i}")
            break

        # Actualizar los valores de a o b según el signo de f(x_medio)
        if f_xmedio == 0:
            print(f"La solución exacta es x = {x_medio}")
            break
        elif f_xmedio * funcion(expr, a) < 0:
            b = x_medio
        else:
            a = x_medio
