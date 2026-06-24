def eliminacion_gauss(A, b):
    """
    Resuelve un sistema lineal Ax = b usando eliminación de Gauss.

    Parámetros:
    A : matriz de coeficientes como lista de listas
    b : vector de términos independientes como lista

    Retorna:
    x : solución del sistema
    """
    A = [[float(x) for x in fila] for fila in A]
    b = [float(x) for x in b]

    if not A or not A[0]:
        raise ValueError("La matriz A no puede estar vacía")
    if len(A) != len(A[0]):
        raise ValueError("A debe ser una matriz cuadrada")
    if len(A) != len(b):
        raise ValueError("El tamaño de b no coincide con el tamaño de A")

    n = len(b)
    Ab = [fila + [b[i]] for i, fila in enumerate(A)]

    print("Matriz ampliada inicial:")
    for fila in Ab:
        print(fila)
    print()

    for i in range(n):
        pivot_row = max(range(i, n), key=lambda r: abs(Ab[r][i]))

        if abs(Ab[pivot_row][i]) < 1e-15:
            raise ValueError(f"No se puede aplicar la eliminación de Gauss: pivote cero en la columna {i + 1}")

        if pivot_row != i:
            Ab[i], Ab[pivot_row] = Ab[pivot_row], Ab[i]
            print(f"Se intercambiaron las filas {i + 1} y {pivot_row + 1}")

        for j in range(i + 1, n):
            factor = Ab[j][i] / Ab[i][i]
            for k in range(i, n + 1):
                Ab[j][k] -= factor * Ab[i][k]

        print(f"Etapa {i + 1}:")
        for fila in Ab:
            print(fila)
        print()

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(Ab[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (Ab[i][n] - suma) / Ab[i][i]

    return x


if __name__ == "__main__":
    A = [
        [2, 1, -1],
        [4, 2, 2],
        [-2, 3, 1]
    ]
    b = [1, 10, 5]

    solucion = eliminacion_gauss(A, b)
    print("Solución del sistema:")
    print(solucion)
