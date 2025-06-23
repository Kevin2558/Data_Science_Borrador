# Predicción de Probabilidad de Incumplimiento en Créditos de Consumo

## Descripción General

Este proyecto aborda la **predicción de la probabilidad de incumplimiento de pago de clientes** en productos de crédito bancario, utilizando el dataset *Default of Credit Card Clients*. El objetivo principal fue construir un modelo de clasificación capaz de estimar el riesgo crediticio individual, entendiendo la relación entre variables demográficas, comportamientos de pago y la ocurrencia del default.

## Dataset

* **Nombre del Dataset:** Default of Credit Card Clients Dataset  
* **Fuente:** [Kaggle - Default of Credit Card Clients](https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset)  
* **Descripción Breve:** El dataset contiene información de 30.000 clientes de una entidad financiera en Taiwán, incluyendo variables demográficas (edad, género, educación), comportamiento de pago en los últimos 6 meses, historial de crédito y monto del default (variable objetivo).

## Objetivos del Proyecto

Los principales objetivos de este proyecto fueron:

1. Explorar y comprender las características del dataset y su relación con el default.
2. Aplicar técnicas de preprocesamiento, balanceo y selección de variables para mejorar la calidad del modelo.
3. Desarrollar y evaluar modelos de clasificación para predecir el incumplimiento de clientes.
4. Analizar la interpretabilidad de los modelos y el impacto de cada variable en la decisión final.

## Metodología

El proceso seguido en este proyecto incluyó las siguientes etapas:

1.  **Carga y Exploración de Datos (EDA):** [Breve descripción de qué se hizo en esta etapa, ej., "análisis de distribuciones, identificación de valores atípicos/faltantes, correlaciones."]
2.  **Preprocesamiento de Datos:** [Descripción de las transformaciones aplicadas, ej., "escalado de características (StandardScaler), codificación de variables categóricas (One-Hot Encoding)."]
3.  **Reducción de Dimensionalidad:** Se utilizó [Técnica de Reducción, ej., PCA (Análisis de Componentes Principales)] para [propósito, ej., "reducir la dimensionalidad del dataset a X componentes principales para facilitar la visualización y mejorar el rendimiento del modelo"].
4.  **Modelado:** Se entrenaron y evaluaron varios modelos de Machine Learning, incluyendo:
    * [Modelo 1, ej., "Regresión Logística"]
    * [Modelo 2, ej., "Support Vector Machine (SVM)"]
    * [Modelo 3, ej., "Random Forest"]
    * [Añadir otros modelos utilizados]
5.  **Evaluación:** El rendimiento de los modelos fue evaluado utilizando métricas como [Métricas de Evaluación, ej., "Accuracy, Precision, Recall, F1-Score (para clasificación)", "MAE, RMSE, R² (para regresión)"].

## Resultados y Conclusiones Clave

* [Conclusión 1: Ej. "PCA logró capturar el 95% de la varianza con solo X componentes, facilitando la visualización."]
* [Conclusión 2: Ej. "El modelo [Nombre del Modelo] obtuvo el mejor rendimiento con [métrica clave] de [valor] en este dataset."]
* [Conclusión 3: Ej. "La reducción de dimensionalidad [mejoró/empeoró/no afectó significativamente] el rendimiento del modelo, pero [razón, ej., "redujo el tiempo de entrenamiento"]."]
* [Conclusión 4: Ej. "Los desafíos encontrados incluyeron [desafío, ej., "el desequilibrio de clases", "la alta dimensionalidad"] y cómo se abordaron."]

## Tecnologías y Librerías Utilizadas

* Python [Versión]
* `pandas`
* `numpy`
* `scikit-learn`
* `matplotlib`
* `seaborn`
* [Añadir cualquier otra librería específica, ej., `tensorflow`, `keras`, `imblearn`]

## Cómo Ejecutar el Proyecto (Opcional)

Para replicar este análisis, sigue estos pasos:

1.  Clona este repositorio: `git clone https://github.com/tu_usuario/nombre_del_repositorio.git`
2.  Navega a la carpeta del proyecto: `cd nombre_del_proyecto_carpeta`
3.  (Opcional, pero recomendado) Crea un entorno virtual: `python -m venv venv`
4.  Activa el entorno virtual:
    * Windows: `.\venv\Scripts\activate`
    * macOS/Linux: `source venv/bin/activate`
5.  Instala las dependencias: `pip install -r requirements.txt`
6.  Abre el Jupyter Notebook: `jupyter notebook [Nombre_del_Notebook].ipynb`
7.  Ejecuta las celdas en orden.

## Autor

* **[Tu Nombre Completo]**
* [Tu Perfil de GitHub (enlace)]
* [Tu Perfil de LinkedIn (enlace)]
