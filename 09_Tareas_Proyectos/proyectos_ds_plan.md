# Plan de Desarrollo de Proyectos de Ciencia de Datos

Este documento contiene una guía paso a paso para el desarrollo de 6 proyectos de ciencia de datos, cubriendo distintas áreas: finanzas, salud, sostenibilidad, energía y procesamiento de texto.

---

## 1. Scoring de Crédito (Finanzas)

**Objetivo:** Predecir si un cliente incumplirá un crédito.

**Dataset:**
- [Give Me Some Credit - Kaggle](https://www.kaggle.com/datasets/c/GiveMeSomeCredit)
- [Home Credit Default Risk - Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk)

**Pasos:**
1. Recolectar datos.
2. Realizar EDA: perfiles de clientes, distribución de impagos.
3. Preprocesar: imputación, escalado, codificación, SMOTE.
4. Modelado: regresión logística, Random Forest, XGBoost.
5. Evaluación: AUC, matriz de confusión, KS, Gini.
6. Interpretabilidad: SHAP, Permutation Importance.
7. Despliegue (opcional): API con FastAPI o app con Streamlit.

---

## 2. Churn Bancario (Finanzas/Marketing)

**Objetivo:** Predecir abandono de clientes para campañas de retención.

**Dataset:**
- [Bank Customer Churn Prediction - Kaggle](https://www.kaggle.com/datasets/adammaus/predicting-churn-for-bank-customers)

**Pasos:**
1. EDA: comparaciones entre clientes que se van vs permanecen.
2. Preprocesamiento: codificación, balanceo, ingeniería de variables.
3. Modelado: Logistic Regression, Random Forest, XGBoost.
4. Evaluación: Precision, Recall, F1, ROC AUC.
5. Interpretabilidad: SHAP, análisis de segmentos de riesgo.
6. Despliegue: API o Streamlit.

---

## 3. Clasificación de Tos para Diagnóstico (Salud)

**Objetivo:** Clasificar audios de tos para detectar enfermedades respiratorias.

**Dataset:**
- [Coswara Dataset (India Institute of Science)](https://github.com/iiscleap/Coswara-Data)
- [MIT Open Voice Dataset](https://www.physionet.org/content/covid19-sounds/)

**Pasos:**
1. Preprocesamiento de audio: limpieza, normalización, espectrogramas.
2. Extracción de features: MFCCs, Chroma, ZCR, etc.
3. Modelado:
   - Clásico: Random Forest sobre MFCCs.
   - Deep Learning: CNN sobre espectrogramas.
4. Evaluación: AUC, F1 por clase, Grad-CAM.
5. Interpretabilidad: análisis de espectros mal clasificados.
6. Despliegue: App en Streamlit.

---

## 4. Clasificación de Basura para Reciclaje (Imágenes)

**Objetivo:** Identificar tipo de residuo en imágenes para reciclaje automatizado.

**Dataset:**
- [TrashNet Dataset](https://github.com/garythung/trashnet)

**Pasos:**
1. Preprocesamiento: redimensionamiento, normalización, aumento de datos.
2. Modelado:
   - CNN desde cero.
   - Transfer Learning (ResNet50, EfficientNet).
3. Evaluación: accuracy por clase, matriz de confusión.
4. Interpretabilidad: Grad-CAM.
5. Despliegue: Streamlit o API.

---

## 5. Predicción de Demanda Energética (Series Temporales)

**Objetivo:** Predecir consumo energético diario para planificación.

**Dataset:**
- [UCI Household Power Consumption Dataset](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption)
- [Red Eléctrica de España - Datos abiertos](https://www.ree.es/es/datos)

**Pasos:**
1. EDA: descomposición de series, análisis de estacionalidad.
2. Preprocesamiento: resampleo, imputación, normalización.
3. Modelado:
   - ARIMA/SARIMA
   - Prophet
   - LSTM
4. Evaluación: MAE, RMSE, MAPE.
5. Visualización de predicciones.
6. Interpretabilidad: error por segmento temporal.

---

## 6. Clasificación de Reclamos de Clientes (Texto)

**Objetivo:** Clasificar correos/reclamos según su temática (fraude, cobros, etc.).

**Dataset:**
- [CFPB Consumer Complaints - US Government](https://www.consumerfinance.gov/data-research/consumer-complaints/)

**Pasos:**
1. Preprocesamiento: lematización, stopwords, limpieza.
2. Vectorización: TF-IDF, Word2Vec o BERT embeddings.
3. Modelado: LogisticRegression, XGBoost, SVC, Transformers.
4. Evaluación: F1-score por clase, matriz de confusión.
5. Interpretabilidad: LIME, SHAP.
6. Despliegue: API REST o app interactiva.

---

Puedes ir avanzando proyecto por proyecto, documentando en GitHub y añadiendo README claros, notebooks ordenados y despliegues opcionales para cada uno. ¿Quieres que te ayude a iniciar alguno en particular con código base?

