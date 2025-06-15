# 08 - Implementación de Modelos

Esta sección muestra cómo llevar un modelo de Machine Learning desde su entrenamiento hasta su implementación básica en producción.

## Contenido

1. **Entrenamiento y Pipeline**
   - Uso de `Pipeline` de Scikit-learn para encapsular preprocesamiento y modelo.
   - Archivo: `entrenamiento_pipeline.ipynb`

2. **Serialización del Modelo**
   - Guardado del modelo con `joblib` para facilitar su reutilización.

3. **Predicción con Nuevos Datos**
   - Ejemplo de cómo cargar el modelo y aplicarlo sobre datos nuevos.
   - Archivo: `prediccion_nuevos_datos.ipynb`

4. **Exposición como API REST**
   - Integración con una API básica usando Flask.
   - Archivo: `api_modelo.py`

Este ejemplo está basado en el dataset de cáncer de mama (`sklearn.datasets.load_breast_cancer`) pero puede adaptarse a cualquier modelo entrenado con Scikit-learn.
