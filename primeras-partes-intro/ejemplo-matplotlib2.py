import pandas as pd
import matplotlib.pyplot as plt

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
