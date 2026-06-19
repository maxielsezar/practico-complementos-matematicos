def bisection(f, a, b, tolerance=1e-6, max_iterations=100):
    """
    Método de bisección para encontrar la raíz de una función.
    
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
    
    while abs(b - a) > tolerance and iterations < max_iterations:
        c = (a + b) / 2
        
        print(f"Iteración {iterations + 1}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={f(c):.6f}")
        
        if f(c) == 0:
            return c, iterations + 1
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iterations += 1
    
    root = (a + b) / 2
    return root, iterations


# Ejemplo: x² - 3 = 0 en el intervalo [1, 2] con 4 iteraciones
print("=" * 70)
print("Método de Bisección: f(x) = x² - 3 en [1, 2]")
print("=" * 70)

def f(x):
    return x**2 - 3

raiz, iteraciones = bisection(f, 1, 2, tolerance=1e-10, max_iterations=4)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL:")
print(f"{'=' * 70}")
print(f"Raíz aproximada: {raiz:.10f}")
print(f"Total de iteraciones: {iteraciones}")
print(f"Verificación - f({raiz:.10f}) = {f(raiz):.2e}")
print(f"Valor esperado (√3): {3**0.5:.10f}")
print(f"Error absoluto: {abs(raiz - 3**0.5):.2e}")
