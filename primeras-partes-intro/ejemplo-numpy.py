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
