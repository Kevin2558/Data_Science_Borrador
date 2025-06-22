#  Predicción de Trayectoria de Huracanes

1. Modelo estadistico: Este proyecto tiene como objetivo desarrollar un modelo estadístico que permita predecir la trayectoria de huracanes en función de la evolución del campo de presiones atmosféricas. Se utiliza una representación finito-dimensional del campo de presiones basada en elementos finitos no conformes de Crouzeix–Raviart (o conformes, elementos de Lagrange), y un modelo probabilístico de tipo proceso gaussiano de larga memoria para capturar la dinámica temporal.
2. Modelo Basado en redes neuronales para hacer predicciones
---

## Dataset

Se utiliza el dataset:

- **Nombre:** `reanalysis-era5-pressure-levels`
- **Fuente:** [Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu)
- **Fecha de los datos:** 1 de septiembre de 2023
- **Variables principales:** presión a diferentes niveles atmosféricos (en particular, 1000 hPa)

Los datos se descargan en formato NetCDF y representan campos de presión sobre una grilla geográfica.

---

## Objetivo

El objetivo principal es construir un modelo que prediga la trayectoria de un huracán a corto plazo, utilizando como entrada la evolución espacio-temporal del campo de presiones atmosféricas.

---

##  Metodología

1. **Descarga y preprocesamiento** de campos de presión desde ERA5.
2. **Interpolación finito-elemento**: proyección del campo de presión sobre una base de elementos de Crouzeix–Raviart definidos sobre una triangulación del dominio.
3. **Reducción de dimensión**: obtención de los coeficientes finitos que representan el campo.
4. **Modelado temporal**: aplicación de un proceso gaussiano con memoria larga sobre los coeficientes.
5. **Predicción de trayectoria**: estimación de la posición futura del huracán en función del campo de presión proyectado.

---

## Librerías utilizadas

- `xarray` – para manejo de datos NetCDF
- `cdsapi` – para descargar datos desde el Climate Data Store
- `matplotlib`, `cartopy` – para visualización geográfica
- `scipy`, `numpy` – para interpolación y análisis numérico
- `scikit-learn` o `GPy`, `gpytorch` – para modelado gaussiano (dependiendo del backend)
- `meshzoo`, `pygmsh` (opcional) – para generación de mallas triangulares

---

## Notas

- Es necesario contar con una cuenta en Copernicus y aceptar la licencia del dataset antes de descargar.
- Se recomienda ejecutar los experimentos en entorno Python 3.10 o superior.
- No es muy viable esta opcion awkdñawd

---
