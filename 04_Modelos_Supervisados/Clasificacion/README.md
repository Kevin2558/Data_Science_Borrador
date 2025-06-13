# Clasificación

Modelos supervisados aplicados a problemas de clasificación:

- K-Nearest Neighbors (KNN)
- Support Vector Machines (SVM)
- Árboles de decisión y Random Forest
- Evaluación con métricas como Accuracy, F1-score, Matriz de Confusión

Incluye ejemplos en datasets reales.

# Marco Teórico de los modelos:

# - Regresión Logística

Modelo de clasificación supervisada lineal, diseñado originalmente para resolver problemas de clasificación binaria pero que se puede extender a multiclase. Este modelo en lugar de predecir una clase, predice la probabilidad de pertenecer a una clase.

La idea principal del modelo es calcular la probabilidad de que la clase objetivo sea 1, dado un conjunto de variables *independientes*. Utiliza la función logística (sigmoide) para transformar la combinación lineal de las variables en una probabilidad entre 0 y 1, es decir, la probabilidad de pertenencia de una entrada en la clase 1 viene dada por la función logística.

El modelo se entrena buscando los coeficientes de la combinación que maximicen la verosimilitud. Usualmente, se entrena con métodos de optimización como Descenso del Gradiente (también puede ser Newton-Raphson).

# - K Nearest Neighbors

Modelo de aprendizaje supervisado no paramétrico que se utiliza tanto para clasificación (más común) como para regresión. Este modelo clasifica dependiendo de los k vecinos más cercanos, quienes definirán en que clase ubicar a la entrada.

La idea principal es calcular las distancias entre la nueva entrada y todas las utilizadas en el entrenamiento. Luego, seleccionar los k vecinos más cercanos y se hace una votación por mayoría entre las clases de estos vecinos (clasificación) o se hace un promedio de los valores (regresión).

El modelo no requiere entrenamiento, el "entrenamiento" es proveerle las entradas para que calcule las distancias con las entradas nuevas y pueda modelar. Se pueden utilizar distintas distancias tales como euclideana, manhattan, minkowski, etc.

# - Árboles de Decisión

Modelo supervisado que divide el espacio de caracteríticas (variables) en regiones homogéneas mediante una estructura jerárquica de decisiones. Se utiliza tanto para clasificación como para regresión.

La idea principal es construir un árbol donde cada nodo es una variable y se divide donde se máximice la separación de las clases (clasificación) o se reduce la varianza (regresión).

Los criterios para realizar la división dependen de las funciones a utilizar. En clasificación se puede utiizar la impureza de Gini, la entropía, etc. En regresión se utiliza la varianza o la suma de los errores cuadrados.

Entonces, el proceso de construcción del árbol es el siguiente: Se escoje una característica y se calcula la métrica de calidad de todos los posibles split. Se escoje el split que maximice la pureza y se repite este proceso recursivamente. Los criterios de parada pueden ser alcanzar

En clasificación, la predicción es la clase mayoritaria en la hoja final. En regrsión, la predicción es el promedio de los valores en la hoja.
