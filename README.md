# Trabajo Práctico de Complementos Matemáticos

Este proyecto contiene una recopilación de ejercicios y scripts en Python para resolver problemas de análisis numérico, métodos de búsqueda de raíces y graficación de funciones.

## Objetivo del trabajo práctico

El trabajo práctico busca comprender y aplicar conceptos fundamentales de:

- métodos numéricos para encontrar raíces de funciones,
- análisis del error y la convergencia,
- representación de números en punto flotante,
- graficación de funciones para visualizar resultados.

## Archivos del proyecto

- `bisection.py`: implementación del método de bisección para encontrar raíces.
- `falsa_posicion.py`: implementación del método de la falsa posición.
- `metodos_abiertos.py`: implementación de Newton-Raphson, secante y punto fijo.
- `suma_flotante.py`: ejemplo que muestra el efecto de la aritmética de punto flotante en operaciones como `0.1 + 0.2`.
- `graficar_funciones.py`: script para graficar funciones usando `numpy` y `matplotlib`.
- `eliminacion_gauss.py`: script para resolver sistemas de ecuaciones lineales mediante eliminación de Gauss con pivoteo parcial.

## Resumen de la resolución

### 1. Método de bisección
Se utiliza para encontrar una raíz de una función continua cuando se conoce un intervalo `[a, b]` en el que la función cambia de signo.

La idea es:
1. calcular el punto medio del intervalo,
2. evaluar la función en ese punto,
3. reducir el intervalo según el signo de la función,
4. repetir hasta alcanzar la tolerancia deseada.

### 2. Método de la falsa posición
Este método mejora la aproximación utilizando una interpolación lineal entre los extremos del intervalo.

Se aproxima la raíz como la intersección de la recta que une los puntos `(a, f(a))` y `(b, f(b))` con el eje x.

### 3. Métodos abiertos
Se incluyen métodos que no requieren un intervalo cerrado:

- Newton-Raphson: usa la derivada de la función.
- Secante: aproxima la derivada con dos puntos previos.
- Punto fijo: transforma la ecuación `f(x) = 0` en una forma `x = g(x)`.

### 4. Suma en punto flotante
Se demuestra que algunas operaciones decimales no se representan con exactitud en la computadora, lo que provoca resultados inesperados al comparar valores numéricos.

### 5. Graficación de funciones
Se implementó un script que permite graficar una o más funciones en un intervalo determinado y guardar la imagen en formato PNG.

### 6. Eliminación de Gauss
Se agregó un script para resolver sistemas lineales de la forma $Ax = b$ mediante eliminación de Gauss.

Este método transforma la matriz ampliada del sistema en una forma escalonada y luego resuelve por sustitución regresiva. Además, incorpora pivoteo parcial para evitar problemas cuando aparece un cero en la diagonal.

## Requisitos

Para ejecutar las gráficas es necesario tener instaladas las librerías:

```bash
pip install numpy matplotlib
```

## Cómo ejecutar los scripts

Desde la carpeta del proyecto:

```bash
py -3 bisection.py
py -3 falsa_posicion.py
py -3 metodos_abiertos.py
py -3 suma_flotante.py
py -3 graficar_funciones.py
py -3 eliminacion_gauss.py
```

## Resultado esperado

Al ejecutar los scripts se obtienen:

- aproximaciones de raíces de funciones,
- tablas de iteraciones para los métodos numéricos,
- una demostración del comportamiento de los números en punto flotante,
- una gráfica guardada como `grafica_funciones.png`,
- la solución de sistemas lineales mediante eliminación de Gauss.

## Autor

Proyecto desarrollado por Maximiliano Elsezar para el trabajo práctico de Complementos Matemáticos.
