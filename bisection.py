def bisection(f, xl, xu, tolerance=1e-6, max_iterations=100):
    """
    Método de bisección para encontrar la raíz de una función.
    
    Parámetros:
    f: función a la cual encontrar la raíz
    xl, xu: extremos del intervalo [xl, xu]
    tolerance: tolerancia para convergencia
    max_iterations: número máximo de iteraciones
    
    Retorna:
    root: la raíz aproximada
    iterations: número de iteraciones realizadas
    """
    
    if f(xl) * f(xu) > 0:
        raise ValueError("f(xl) y f(xu) deben tener signos opuestos")
    
    iterations = 0
    
    while abs(xu - xl) > tolerance and iterations < max_iterations:
        xr = (xl + xu) / 2
        
        print(f"Iteración {iterations + 1}: xl={xl:.6f}, xu={xu:.6f}, xr={xr:.6f}, f(xr)={f(xr):.6f}")
        
        if f(xr) == 0:
            return xr, iterations + 1
        elif f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
        
        iterations += 1
    
    root = (xl + xu) / 2
    return root, iterations


# Ejemplo: x² - x - 1 = 0 en el intervalo [0, 2]
print("=" * 70)
print("Método de Bisección: f(x) = x² - x - 1 en [0, 2]")
print("=" * 70)

def f(x):
    return x**2 - x - 1

raiz, iteraciones = bisection(f, 0, 2, tolerance=0.08, max_iterations=100)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL:")
print(f"{'=' * 70}")
print(f"Raíz aproximada: {raiz:.10f}")
print(f"Total de iteraciones: {iteraciones}")
print(f"Verificación - f({raiz:.10f}) = {f(raiz):.2e}")
print(f"Valor esperado (φ = (1+√5)/2): {(1+5**0.5)/2:.10f}")
print(f"Error absoluto: {abs(raiz - (1+5**0.5)/2):.2e}")


# Ejemplo 2: x³ - 7x² + 14x - 6 = 0 en el intervalo [2.7; 3.2]
print("\n" + "=" * 70)
print("Método de Bisección: f(x) = x³ - 7x² + 14x - 6 en [2.7; 3.2]")
print("=" * 70)

def f2(x):
    return x**3 - 7*x**2 + 14*x - 6

raiz2, iteraciones2 = bisection(f2, 2.7, 3.2, tolerance=0.08, max_iterations=100)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL:")
print(f"{'=' * 70}")
print(f"Raíz aproximada: {raiz2:.10f}")
print(f"Total de iteraciones: {iteraciones2}")
print(f"Verificación - f({raiz2:.10f}) = {f2(raiz2):.2e}")
