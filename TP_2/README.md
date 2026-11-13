# Trabajo Práctico de **Aprendizaje Automático 1**:
## *Predicción de lluvia en Australia*
### Tecnicatura Universitaria en Inteligencia Artificial – FCEIA, Universidad Nacional de Rosario

## Integrantes

| Apellido y nombre | Usuario de GitHub |
|---|---|
| Mendoza, Emmanuel | @emmamz1 |
| Ruiz, Irma Carolina | @CaroRuiz92 |
| Toledo, Alvaro | @AlvaTF |

## Propósito

Este repositorio contiene la resolución del trabajo práctico de clasificación de la materia. El objetivo consiste en predecir si **lloverá al día siguiente** (`RainTomorrow`) a partir de variables meteorológicas registradas en distintas ciudades de Australia, utilizando técnicas de clasificación supervisada y herramientas de aprendizaje automático.

## Estructura del repositorio

```text
TP-AA1-Ruiz-Toledo-Mendoza/
├── TP_2/
│   ├── README.md                           # Este archivo
│   ├── TP-clasificacion-AA1.ipynb          # Notebook con el desarrollo
│   ├── 2026C2 - TrabajoPrácticoClasificacionAA1.pdf # Consigna
│   └── weatherAUS_2026C2.csv               # Dataset utilizado
```

## Contenido del notebook

1. **Análisis descriptivo**
   - Exploración inicial del dataset.
   - Tratamiento de valores faltantes.
   - Análisis estadístico descriptivo.
   - Visualizaciones (histogramas, boxplots, matriz de correlación, etc.).
   - Codificación de variables categóricas.
   - Escalado de variables.
   - División del conjunto de datos en entrenamiento y prueba.

2. **Regresión logística**
   - Implementación del modelo utilizando `LogisticRegression`.
   - Evaluación mediante Accuracy, Precision, Recall, F1-score, Balanced Accuracy, ROC AUC y PR AUC.
   - Matriz de confusión y análisis de falsos positivos y falsos negativos.
   - Curva ROC y análisis del umbral de clasificación.
   - Evaluación del ajuste del modelo.

3. **Modelo base**
   - Implementación mediante `DummyClassifier`.
   - Comparación de métricas con la regresión logística.
   - Comparación de matrices de confusión.
   - Análisis del desempeño respecto de una estrategia basada en la clase mayoritaria.

4. **Optimización de hiperparámetros**
   - Definición del espacio de búsqueda de hiperparámetros de la regresión logística (`C`, `penalty`, `solver`, `class_weight`).
   - Búsqueda mediante [Optuna / GridSearchCV / RandomizedSearchCV] con validación cruzada estratificada.
   - Métrica objetivo utilizada: [F1-score / ROC AUC / Balanced Accuracy], justificada por el desbalance de clases.
   - Evaluación del modelo optimizado sobre el conjunto de prueba y comparación con la regresión logística inicial y con el modelo base.
   - Análisis del impacto de la optimización sobre las métricas y la matriz de confusión.

5. **Explicabilidad**
   - Análisis de los coeficientes de la regresión logística (signo y magnitud) para identificar las variables más influyentes.
   - Importancia de variables mediante [SHAP / permutation importance].
   - Explicaciones globales (variables que más pesan en el modelo) y locales (explicación de predicciones individuales) mediante [SHAP / LIME].
   - Interpretación de los resultados desde el punto de vista meteorológico (por ejemplo, rol de `Humidity3pm`, `Pressure3pm`, `Sunshine`, `Rainfall`).


6. **AutoML**
   - Aplicación de [FLAML / TPOT / PyCaret / auto-sklearn] para la búsqueda automática de modelos y preprocesamiento.
   - Configuración utilizada: métrica objetivo, tiempo máximo de búsqueda y estrategia de validación.
   - Identificación del mejor modelo encontrado y sus hiperparámetros.
   - Evaluación sobre el conjunto de prueba con las mismas métricas que los modelos anteriores.
   - Comparación con la regresión logística optimizada: ventajas, desventajas, costo computacional e interpretabilidad.

7. **Red neuronal**
   - *Pendiente.*

8. **Comparación de modelos**
   - *Pendiente.*

9. **MLOps**
   - *Pendiente.*

10. **Conclusiones**
    - *Pendiente.*

## Estado del trabajo

| Consigna | Estado |
|---|---|
| 1. Análisis descriptivo | *Completa* |
| 2. Regresión logística | *Completa* |
| 3. Modelo base | *Completa* |
| 4. Optimización de hiperparámetros | *Pendiente* |
| 5. Explicabilidad | *Pendiente* |
| 6. AutoML | *Pendiente* |
| 7. Red neuronal | *Pendiente* |
| 8. Comparación de modelos | *Pendiente* |
| 9. MLOps | *Pendiente* |
| 10. Conclusión | *Pendiente* |

## Cómo ejecutar

1. Clonar el repositorio:

```bash
git clone https://github.com/<usuario>/TP-AA1-Ruiz-Toledo-Mendoza.git
```

2. Instalar las dependencias:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

3. Abrir `TP-clasificacion-AA1.ipynb` con Jupyter Notebook o Google Colab y ejecutar las celdas en orden.

## Herramientas utilizadas

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Observaciones

Este trabajo fue desarrollado como parte de la materia **Aprendizaje Automático 1** de la Tecnicatura Universitaria en Inteligencia Artificial (FCEIA – Universidad Nacional de Rosario) durante el segundo cuatrimestre de 2026.
