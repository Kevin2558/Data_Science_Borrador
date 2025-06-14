# Práctica de Análisis Exploratorio de Datos (EDA) con Titanic
### Objetivo General:

Aplicar un flujo de EDA completo en un solo dataset de Titanic, desde la carga de datos y exploración inicial, pasando por estadísticas descriptivas, limpieza (valores nulos, outliers), manipulación (filtros, creación de columnas) y finalizando con visualizaciones que ayuden a contar una historia de los datos.

**Recomendación Importante:**

Usar la documentación oficial de cada librería (Pandas, NumPy, Matplotlib) cuando surjan dudas.

## Sección 0: Preparación del Entorno y Descarga del Dataset
* Descarga del Titanic-dataset (un solo CSV) desde Kaggle.
Ej.: https://www.kaggle.com/datasets/yasserh/titanic-dataset

* Organiza el archivo (por ejemplo, titanic-dataset.csv) en la misma carpeta de tu Notebook o con la ruta clara para pd.read_csv().

* Instala/Verifica que tienes las librerías: pandas, numpy y matplotlib.

## Sección 1: Carga y Exploración Inicial
1. Ejercicio 1: Carga del CSV y vista general
   * Usa pandas para cargar el DataFrame (llámalo df).
   * Observa y muestra las primeras 5 filas.
   * Revisa la dimensión, la estructura y la descripción estadística.

1. Ejercicio 2: Identificación de columnas y tipos de datos
    * Lista los nombres de las columnas.
    * Verifica los tipos (object, float, int) con df.dtypes.
    * Comenta para qué puede servir cada columna (ej.: Survived indica sobrevivencia).

## Sección 2: Estadísticas Descriptivas y Manejo de Datos

3. Ejercicio 3: Estadísticas básicas
   * Calcula la media, mediana, rango o desviación estándar de columnas numéricas (por ejemplo, Age, Fare).
   * Explora el conteo de valores únicos en columnas categóricas (por ejemplo, Sex, Embarked).

4. Ejercicio 4: Identificación de valores nulos
   * Usa df.isnull().sum() para ver cuántos faltantes hay por columna.
   * Inspecciona si alguna columna (ej. Cabin, Age) tiene muchos valores nulos.
   * Discute brevemente posibles estrategias de imputación o eliminación.
   * Lee la documentación de dropna, fillna y experimenta con distintas imputaciones. Justifica con cuál te quedas y por qué (por ejemplo, df["Age"].fillna(df["Age"].median(), inplace=True)).
  
## Sección 3: Filtrado, Selección y Agrupación

5. Ejercicio 5: Filtros y selección de columnas
   * Selecciona solamente ["Survived","Pclass","Sex","Age","Fare"].
   * Filtra filas donde la Age sea mayor a 50.
   * Filtra filas donde la `Pclass` sea 1 o 2 (usa condiciones compuestas).
6. Ejercicio 6: Agrupaciones (groupby)
   * Agrupa por `Pclass` y muestra la edad promedio de cada clase.
   * Agrupa por Sex y muestra la tasa de supervivencia (ej. df.groupby("Sex")["Survived"].mean()).
   * Haz múltiples agregaciones en un solo groupby (ej. .agg({"Age":["mean","max"],"Fare":"median"})). Siéntete libre de consultar la doc de groupby.

## Sección 4: Creación de Nuevas Columnas y Merges
7. Ejercicio 7: Creación de columnas
    * Crea df["FamilySize"] = df["SibSp"] + df["Parch"] + 1.
    * Analiza la relación entre el tamaño de la familia y la supervivencia (groupby("FamilySize")["Survived"].mean()).
    * Opcional: Genera una columna categórica que clasifique la edad en rangos (niño, joven, adulto, mayor) usando pd.cut.

## Sección 5: Outliers y Limpieza de Datos
8. Ejercicio 8: Detección de outliers
   * Observa la distribución de Fare y Age:
     * Calcula los cuartiles (Q1, Q3) y el rango intercuartílico (IQR).
     * Identifica valores que estén más allá de [Q1 - 1.5*IQR, Q3 + 1.5*IQR].
   * Revisa cuántos outliers aparecen.
   * Decide si eliminas esos outliers o los ajustas, y justifica tu criterio.
   * (Opcional) Aplica la técnica de Winsorizing (búsquela en la documentación o foros) o experimenta con el log de “Fare” para ver si mejora la distribución.

## Sección 6: Visualizaciones con Matplotlib
9. Ejercicio 9: Visualizaciones simples
    * Histograma de la columna Age. Observa si la distribución es sesgada.
    * Bar plot de Sex para ver cuántos hombres vs. mujeres hay.
    * Pie chart (opcional) para ver la proporción de sobrevivientes (Survived).

10. Ejercicio 10: Comparaciones y subgrupos
    * Haz dos histogramas (survived vs. no survived) para comparar edades.
    * Scatter plot de Age vs. Fare, coloreando según Survived (alfa, label, etc.).

(Opcional)
* Crea un FacetGrid con Seaborn (sns.FacetGrid) para ver la distribución de Age segmentada por Sex y Survived.
* Explora boxplots o violin plots para Age/Fare diferenciando grupos.

## Sección 7: Integra y Cuenta una Historia (Síntesis)
11. Ejercicio 11: Mini-Reporte
Resumen de transformaciones:
* ¿Cómo manejaste nulos, outliers, columnas nuevas?
* Principales estadísticas o hallazgos con groupby (por ejemplo, ¿sobreviven más mujeres que hombres?, ¿qué pasa con la clase 1?).
* Visualizaciones clave: 2-3 gráficos que muestren conclusiones relevantes (edad vs. supervivencia, tarifas vs. supervivencia, etc.).
  
Conclusión final de tu EDA:

¿Hay evidencia clara de que ciertas variables influyen en la supervivencia?

¿Te llamó la atención algún outlier?
