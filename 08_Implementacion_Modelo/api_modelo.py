from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.datasets import load_breast_cancer

# Cargar modelo entrenado
modelo = joblib.load('modelo_entrenado.joblib')

# Obtener nombres de columnas desde el dataset original
columnas = load_breast_cancer().feature_names

app = Flask(__name__)

@app.route('/')
def home():
    return "API de predicción - Logistic Regression (breast cancer)"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data], columns=columnas)
        pred = modelo.predict(df)
        return jsonify({'prediccion': int(pred[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
