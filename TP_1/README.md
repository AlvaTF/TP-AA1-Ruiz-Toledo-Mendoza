# Trabajo Práctico de **Aprendizaje Automático 1**: 
## *Predicción de precios de casas*
### Tecnicatura Universitaria en Inteligencia Artificial – FCEIA, Universidad Nacional de Rosario
#### Segundo cuatrimestre 2026

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
├── README.md                # Este archivo
├── TP-regresion-AA1.ipynb   # Notebook de trabajo con todo el desarrollo
└── house-prices.csv         # Dataset utilizado
```

## Contenido del notebook

1. **Análisis descriptivo**: características y rango de cada variable, tratamiento de datos faltantes, visualizaciones (histogramas, scatterplots, boxplots), matriz de correlación, división train/test y escalado de datos.
2. **Regresión lineal múltiple**:
   - `LinearRegression`
   - Gradiente descendente, con gráficas de error vs. iteraciones
   - Regularización: Lasso, Ridge y Elastic Net
   - Métricas de evaluación en entrenamiento y prueba, y análisis del ajuste (fitting)
3. **Optimización de hiperparámetros** *(en progreso)*: variación de hiperparámetros de gradiente descendente, Lasso y Ridge.

## Estado del trabajo

| Consigna | Estado |
|---|---|
| 3. Análisis descriptivo | *Completa* |
| 4. Regresión lineal múltiple | *Completa* |
| 5. Optimización de hiperparámetros | 🟡 Incompleta |
| 6. Comparación de modelos | Pendiente |
| 7. Conclusión | Pendiente |

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
