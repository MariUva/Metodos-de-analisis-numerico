import numpy as np

def jacobi(A, b, x0=None, tol=1e-10):
    """
    Resuelve el sistema Ax = b usando el método de Jacobi.
    
    Parámetros:
    A : ndarray
        Matriz de coeficientes (n x n).
    b : ndarray
        Vector de términos independientes (n).
    x0 : ndarray
        Vector de estimaciones iniciales (n). Si no se proporciona, se inicializa en ceros.
    tol : float
        Tolerancia para el criterio de parada.

    Retorna:
    x : ndarray
        Solución aproximada al sistema.
    """
    
    n = len(b)  # Número de ecuaciones
    x = np.zeros_like(b) if x0 is None else x0  # Estimación inicial

    # Encabezado de la tabla
    print(f"{'Iteración':<10}{'x1':<15}{'x2':<15}{'x3':<15}")

    iteration = 0  # Contador de iteraciones
    while True:
        x_new = np.zeros_like(x)  # Crear un nuevo vector para las estimaciones
        iteration += 1  # Incrementar el contador de iteraciones

        for i in range(n):
            # Calcular la suma de A[i][j] * x[j] para j != i
            sum_ax = np.dot(A[i, :], x) - A[i, i] * x[i]
            # Aplicar la fórmula de Jacobi
            x_new[i] = (b[i] - sum_ax) / A[i, i]

        # Calcular la norma de la diferencia para verificar la convergencia
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            print(f"Convergió en la iteración {iteration}")
            return x_new
        
        # Imprimir la iteración y los valores actuales de x1, x2, x3, ...
        print(f"{iteration:<10}{x_new[0]:<15.6f}{x_new[1]:<15.6f}{x_new[2]:<15.6f}")

        x = x_new  # Actualizar x para la siguiente iteración

# Función para pedir los valores de la matriz A y el vector b
def ingresar_matriz_vector():
    n = int(input("Introduce el tamaño de la matriz A (n x n): "))

    # Ingresar la matriz A
    print("Introduce la matriz A, fila por fila (separada por espacios):")
    A = []
    for i in range(n):
        fila = list(map(float, input(f"Fila {i + 1}: ").split()))
        A.append(fila)
    
    A = np.array(A)

    # Ingresar el vector b
    print("Introduce el vector b (separado por espacios):")
    b = list(map(float, input().split()))
    b = np.array(b)

    # Ingresar el vector inicial x0
    print("Introduce el vector de estimaciones iniciales x0 (separado por espacios):")
    x0 = list(map(float, input().split()))
    x0 = np.array(x0)

    return A, b, x0

# Ejemplo de uso
if __name__ == "__main__":
    # Ingresar la matriz A y el vector b
    A, b, x0 = ingresar_matriz_vector()

    # Ejecutar el método de Jacobi
    solution = jacobi(A, b, x0, tol=1e-10)

    print("La solución es:", solution)
