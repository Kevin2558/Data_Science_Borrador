# Tarea: EDA con “House Sales in King County, USA”

1. **Objetivo de la Tarea**:
   Aplicar todo lo aprendido sobre Exploración de Datos (EDA) en un contexto realista. El dataset de House Sales in King County contiene información sobre ventas de casas (precio, número de habitaciones, metros cuadrados, ubicación, etc.). Su misión es analizar, limpiar y descubrir patrones usando las técnicas de estadística y visualización vistas en clase.
   Pueden formar grupos de 2 a 3 alumnos. Indicar nombres de sus integrantes en la primera celda del notebook de entrega.

2. **Descripción del Dataset**
   Fuente Kaggle: [House Sales in King County, USA](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)
   
   Columnas Principales (ejemplos):

   - price: Precio de venta de la casa.
   - bedrooms, bathrooms: Número de habitaciones y baños.
   - sqft_living, sqft_lot: Metros cuadrados construidos y de terreno.
   - floors: Número de pisos.
   - waterfront: 1 si la casa está frente al lago/agua, 0 si no.
   - view: Índice de la calidad de la vista.
   - condition, grade: Estado general de la casa, calificaciones.
   - yr_built, yr_renovated: Año de construcción y de renovación (si corresponde).
   - lat, long: Coordenadas geográficas.

   ... y más.

   Tamaño: ~21 613 filas, 19 columnas.

3. **Requerimientos Técnicos**
   1. Usa Python en un Jupyter Notebook (o Google Colab).
   2. Asegúrate de tener instaladas las librerías: pandas, numpy, matplotlib, seaborn (o cualquier otra de visualización).
   3. Opcionalmente, puedes experimentar con ydata-profiling o Sweetviz si deseas un reporte automático, pero se requiere que muestres también un EDA manual (groupby, histogramas, boxplots, correlaciones, etc.).

4. **Instrucciones Detalladas**
   
   4.1. Carga y Exploración Básica
      - Carga el CSV de Kaggle en un DataFrame.
      - Muestra las primeras 5 filas (.head()), la estructura (.info()) y la descripción (.describe()).
      - Identifica si hay valores nulos. ¿En qué columnas? ¿En qué proporción?

   4.2. Limpieza y Manejo de Datos
      - Verifica si alguna columna requiere conversión de tipo (por ejemplo, date).
      - Decide cómo manejar los valores nulos (imputar, eliminar). Justifica tu elección.
      - Explora la columna bedrooms o bathrooms para detectar posibles valores atípicos (por ejemplo, 33 bedrooms, si existe).
   
   4.3. Estadística Descriptiva Avanzada
      - Calcula la media, mediana, IQR y rango de variables clave (ej. price, sqft_living, sqft_lot).
      - Detecta outliers usando la regla 1.5 · IQR en price o sqft_living. Decide si los mantienes o los filtras. Comenta el criterio.
      - Observa la distribución de variables categóricas (por ejemplo, floors, bedrooms).

   4.4. Visualizaciones
      - Genera al menos 5 gráficas relevantes:
      - Histogramas para ver la distribución de price, sqft_living, etc.
      - Boxplot para identificar outliers (por ejemplo, price).
      - Scatter Plot: Relación sqft_living vs. price.
      - Mapa de calor (heatmap) de correlaciones con seaborn.
      - Alguna visualización segmentada (por ejemplo, un FacetGrid o barplot comparando distintas categorías como floors o view frente a price).

   4.5. Análisis de Correlación
      - Examina la matriz de correlaciones (df.corr()).
      - Identifica la correlación más alta y más baja con price. ¿Te sorprende alguna?
      - Escoge 2 correlaciones destacadas y crea un gráfico (scatter, regplot) para visualizarlas.

   4.6. Conclusiones
      - Resumiendo: ¿Qué factores parecen más influyentes en el precio de una casa?
      - ¿Hallaste algún dato curioso o anormal en el dataset? (ej.: casas con 0 bathrooms, precios extremadamente altos).
      - Propón 1-2 ideas para un eventual modelo predictivo (ej. “Podríamos usar sqft_living, bedrooms, view, grade para predecir el price”).
  
5. Formato de Entrega
   - Notebook (.ipynb) con celdas de código y celdas Markdown para las explicaciones.
   - Nombra tu archivo como: EDA_KingCounty_Grupo_N.ipynb.
   - Sube el notebook a este repositorio en la carpeta entregas (o envíalo por correo).

6. Fecha Límite
   21-04-2025 (23:59)