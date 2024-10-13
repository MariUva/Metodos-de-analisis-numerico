import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iterations=100):
    """
    Resuelve el sistema Ax = b usando el método de Gauss-Seidel.
    
    Parámetros:
    A : ndarray
        Matriz de coeficientes (n x n).
    b : ndarray
        Vector de términos independientes (n).
    x0 : ndarray
        Vector de estimaciones iniciales (n). Si no se proporciona, se inicializa en ceros.
    tol : float
        Tolerancia para el criterio de parada.
    max_iterations : int
        Número máximo de iteraciones.

    Retorna:
    x : ndarray
        Solución aproximada al sistema.
    """
    
    n = len(b)  # Número de ecuaciones
    x = np.zeros_like(b) if x0 is None else x0  # Estimación inicial

    for iteration in range(max_iterations):
        x_new = np.copy(x)  # Copiar x para almacenar nuevas estimaciones

        for i in range(n):
            # Calcular la suma de A[i][j] * x[j] para j != i
            sum1 = np.dot(A[i, :i], x_new[:i])  # Parte de las nuevas estimaciones
            sum2 = np.dot(A[i, i+1:], x[i+1:])  # Parte de las estimaciones anteriores

            # Actualizar el valor de x[i]
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]

        # Calcular el error relativo para verificar la convergencia
        error = np.linalg.norm(x_new - x, ord=np.inf) / np.linalg.norm(x_new, ord=np.inf)

        # Imprimir el estado actual de la iteración
        print(f"Iteración {iteration+1}: x = {x_new}, Error = {error}")

        # Verificar la condición de convergencia
        if error < tol:
            print(f"La solución ha convergido en la iteración {iteration + 1}")
            return x_new

        # Actualizar el valor de x para la siguiente iteración
        x = x_new

    print("No convergió en el número máximo de iteraciones")
    return x

def solicitar_matriz_vector():
    """
    Solicita al usuario que ingrese una matriz y un vector para el sistema de ecuaciones Ax = b.
    """
    n = int(input("Introduce el tamaño de la matriz (n x n): "))

    # Inicializar matriz A
    A = np.zeros((n, n))
    
    print("Introduce los valores de la matriz A (una fila a la vez, separada por espacios):")
    for i in range(n):
        A[i] = [float(x) for x in input(f"Fila {i+1}: ").split()]
    
    # Inicializar vector b
    print("Introduce los valores del vector b (separados por espacios):")
    b = np.array([float(x) for x in input().split()])
    
    return A, b

# Ejemplo de uso
if __name__ == "__main__":
    # Solicitar la matriz A y el vector b
    A, b = solicitar_matriz_vector()
    
    # Valor inicial (opcional)
    x0 = np.zeros(len(b))

    # Ejecutar el método de Gauss-Seidel
    solution = gauss_seidel(A, b, x0, tol=1e-10, max_iterations=25)

    print("La solución es:", solution)
