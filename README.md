"# ML-supervisado-proyect1" 
Este código implementa un flujo de trabajo de clasificación utilizando tres algoritmos de machine learning: naive bayes, regresión logística y k-vecinos más cercanos (knn). Se aplica en dos escenarios de clasificación: uno utilizando el conjunto de datos de mensajes de texto (spam vs. ham) y otro utilizando el conjunto de datos iris. 

Ambos problemas son clasificaciones supervisadas, donde el objetivo es predecir una categoría (ya sea "spam" o "ham" en el caso de los mensajes de texto, o una especie de flor en el caso de iris) a partir de un conjunto de características. El código sigue un flujo de trabajo similar en ambos casos, que incluye la carga y preprocesamiento de datos, la división de los datos en conjuntos de entrenamiento y prueba, el entrenamiento de modelos, la evaluación de su rendimiento y la predicción de nuevos datos.



Algoritmos utilizados

1. naive bayes:
naive bayes es un clasificador probabilístico basado en el teorema de Bayes, que asume que las características son independientes entre sí. Este modelo es eficaz en muchos problemas de clasificación, incluyendo la clasificación de texto (spam vs. ham) y clasificación multiclase (como en el conjunto de datos iris).

2. regresión logística:
regresión logística es un modelo estadístico utilizado para clasificación binaria, pero puede extenderse a clasificación multiclase. En este código, se utiliza tanto para predecir si un mensaje es spam o ham, como para clasificar las flores del conjunto iris en una de tres especies.

3. k-vecinos más cercanos (knn):
knn clasifica un nuevo punto de datos en función de los puntos más cercanos en el espacio de características. Es un algoritmo sencillo pero potente para la clasificación tanto binaria como multiclase, como se demuestra con los mensajes de texto y el conjunto iris.



Flujo del programa

El flujo de trabajo sigue una estructura coherente que se aplica tanto a la clasificación de mensajes de texto como a la clasificación con el conjunto iris:

1. cargar y preprocesar los datos
2. división de los datos
3. entrenamiento y evaluación de los modelos
4. visualización de resultados
5. predicción de nuevos datos