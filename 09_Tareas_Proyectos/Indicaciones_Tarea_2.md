# Tarea 2, parte 1 — Reducción de Dimensionalidad (solo pre-procesamiento)

> **Objetivo:** practicar distintas técnicas de reducción de variables  

---

## Instrucciones generales

1. Descarga el dataset indicado desde Kaggle.  
2. Carga los datos en un notebook (`pandas`) e inspecciona su forma *(filas × columnas)*.  
3. Estandariza las variables numéricas cuando corresponda (`StandardScaler`).  
4. Aplica la técnica de reducción solicitada.  
5. Reporta en tu notebook:  
   - **Número de componentes** retenidos.  
   - **Porcentaje de varianza explicada** (o criterio equivalente).  
   - Una **visualización 2-D** o 3-D (scatter) coloreada con la etiqueta disponible, si existe.  
   - Una breve conclusión (2-3 frases) sobre si la proyección revela estructura o correlaciones.

---

## Lista de ejercicios

| # | Dataset (Kaggle slug) | Tipo / Dimensión | Técnica de reducción solicitada |
|---|-----------------------|------------------|---------------------------------|
| 1 | `zalando-research/fashionmnist` | 70 000 × 784 (imágenes) | **PCA** → conservar 95 % de la varianza |
| 2 | `mchrishtw/human-activity-recognition-with-smartphones` | 10 299 × 561 (sensores) | **PCA** (scree plot) + **ICA** (10 componentes); compara varianza vs. independencia |
| 3 | `wine-quality` | 6 497 × 11 (químico) | **LDA** (proyección supervisada) → 2 componentes y scatter tintos vs. blancos |
| 4 | `credit-card-fraud` | 284 807 × 30 (numérico) | **t-SNE** y **UMAP** a 2 D; colorea fraude / no fraude |
| 5 | `uci-ml/energy-efficiency` | 768 × 8 (regresión) | **PCA** a 2 D; muestra por qué a veces la reducción **no** es necesaria (varianza explicada ≥ 90 %?) |


# Parte 2 — Modelos Supervisados sobre Datos Reducidos

## 🎯 Objetivo
Aplicar modelos supervisados sobre datasets con y sin reducción de dimensionalidad, comparando su rendimiento y utilidad.

---

## 📌 Instrucciones Generales

Para cada uno de los datasets usados en la Parte 1:

1. **Prepara los datos**:
   - Usa la versión reducida del dataset (por PCA, ICA, LDA, etc.).
   - Si es necesario, vuelve a calcular la reducción con `scikit-learn`.

2. **Divide el dataset** en conjuntos de entrenamiento y prueba (ej. 80/20).

3. **Entrena al menos dos modelos supervisados**:
   - Para clasificación: `LogisticRegression`, `KNeighborsClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, etc.
   - Para regresión: `LinearRegression`, `Ridge`, `RandomForestRegressor`, etc.

4. **Evalúa el rendimiento**:
   - Clasificación: `accuracy`, `precision`, `recall`, `F1-score`, `confusion_matrix`, `ROC-AUC`.
   - Regresión: `MAE`, `RMSE`, `R²`.

5. **Compara resultados**:
   - Entrena los mismos modelos usando las **features originales** (sin reducción).
   - Compara el rendimiento con y sin reducción de dimensionalidad.
   - Usa una tabla o resumen visual.

---

## 📊 Reporte Esperado para Cada Dataset

- ✅ Código bien comentado y organizado.
- 📈 Visualizaciones o métricas de evaluación.
- 📊 Tabla comparativa con rendimiento con vs. sin reducción.
- 💬 Mini-conclusión: ¿ayudó la reducción? ¿Cuál modelo funcionó mejor?

---

## 💡 Sugerencias por Dataset

| Dataset                           | Tipo         | Modelos recomendados                          |
|----------------------------------|--------------|-----------------------------------------------|
| Fashion MNIST                    | Clasificación| Logistic Regression, SVM, k-NN                 |
| Human Activity Recognition       | Clasificación| Random Forest, k-NN, Gradient Boosting         |
| Wine Quality                     | Clasificación| Logistic Regression, k-NN, LDA                 |
| Credit Card Fraud Detection      | Clasificación| Logistic Regression, Random Forest             |
| Energy Efficiency (regresión)    | Regresión    | Linear Regression, Ridge, Random Forest        |

---

## 📝 Reflexión Final

Al final del notebook, agrega una sección:

```markdown
## 📌 Reflexión General
- ¿En qué casos la reducción de dimensionalidad **mejoró o perjudicó** el rendimiento?
- ¿Qué técnica y modelo te parecieron más adecuados para cada tipo de datos?
- ¿Recomendarías aplicar reducción de dimensionalidad antes de modelar?
```
---

Enlaces a los Datasets
Fashion MNIST (imágenes de ropa, 70,000 × 784)

Kaggle: https://www.kaggle.com/datasets/zalando-research/fashionmnist

Human Activity Recognition with Smartphones (sensores, 10,299 × 561)

Kaggle: https://www.kaggle.com/datasets/uciml/human-activity-recognition-with-smartphones

Wine Quality (vino tinto y blanco, 6,497 × 11)

Kaggle: https://www.kaggle.com/datasets/rajyellow46/wine-quality

Credit Card Fraud Detection (transacciones, 284,807 × 30)

Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Energy Efficiency (regresión, 768 × 8)

Kaggle: https://www.kaggle.com/datasets/ujjwalchowdhury/energy-efficiency-data-set



### Entrega

- Notebook (.ipynb) bien comentado.  
- Incluye gráficos y celdas con los valores de varianza explicada / independencia.  
- Una sección final “Conclusiones” (máx. ½ página) donde resumas qué técnica te pareció más informativa para cada dataset.
