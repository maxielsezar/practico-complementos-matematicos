import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def graficar_funciones(funciones, xmin, xmax, muestras=500, titulo="Gráfica de funciones", nombre_archivo="grafica_funciones.png"):
    """
    Grafica una o varias funciones en un intervalo dado.

    Parámetros:
    funciones: lista de tuplas (nombre, funcion)
    xmin, xmax: límites del eje x
    muestras: número de puntos para dibujar la curva
    titulo: título de la gráfica
    nombre_archivo: nombre del archivo PNG que se guardará
    """
    x = np.linspace(xmin, xmax, muestras)

    plt.figure(figsize=(9, 5))

    for nombre, funcion in funciones:
        y = [funcion(valor) for valor in x]
        plt.plot(x, y, label=nombre, linewidth=1.8)

    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(nombre_archivo, dpi=300)
    plt.close()

    print(f"Gráfica guardada en: {nombre_archivo}")


if __name__ == "__main__":
    def f1(x):
        return x**2 - x - 1

    def f2(x):
        return x**3 - 7*x**2 + 14*x - 6

    graficar_funciones(
        funciones=[
            ("x² - x - 1", f1),
            ("x³ - 7x² + 14x - 6", f2),
        ],
        xmin=-2,
        xmax=4,
        titulo="Ejemplos de funciones",
    )
