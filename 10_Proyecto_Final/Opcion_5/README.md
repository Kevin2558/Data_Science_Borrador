# Herramienta de Monitoreo de Liquidez Bancaria

## Descripción General

Este proyecto aborda el monitoreo integral del riesgo de liquidez en instituciones bancarias, utilizando como base la normativa de Basilea III y la Comisión para el Mercado Financiero (CMF) de Chile. El objetivo principal es desarrollar un sistema que permita calcular y visualizar métricas claves como el LCR, NSFR, el GAP de liquidez y simular escenarios de estrés, incluyendo la activación de planes de contingencia (Contingency Funding Plan, CFP), utilizando flujos proyectados y activos disponibles.

## Dataset

* **Nombre del Dataset:** Dataset simulado de estructura de balance y flujos de caja bancarios
* **Fuente:** Datos generados artificialmente con base en lineamientos de la CMF y Basilea III
* **Descripción Breve:** Dataset compuesto por proyecciones de flujos de caja, clasificaciones de activos líquidos según nivel HQLA, características de pasivos y activos bancarios, e información necesaria para simular el cálculo del LCR, NSFR y GAP

## Objetivos del Proyecto

Los principales objetivos de este proyecto fueron:

1. Construir un inventario dinámico de activos líquidos de alta calidad (HQLA) aplicando haircuts regulatorios
2. Implementar el cálculo del Índice de Cobertura de Liquidez (LCR) bajo la normativa de la CMF, con flujos esperados de entrada/salida
3. Desarrollar una matriz de GAP de liquidez por tramo temporal. detectando descalces críticos
4. Calcular el Índice de Fondeo Estable Neto (NSFR) a partir de ponderados de ASF y RSF según Basilea III
5. Simular escenarios de estrés de liquidez, como corridas bancarias o congelamiento de mercados, y activar medidas del CFP
6. Consolidar todas las métricas en una arquitectura que funcione como una herramienta profesional de monitoreo

## Metodología

El proceso seguido en este proyecto incluyó las siguientes etapas:

1. **Diseño del marco conceptual y regulatorio:** Se estudió la normativa Basilea III, la regulación chilena de la CMF, y se identificaron los componentes teóricos de LCR, NSFR, GAP y CFP
2. **Construcción del inventario de HQLA:** Clasificación de activos por niveles, aplicación de haircuts y cálculo del stock disponible
3. **Simulación de flujos de caja:** Generación de matrices de entrada y salida proyectadas en horizontes de 1, 7, 30, 90 y 360 días
4. **Modelo de métricas regulatorias:** Cálculo del LCR, NSFR y GAP de liquidez
5. **Simulación de escenarios de estrés:** Corrida de depósitos, caída en precios de activos líquidos y cierre del mercado mayorista
6. **Activación del CFP:** Definición de rutas de liquidez y medidas defensivas
7. **Visualización de resultados y alertas:** Generación de tablas y gráficos para interpretar las métricas clave y condiciones de alerta

## Resultados y Conclusiones Clave



## Tecnologías y Librerías Utilizadas

* Python 3.11
* `pandas`
* `numpy`
* `matplotlib / seaborn`
* `streamlit`
* `openpyxl`
* `warnings`
* `decimal`
* `Microsoft Excel`

## Autor

* **Kevin Ortiz**
* [Github] (https://github.com/Kevin2558/Portafolio_DataScience)
* [LinkedIn] (https://www.linkedin.com/in/kevin-ortiz-collao-16376a275/)

---
