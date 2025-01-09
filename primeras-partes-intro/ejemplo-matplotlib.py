import numpy as np
import matplotlib.pyplot as plt


# generacion de datos para representar una funcion seno y coseno
x = np.linspace(0, 10, 1000)  # genera array de mil puntos espaciados entre 0 y 10
# creacion de la figura con graficos de seno y coseno
plt.plot(x, np.sin(x), label="seno", color="blue")  # grafico de la funcion seno
plt.plot(x, np.cos(x), label="coseno", color="red")  # grafico de la funcion coseno
plt.show()

# agregamos detalles al grafico (sin datos)
plt.title("funciones Seno y coseno")  # titulo de grafico
plt.xlabel("eje X ( angulo en radianes)")  # etiqueta del eje X
plt.ylabel("Valor de la funcion")  # etiqueta del eje y
plt.legend()  # mostrar la leyenda con los nombres de las funciones
plt.grid(True)  # mostrar la cuadricula
plt.show()


# detalles anteriores pero con datos
x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x), label="seno", color="blue")  # grafico de la funcion seno
plt.plot(x, np.cos(x), label="coseno", color="red")  # grafico de la funcion coseno
plt.title("funciones Seno y coseno")  # titulo de grafico
plt.xlabel("eje X ( angulo en radianes)")  # etiqueta del eje X
plt.ylabel("Valor de la funcion")  # etiqueta del eje y
plt.legend()  # mostrar la leyenda con los nombres de las funciones
plt.grid(True)
plt.show()


# ejemplo con grafico de barras
# en este caso, generamos datos de ventas de productos
productos = [
    "producto A",
    "producto B",
    "producto C",
    "producto D",
]
ventas = [150, 200, 300, 100]
# crear un grafico de barras
plt.bar(productos, ventas, color="green")  # grafico de barras
plt.title("ventas de productos")  # titulo de grafico
plt.xlabel("Productos")  # etiqueta para el eje X
plt.ylabel("Ventas")  # etiqueta para el eje Y
plt.show()


# ejemplo de graficas de dispersion
# Generamos datos alearotios para simular una relacion entre dos variables
x = np.random.rand(100)  # 100 valores aleatorios para el eje X
y = np.random.rand(100)  # 100 valores aleatorios para el eje Y

plt.scatter(x, y, color="purple", alpha=0.6)  # alpha controla la transparencia
plt.title("grafico de dispersion aleatorio")  # titulo del grafico
plt.xlabel("variable x")  # etiqueta del eje X
plt.ylabel("Variable y")  # etiqueta del eje y
plt.show()


# graficos de varias lineas con diferentes estilos
plt.plot(x, np.sin(x), linestyle="-", label="seno")  # linea continua
plt.plot(x, np.cos(x), linestyle="--", label="coseno")  # linea descontinua
plt.plot(x, np.tan(x), linestyle=":", label="tangente")  # linea punteada
plt.title(
    "Funciones trigonometricas con diferentes estilos de linea"
)  # titulo del grafico
plt.xlabel("Angulo de radianes")  # etiqueta del eje X
plt.ylabel("Valor de la funcion")  # etiqueta del eje y
plt.legend()  # muestra la leyenda
plt.ylim(
    0, 1.6
)  # lmitamos el rango de valores para evitar valores extremadamente altos
plt.xlim(0, 1)
plt.show()
