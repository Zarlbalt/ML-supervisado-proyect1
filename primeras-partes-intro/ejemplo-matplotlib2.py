import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# graficas de pastel (pie chart)
# datos para el grafico de pastel
categorias = ["Categoria A", "Categoria B", "Categoria C", "Categoria D"]
valores = [30, 40, 20, 10]

# crear un grafico de pastel
plt.pie(
    valores,
    labels=categorias,
    autopct="%1.1f%%",
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
)
plt.title("distribucion de categorias")
plt.show()

# graficos de barras horizontales
# en lugar de barras verticales, creamos barras horizontales
# en este caso, generamos datos de ventas de productos
productos = [
    "producto A",
    "producto B",
    "producto C",
    "producto D",
]
ventas = [150, 200, 300, 100]
plt.barh(productos, ventas, color="orange")  # grafico de barras horizontales
plt.title("ventas de productos( Barras horizontales)")  # titulo del grafico
plt.xlabel("ventas")  # etiquetas del eje x
plt.ylabel("producto")  # etiqueta del eje Y
plt.show()

# graficos a partir de un dataframe
# generamos datos ficticios para un dataframe con columnas 'salario' y 'edad' de empleados
data = {
    "Nombre": ["Juan", "Ana", "Pedro", "Maria", "Luis"],
    "SALARIO": [30000, 40000, 25000, 50000, 45000],
    "EDAD": [28, 35, 40, 32, 50],
}
# creamos el dataframe
df = pd.DataFrame(data)
# visualizacion de la relacion entre salario y edad usando un grafico de dispersion
df.plot(kind="scatter", x="SALARIO", y="EDAD", color="brown")  # grafico de dispersion
plt.title("relacion entre salario y edad")
plt.xlabel("SALARIO")
plt.ylabel("EDAD")
plt.show()

# guardamos el grafico generado en el disco local(sin necesidad de google drive)
x = np.random.rand(100)  # 100 valores aleatorios para el eje X
y = np.random.rand(100)

output_dir = "img"
os.makedirs(output_dir, exist_ok=True)

plt.plot(x, np.sin(x), label="Seno", color="blue")
plt.plot(x, np.cos(x), label="coseno", color="red")
plt.title("Funciones trigonometricas")
plt.xlabel("Angulo en radianes")
plt.ylabel("Valor de la funcion")
plt.legend()

plt.grid(True)
# guardamos el grafico como img PNG en el entorno local
plt.savefig(os.path.join(output_dir, "funciones_trigonometricas.png"))
plt.show()
# mensaje de confirmacion
print("el grafico se ha guardado correctamente en la ruta indicada.")
