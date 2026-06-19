def newton_raphson(f, df, x0, tolerance=1e-6, max_iterations=100):
    """
    Método de Newton-Raphson para encontrar la raíz de una función.
    
    Requiere la función f y su derivada df.
    Parámetros:
    f: función a la cual encontrar la raíz
    df: derivada de la función
    x0: aproximación inicial
    tolerance: tolerancia para convergencia
    max_iterations: número máximo de iteraciones
    
    Retorna:
    root: la raíz aproximada
    iterations: número de iteraciones realizadas
    """
    
    iterations = 0
    x = x0
    
    print(f"{'Iteración':<12} {'x':<15} {'f(x)':<15} {'f\'(x)':<15}")
    print("=" * 60)
    
    while iterations < max_iterations:
        fx = f(x)
        dfx = df(x)
        
        print(f"{iterations:<12} {x:<15.10f} {fx:<15.10f} {dfx:<15.10f}")
        
        if abs(fx) < tolerance:
            return x, iterations + 1
        
        if dfx == 0:
            raise ValueError(f"La derivada es cero en x = {x}")
        
        # Fórmula de Newton-Raphson: x_new = x - f(x) / f'(x)
        x_new = x - fx / dfx
        
        if abs(x_new - x) < tolerance:
            return x_new, iterations + 1
        
        x = x_new
        iterations += 1
    
    return x, iterations


def secante(f, x0, x1, tolerance=1e-6, max_iterations=100):
    """
    Método de la Secante para encontrar la raíz de una función.
    
    No requiere la derivada, usa dos aproximaciones iniciales.
    Parámetros:
    f: función a la cual encontrar la raíz
    x0, x1: dos aproximaciones iniciales
    tolerance: tolerancia para convergencia
    max_iterations: número máximo de iteraciones
    
    Retorna:
    root: la raíz aproximada
    iterations: número de iteraciones realizadas
    """
    
    iterations = 0
    
    print(f"{'Iteración':<12} {'x_anterior':<15} {'x_actual':<15} {'f(x)':<15}")
    print("=" * 60)
    
    fx0 = f(x0)
    fx1 = f(x1)
    
    while iterations < max_iterations:
        print(f"{iterations:<12} {x0:<15.10f} {x1:<15.10f} {fx1:<15.10f}")
        
        if abs(fx1) < tolerance:
            return x1, iterations + 1
        
        if abs(fx1 - fx0) < 1e-15:
            raise ValueError("Denominador muy pequeño en el método de la secante")
        
        # Fórmula de la secante: x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        if abs(x_new - x1) < tolerance:
            return x_new, iterations + 1
        
        x0 = x1
        fx0 = fx1
        x1 = x_new
        fx1 = f(x1)
        
        iterations += 1
    
    return x1, iterations


def punto_fijo(g, x0, tolerance=1e-6, max_iterations=100):
    """
    Método de Punto Fijo para encontrar la raíz de una función.
    
    Requiere reescribir f(x) = 0 como x = g(x)
    Parámetros:
    g: función de iteración x = g(x)
    x0: aproximación inicial
    tolerance: tolerancia para convergencia
    max_iterations: número máximo de iteraciones
    
    Retorna:
    root: la raíz aproximada
    iterations: número de iteraciones realizadas
    """
    
    iterations = 0
    x = x0
    
    print(f"{'Iteración':<12} {'x':<20} {'|x_new - x|':<15}")
    print("=" * 50)
    
    while iterations < max_iterations:
        x_new = g(x)
        error = abs(x_new - x)
        
        print(f"{iterations:<12} {x:<20.10f} {error:<15.2e}")
        
        if error < tolerance:
            return x_new, iterations + 1
        
        x = x_new
        iterations += 1
    
    return x, iterations


# ============================================================
# EJEMPLO 1: Newton-Raphson para x² - 3 = 0
# ============================================================
print("=" * 70)
print("MÉTODO 1: NEWTON-RAPHSON")
print("=" * 70)
print("\nBúsqueda de √3 usando f(x) = x² - 3")
print("Derivada: f'(x) = 2x")
print("Aproximación inicial: x₀ = 2")
print("-" * 70)

def f1(x):
    return x**2 - 3

def df1(x):
    return 2*x

raiz1, iter1 = newton_raphson(f1, df1, 2.0, tolerance=1e-8)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL - Newton-Raphson:")
print(f"{'=' * 70}")
print(f"Raíz encontrada: {raiz1:.10f}")
print(f"Iteraciones: {iter1}")
print(f"Verificación - f({raiz1:.10f}) = {f1(raiz1):.2e}")
print(f"Valor esperado (√3): {3**0.5:.10f}")
print(f"Error absoluto: {abs(raiz1 - 3**0.5):.2e}\n")


# ============================================================
# EJEMPLO 2: Newton-Raphson para cos(x) - x = 0
# ============================================================
print("=" * 70)
print("BÚSQUEDA DE RAÍZ DE cos(x) - x = 0")
print("-" * 70)

import math

def f2(x):
    return math.cos(x) - x

def df2(x):
    return -math.sin(x) - 1

raiz2, iter2 = newton_raphson(f2, df2, 0.5, tolerance=1e-8)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL - Newton-Raphson:")
print(f"{'=' * 70}")
print(f"Raíz encontrada: {raiz2:.10f}")
print(f"Iteraciones: {iter2}")
print(f"Verificación - f({raiz2:.10f}) = {f2(raiz2):.2e}\n")


# ============================================================
# EJEMPLO 3: Método de la Secante para x² - 3 = 0
# ============================================================
print("=" * 70)
print("MÉTODO 2: SECANTE")
print("=" * 70)
print("\nBúsqueda de √3 usando f(x) = x² - 3")
print("Aproximaciones iniciales: x₀ = 1.5, x₁ = 2.0")
print("-" * 70)

def f3(x):
    return x**2 - 3

raiz3, iter3 = secante(f3, 1.5, 2.0, tolerance=1e-8)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL - Secante:")
print(f"{'=' * 70}")
print(f"Raíz encontrada: {raiz3:.10f}")
print(f"Iteraciones: {iter3}")
print(f"Verificación - f({raiz3:.10f}) = {f3(raiz3):.2e}")
print(f"Valor esperado (√3): {3**0.5:.10f}")
print(f"Error absoluto: {abs(raiz3 - 3**0.5):.2e}\n")


# ============================================================
# EJEMPLO 4: Método de Punto Fijo para x² - 3 = 0
# ============================================================
print("=" * 70)
print("MÉTODO 3: PUNTO FIJO")
print("=" * 70)
print("\nBúsqueda de √3 reescribiendo como x = (x² + 3) / (2x)")
print("Aproximación inicial: x₀ = 2.0")
print("-" * 70)

def g(x):
    # Reescribiendo x² - 3 = 0 como x = (x² + 3) / (2x)
    return (x**2 + 3) / (2*x)

raiz4, iter4 = punto_fijo(g, 2.0, tolerance=1e-8)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL - Punto Fijo:")
print(f"{'=' * 70}")
print(f"Raíz encontrada: {raiz4:.10f}")
print(f"Iteraciones: {iter4}")
print(f"Verificación - f({raiz4:.10f}) = {raiz4**2 - 3:.2e}")
print(f"Valor esperado (√3): {3**0.5:.10f}")
print(f"Error absoluto: {abs(raiz4 - 3**0.5):.2e}\n")


# ============================================================
# COMPARACIÓN DE MÉTODOS
# ============================================================
print("=" * 70)
print("COMPARACIÓN DE MÉTODOS")
print("=" * 70)
print(f"{'Método':<20} {'Raíz Encontrada':<20} {'Iteraciones':<15}")
print("-" * 70)
print(f"{'Newton-Raphson':<20} {raiz1:<20.10f} {iter1:<15}")
print(f"{'Secante':<20} {raiz3:<20.10f} {iter3:<15}")
print(f"{'Punto Fijo':<20} {raiz4:<20.10f} {iter4:<15}")
print(f"{'Valor Real (√3)':<20} {3**0.5:<20.10f} {'-':<15}\n")


# ============================================================
# EJEMPLO 5: Método de Punto Fijo para x³ - 7x² + 14x - 6 = 0
# ============================================================
print("=" * 70)
print("MÉTODO: ITERACIÓN DE PUNTO FIJO")
print("=" * 70)
print("\nBúsqueda de raíz de f(x) = x³ - 7x² + 14x - 6 = 0")
print("Intervalo: [2.7; 3.2]")
print("Reescribiendo como: x = (x³ + 14x - 6) / (7x)")
print("-" * 70)

def g_pf(x):
    # Reescribiendo x³ - 7x² + 14x - 6 = 0 como x = (x³ + 14x - 6) / (7x)
    return (x**3 + 14*x - 6) / (7*x)

raiz_pf, iter_pf = punto_fijo(g_pf, 3.0, tolerance=1e-8)

print(f"\n{'=' * 70}")
print(f"RESULTADO FINAL - Punto Fijo:")
print(f"{'=' * 70}")
print(f"Raíz encontrada: {raiz_pf:.10f}")
print(f"Iteraciones: {iter_pf}")

# Verificación con la función original
def f_pf(x):
    return x**3 - 7*x**2 + 14*x - 6

print(f"Verificación - f({raiz_pf:.10f}) = {f_pf(raiz_pf):.2e}")
print("=" * 70)
