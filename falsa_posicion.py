def falsa_posicion(f, a, b, tolerance=1e-6, max_iterations=100):
    """
    Método de la Falsa Posición (Regula Falsi) para encontrar la raíz de una función.
    
    A diferencia de la bisección, utiliza interpolación lineal para aproximar la raíz,
    lo que generalmente resulta en una convergencia más rápida.
    
    Parámetros:
    f: función a la cual encontrar la raíz
    a, b: extremos del intervalo [a, b]
    tolerance: tolerancia para convergencia
    max_iterations: número máximo de iteraciones
    
    Retorna:
    root: la raíz aproximada
    iterations: número de iteraciones realizadas
    """
    
    if f(a) * f(b) > 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")
    
    iterations = 0
    fa = f(a)
    fb = f(b)
    
    while abs(b - a) > tolerance and iterations < max_iterations:
        # Fórmula de la falsa posición
        # Encuentra el punto donde la recta que une (a, f(a)) y (b, f(b)) cruza el eje x
        c = a - (fa * (b - a)) / (fb - fa)
        fc = f(c)
        
        print(f"Iteración {iterations + 1}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={fc:.6f}")
        
        if abs(fc) < tolerance or abs(b - a) < tolerance:
            return c, iterations + 1
        
        # Actualizar el intervalo
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        iterations += 1
    
    return c, iterations


# Ejemplo 1: Encontrar √2 (raíz de x² - 2 = 0)
print("=" * 70)
print("Método de la Falsa Posición: f(x) = x² - 2 en [1, 2]")
print("=" * 70)

def f1(x):
    return x**2 - 2

raiz1, iter1 = falsa_posicion(f1, 1, 2, tolerance=1e-8)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL:")
print(f"{'=' * 70}")
print(f"Raíz aproximada: {raiz1:.10f}")
print(f"Total de iteraciones: {iter1}")
print(f"Verificación - f({raiz1:.10f}) = {f1(raiz1):.2e}")
print(f"Valor esperado (√2): {2**0.5:.10f}")
print(f"Error absoluto: {abs(raiz1 - 2**0.5):.2e}\n")


# Ejemplo 2: Encontrar √3 (raíz de x² - 3 = 0) con 4 iteraciones
print("=" * 70)
print("Método de la Falsa Posición: f(x) = x² - 3 en [1, 2]")
print("=" * 70)

def f2(x):
    return x**2 - 3

raiz2, iter2 = falsa_posicion(f2, 1, 2, tolerance=1e-10, max_iterations=4)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL:")
print(f"{'=' * 70}")
print(f"Raíz aproximada: {raiz2:.10f}")
print(f"Total de iteraciones: {iter2}")
print(f"Verificación - f({raiz2:.10f}) = {f2(raiz2):.2e}")
print(f"Valor esperado (√3): {3**0.5:.10f}")
print(f"Error absoluto: {abs(raiz2 - 3**0.5):.2e}\n")


# Ejemplo 3: Encontrar la raíz de x³ - 1 = 0
print("=" * 70)
print("Método de la Falsa Posición: f(x) = x³ - 1 en [0, 2]")
print("=" * 70)

def f3(x):
    return x**3 - 1

raiz3, iter3 = falsa_posicion(f3, 0, 2, tolerance=1e-8)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL:")
print(f"{'=' * 70}")
print(f"Raíz aproximada: {raiz3:.10f}")
print(f"Total de iteraciones: {iter3}")
print(f"Verificación - f({raiz3:.10f}) = {f3(raiz3):.2e}")
print(f"Valor esperado: 1.0000000000")
print(f"Error absoluto: {abs(raiz3 - 1):.2e}\n")


# Ejemplo 4: Comparación con la función x⁴ - 5
print("=" * 70)
print("Método de la Falsa Posición: f(x) = x⁴ - 5 en [1, 2]")
print("=" * 70)

def f4(x):
    return x**4 - 5

raiz4, iter4 = falsa_posicion(f4, 1, 2, tolerance=1e-8)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL:")
print(f"{'=' * 70}")
print(f"Raíz aproximada: {raiz4:.10f}")
print(f"Total de iteraciones: {iter4}")
print(f"Verificación - f({raiz4:.10f}) = {f4(raiz4):.2e}")
print(f"Valor esperado (⁴√5): {5**(1/4):.10f}")
print(f"Error absoluto: {abs(raiz4 - 5**(1/4)):.2e}")
