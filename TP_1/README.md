# Trabajo Práctico de **Aprendizaje Automático 1**: 
## *Predicción de precios de casas*
### Tecnicatura Universitaria en Inteligencia Artificial – FCEIA, Universidad Nacional de Rosario

## Integrantes

| Apellido y nombre | Usuario de GitHub |
|---|---|
| Mendoza, Emmanuel | @emmamz1 |
| Ruiz, Irma Carolina | @CaroRuiz92 |
| Toledo, Alvaro | @AlvaTF |

## Propósito

Este repositorio contiene la resolución del trabajo práctico de regresión de la materia. El problema consiste en predecir **MEDV** (valor mediano de las viviendas ocupadas por sus propietarios, en miles de dólares) a partir de 13 variables socioeconómicas y urbanas del dataset de precios de casas de Boston (`house-prices.csv`).

## Estructura del repositorio

```
TP_AA1_Apellido1_Apellido2_Apellido3/
├── TP_1/
   ├── README.md                # Este archivo
   ├── TP-regresion-AA1.ipynb   # Notebook de trabajo con todo el desarrollo
   └── house-prices.csv         # Dataset utilizado
```

## Contenido del notebook

1. **Análisis descriptivo**: 
   - Exploración inicial del dataset.
   - Tratamiento de valores faltantes y eliminación de registros sin variable objetivo.
   - Análisis estadístico descriptivo.
   - Visualizaciones (histogramas, scatterplots, boxplots y matriz de correlación).
   - División de los datos en entrenamiento y prueba.
   - Escalado de variables mediante un pipeline de preprocesamiento.
2. **Regresión lineal múltiple**:
   - `LinearRegression`
   - Implementación de Batch Gradient Descent, Stochastic Gradient Descent y Mini-Batch Gradient Descent.
   - Regularización mediante Ridge, Lasso y Elastic Net.
   - Evaluación de los modelos utilizando RMSE y R² en entrenamiento y prueba.
   - Comparación del desempeño de los distintos modelos.

3. **Optimización de hiperparámetros**:
   - Variación de hiperparámetros para los algoritmos de Gradient Descent.
   - Optimización de Ridge, Lasso y Elastic Net mediante `GridSearchCV`.
   - Comparación de los mejores hiperparámetros y su impacto en el rendimiento de los modelos.
  
4. **Conclusiones**:
   - Comparación final de todos los modelos implementados.
   - Análisis de los resultados obtenidos y conclusiones del trabajo.


## Estado del trabajo

| Consigna | Estado |
|---|---|
| 3. Análisis descriptivo | *Completa* |
| 4. Regresión lineal múltiple | *Completa* |
| 5. Optimización de hiperparámetros | *Completa*|
| 6. Comparación de modelos | *Completa* |
| 7. Conclusión | *Completa* |

## Cómo ejecutar

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/<usuario>/TP_AA1_Apellido1_Apellido2_Apellido3.git
   ```
2. Instalar las dependencias:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn jupyter
   ```
3. Abrir `TP-regresion-AA1.ipynb` con Jupyter o Google Colab y ejecutar las celdas en orden.

## Herramientas utilizadas

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Observaciones

Este trabajo fue desarrollado como parte de la materia Aprendizaje Automático 1 de la Tecnicatura Universitaria en Inteligencia Artificial (FCEIA – UNR) durante el segundo cuatrimestre de 2026.
