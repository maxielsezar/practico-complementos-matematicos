def biseccion(f, a, b, tolerance=1e-6, max_iterations=100):
    """
    Método de Bisección para encontrar la raíz de una función.
    
    Divide repetidamente el intervalo por la mitad y selecciona el subintervalo
    donde cambia el signo de la función.
    
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
    
    print(f"{'Iteración':<12} {'a':<15} {'b':<15} {'c':<15} {'f(c)':<15}")
    print("=" * 75)
    
    while abs(b - a) > tolerance and iterations < max_iterations:
        c = (a + b) / 2
        fc = f(c)
        
        print(f"{iterations + 1:<12} {a:<15.10f} {b:<15.10f} {c:<15.10f} {fc:<15.10f}")
        
        if abs(fc) < tolerance or abs(b - a) < tolerance:
            return c, iterations + 1
        
        # Actualizar el intervalo
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        
        iterations += 1
    
    return c, iterations


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
    
    print(f"{'Iteración':<12} {'a':<15} {'b':<15} {'c':<15} {'f(c)':<15}")
    print("=" * 75)
    
    while abs(b - a) > tolerance and iterations < max_iterations:
        # Fórmula de la falsa posición
        # Encuentra el punto donde la recta que une (a, f(a)) y (b, f(b)) cruza el eje x
        c = a - (fa * (b - a)) / (fb - fa)
        fc = f(c)
        
        print(f"{iterations + 1:<12} {a:<15.10f} {b:<15.10f} {c:<15.10f} {fc:<15.10f}")
        
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


# ============================================================
# CONSIGNA: Encontrar la raíz de f(x) = 4x⁴ - 9x² + 14x + 1
# en el intervalo [0; 1] con n=5 iteraciones y error < 5%
# ============================================================

def f(x):
    """Función: f(x) = 4x⁴ - 9x² + 14x + 1"""
    return 4*x**4 - 9*x**2 + 14*x + 1

# Parámetros
xl = 0.0
xu = 1.0
max_iter = 5
error_tolerance = 5.0  # 5%

print("=" * 90)
print("PROBLEMA: Encontrar la raíz de f(x) = 4x⁴ - 9x² + 14x + 1")
print(f"Intervalo: [{xl}; {xu}]")
print(f"Máximo de iteraciones: {max_iter}")
print(f"Error máximo permitido: {error_tolerance}%")
print("=" * 90)
print(f"\nVerificación de signos opuestos:")
print(f"f({xl}) = {f(xl):.10f}")
print(f"f({xu}) = {f(xu):.10f}")
print(f"¿Signos opuestos? {f(xl) * f(xu) < 0}\n")

# ============================================================
# MÉTODO: FALSA POSICIÓN CON CÁLCULO DE ERROR RELATIVO
# ============================================================
print("=" * 90)
print("MÉTODO: FALSA POSICIÓN (REGULA FALSI)")
print("=" * 90)

iterations = 0
fa = f(xl)
fb = f(xu)
xr_anterior = 0
error_relativo = float('inf')

print(f"{'It':<4} {'xl':<12} {'xu':<12} {'xr':<12} {'f(xr)':<12} {'Error %':<12}")
print("=" * 90)

while iterations < max_iter and error_relativo > error_tolerance:
    # Fórmula de la falsa posición
    xr = xl - (fa * (xu - xl)) / (fb - fa)
    fxr = f(xr)
    
    # Calcular error relativo porcentual
    if iterations > 0:
        error_relativo = abs((xr - xr_anterior) / xr) * 100 if xr != 0 else float('inf')
    else:
        error_relativo = 100.0
    
    print(f"{iterations + 1:<4} {xl:<12.8f} {xu:<12.8f} {xr:<12.8f} {fxr:<12.8f} {error_relativo:<12.4f}")
    
    # Actualizar el intervalo
    if fa * fxr < 0:
        xu = xr
        fb = fxr
    else:
        xl = xr
        fa = fxr
    
    xr_anterior = xr
    iterations += 1

print("\n" + "=" * 90)
print(f"RESULTADO FINAL - FALSA POSICIÓN:")
print("=" * 90)
print(f"Raíz encontrada: {xr:.10f}")
print(f"Iteraciones realizadas: {iterations}")
print(f"Error relativo final: {error_relativo:.4f}%")
print(f"Verificación - f({xr:.10f}) = {f(xr):.2e}")
print(f"Condición de error < 5%: {error_relativo < error_tolerance} ✓" if error_relativo < error_tolerance else f"Condición de error < 5%: {error_relativo < error_tolerance} ✗")



