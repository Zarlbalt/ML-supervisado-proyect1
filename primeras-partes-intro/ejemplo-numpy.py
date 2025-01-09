import numpy as np

# 1. creacion de array simple a partir de una lista de numeros
# se creara una lista con valores enteros del 1 al 10 y convertirla en un array de numpy
# array
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array = np.array(lista)
print("Array original: ", array)

# 2. Generacion de numeros en un rango con np.arange
# Se usa np.arange para generar una secuencia de numeros del 0 al 20, con un paso de 2
range_array = np.arange(0, 20, 2)
print("array con np.arange (de 0 a 20 con paso de 2):", range_array)

# 3 generacion de un numero aleatorio con np.random.randint
# vamos a generar un numero aleatorio entre 0 y 100
aleatorio = np.random.randint(0, 100)
print("numero aleatorio entre 0 y 100:", aleatorio)

# 4 generacion de multiples numeros aleatorios
# ahora generamos 10 numeros aleatorios entre 0 y 99
array_random = np.random.randint(0, 99, 10)
print("array con 10 numeros aleatorios entre 0 y 100:", array_random)

# 5 operaciones basicas sobre el array
# operamos sobre el array para encontrar el valor maximo, la posicion del valor
# maximo, el valor minimo y el promedio
print("Valor maximo del array:", array.max())  # valor maximo
print("Indice del valor maximo:", array.argmax())  # indice de valor maximo
print("valor minimo del array:", array.min())  # valor minimo
print("promedio del array:", array.mean())  # promedio de los elementos del array


# 6 acceso a elementos especificos del array
# podemos acceder a los elementos de un array usando indices. tambien podemos
# hacer sclicing para obtener subarrays.
print(
    "elementos en la posicion 2 del array:", array[2]
)  # acceso al tercer elemento (indice 2)

# 7 modificacion de la forma del array (reshape)
# usamos reshape para cambiar la forma del array a 5 filas y 2 columnas. esto no
# cambia los datos, solo la visualizacion.
array_reshaped = array.reshape(5, 2)
print("array con reshape (5 filas, 2columnas):")
print(array_reshaped)

# 8filtrando de elementos en un array
# usamos una condicion para crear un nuevo array con solo los elementos mayores que 30
array_filtrado = array_random[array_random > 30]
print("array filtrado con valores mayores que 30:", array_filtrado)

# 9 tratamiento de valores NaN (not a number)
# creamos un array con algunos valores NaN para demostrar como manejarlos.
# NaN se utiliza cuando hay datos faltantes.
array_nan = np.asanyarray([np.nan, 2, np.nan, 3, 4, np.nan])
print("array con valores NaN:", array_nan)

# 10 reemplazar Nan por un valor especifico (0 en este caso)
# copiamos el array original y sustituimos todos los Nan por ceros
array_sin_nan = array_nan.copy()
array_sin_nan[np.isnan(array_sin_nan)] = 0
print("array despues de reemplazar NaN por 0:", array_sin_nan)

# 11 Realizacion de operaciones matematicas elementales
# vamos a realizar algunas operaciones matematicas comunes, como la suma, resta, multiplicacion y division entr arrays
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

# suma de arrays
array_suma = array_1 + array_2
print("Suma de arrays:", array_suma)

# resta de arrays
array_resta = array_1 - array_2
print("resta de arrays:", array_resta)

# multiplicacion de arrays
array_multiplicacion = array_1 * array_2
print("multiplicacion de arrays:", array_multiplicacion)

# divicion de arrays
array_divicion = array_1 / array_2
print("divicion de arrays:", array_divicion)

# 12 funciones trigonometricas
# usamos funciones trigonometricas de numpy para trabajar con arrays que contienen angulos.
# vamos a crear un array de angulos (en radianes) y calcular el seno y el coseno de estos valores.
angles = np.array([0, np.pi / 4, np.pi / 2, np.pi])
print("seno de los angulos:", np.sin(angles))
print("coseno de los angulos:", np.cos(angles))

# 13. operaciones sobre matrices (arrays 2D)
# creamos dos matrices y realizamos operaciones matriciales como la multiplicacion y la transposicion.
matriz_1 = np.array([[1, 2], [3, 4]])
matriz_2 = np.array([[5, 6], [7, 8]])

# multiplicacion de matrices
producto_matrices = np.dot(matriz_1, matriz_2)
print("producto de matrices:")
print(producto_matrices)

# transposicion de una matriz
matriz_transpuesta = np.transpose(matriz_1)
print("Matriz transpuesta:")
print(matriz_transpuesta)

# 14 generacion de numeros con una distribucion normal
# generamos 1000 numeros aleatorios con distribucion normal
# (media 0 y desviacion estandar 1)
array_normal = np.random.randn(1000)
print("primeros 10 numeros generados con distribucion normal:", array_normal[:10])

# 15 estadisticas descriptivas sobre arrays
# calculamos algunas estadisticas basicas como la media, mediana y desviacion
# estandar de un array
print("Media del array:", np.mean(array_normal))
print("mediana del array:", np.median(array_normal))
print("desviacion estandar del array:", np.std(array_normal))


# 16 operaciones avanzadas: Broadcasting
# broad casting permite realizar operaciones entre arrays de diferentes dimensiones
# por ejemplo, podemos sumar un array de un 1D a uno de 2D.
array_2d = np.array([[1, 2], [3, 4], [5, 6]])
array_1d = np.array([1, 2])
resultado = array_2d + array_1d
print("Resultado de la operacion con broadcasting:")
print(resultado)
