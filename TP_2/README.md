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
AA1-TUIA-Ruiz-Toledo-Mendoza/
├── TP_2/
│   ├── README.md
│   ├── TP-clasificacion-AA1.ipynb
│   ├── 2026C2 - TrabajoPrácticoClasificacionAA1.pdf
│   ├── weatherAUS_2026C2.csv
│   ├── data_pycaret_train.csv
│   ├── data_pycaret_test.csv  
│   └── docker/
│       ├── inferencia.py
│       ├── requirements.txt
│       ├── preprocesamiento.joblib
│       ├── modelo.keras
│       ├── Dockerfile
│       ├── readme.md
│       └── ejemplo.csv
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
   - Implementación del modelo utilizando LogisticRegression.
   - Evaluación mediante Accuracy, Precision, Recall, F1-score, Balanced Accuracy, ROC AUC y PR AUC.
   - Matriz de confusión y análisis de falsos positivos y falsos negativos.
   - Curva ROC y análisis del umbral de clasificación.
   - Evaluación del ajuste del modelo.

3. **Modelo base**
   - Implementación mediante DummyClassifier.
   - Comparación de métricas con la regresión logística.
   - Comparación de matrices de confusión.
   - Análisis del desempeño respecto de una estrategia basada en la clase mayoritaria.

4. **Optimización de hiperparámetros**
   - Búsqueda de hiperparámetros de la regresión logística con GridSearchCV (C, l1_ratio y solver), que explora todas las combinaciones porque el espacio es chico.
   - Validación cruzada con TimeSeriesSplit de 5 particiones, para respetar el orden temporal. Previamente se compararon KFold, StratifiedKFold y TimeSeriesSplit.
   - Métrica objetivo: ROC AUC, porque no depende del umbral y el dataset está desbalanceado.
   - Mejor configuración: regularización L1, C = 100, solver liblinear (ROC AUC de validación cruzada 0.8751). Sobre el conjunto de prueba las métricas son prácticamente idénticas a las del modelo inicial, por lo que la optimización no produjo una mejora.
     
5. **Explicabilidad**
   - Explicabilidad con SHAP (LinearExplainer) sobre la regresión logística.
   - Dos gráficos globales (importancia media y beeswarm) y dos locales (un día con lluvia y un día seco).
   - Variables más importantes: Pressure3pm, Humidity3pm, Pressure9am, WindGustSpeed y Sunshine. Menos importantes: MinTemp, MaxTemp, Cloud9am, Evaporation y las componentes de la dirección del viento.
   - Interpretación meteorológica: una caída de la presión durante el día y una humedad alta por la tarde aumentan la probabilidad de lluvia, y más horas de sol la disminuyen.


6. **AutoML**
   - Se utilizó PyCaret (compare_models) en un entorno aparte con Python 3.11, porque PyCaret no es compatible con la versión 3.14 del resto del trabajo. Los datos ya procesados se guardaron en data_pycaret_train.csv y data_pycaret_test.csv.
   - Configuración: sin preprocesamiento propio, mismo conjunto de prueba, validación cruzada temporal de 5 particiones, métrica de orden AUC y session_id = 42. No se fijó límite de tiempo.
   - Mejor modelo: Random Forest, con hiperparámetros por defecto (ROC AUC de validación cruzada 0.8817, igual que Extra Trees). En el conjunto de prueba obtuvo un ROC AUC de 0.8764, contra 0.863 de la regresión logística.
   - Comparación con la regresión logística: mejora levemente la precisión y no el recall, entrena más lento (Gradient Boosting tardó unos 10.5 s por partición contra 4.6 s de la regresión logística) y es menos interpretable.
   
7. **Red neuronal**
   - Red multicapa en Keras con dos capas ocultas (32 y 16 neuronas, ReLU) y salida sigmoide, entrenada con binary_crossentropy y Adam, con Early Stopping sobre la pérdida de validación.
   - Validación: último 15% del conjunto de entrenamiento (en orden temporal). No se usó validación cruzada por su costo computacional.
   - Optimización con Optuna (5 pruebas): cantidad de neuronas, dropout y learning rate. Mejor configuración: 64 neuronas, sin dropout y learning rate 0.001.
   - Resultados en test (ROC AUC): red base 0.8782 y red optimizada 0.8796, contra 0.863 de la regresión logística.
   - Explicabilidad con SHAP (GradientExplainer): gráficos globales y locales, con una comparación con la regresión logística.
   
8. **Comparación de modelos**
   - Métrica elegida: ROC AUC, porque no depende del umbral de 0.5, que no es el adecuado para este problema.
   - La red neuronal optimizada obtiene el mayor valor (0.8796), seguida por la red base (0.8782) y el Random Forest de PyCaret (0.8764). Las diferencias entre ellos son menores a 0.004, por lo que su desempeño es equivalente. Los tres superan a la regresión logística (0.863).
   - Se elige la red neuronal optimizada como modelo final.

9. **MLOps**
   - Se guardan en la carpeta docker/ el modelo (modelo.keras), los objetos de preprocesamiento (preprocesamiento.joblib), el script inferencia.py, el Dockerfile y un archivo de ejemplo.
   - El script recibe un CSV con las columnas originales del dataset y devuelve la probabilidad de lluvia y la clase predicha (umbral 0.5).
   - Instrucciones para construir la imagen y ejecutar el contenedor: ver docker/readme.md.
   - 
10. **Conclusiones**
   - Todos los modelos superan ampliamente al modelo base. Los modelos no lineales (red neuronal y Random Forest) mejoran levemente a la regresión logística.
   - Con el umbral de 0.5 todos los modelos detectan solo alrededor de la mitad de los días con lluvia.
   - El modelo final se puso en producción con Docker. El detalle está en la conclusión del notebook.

## Estado del trabajo

| Consigna | Estado |
|---|---|
| 1. Análisis descriptivo | *Completa* |
| 2. Regresión logística | *Completa* |
| 3. Modelo base | *Completa* |
| 4. Optimización de hiperparámetros | *Completa* |
| 5. Explicabilidad | *Completa* |
| 6. AutoML | *Completa* |
| 7. Red neuronal | *Completa* |
| 8. Comparación de modelos | *Completa* |
| 9. MLOps | *Completa* |
| 10. Conclusión | *Completa* |

## Cómo ejecutar

1. Clonar el repositorio:

```bash
git clone https://github.com/<usuario>/TP-AA1-Ruiz-Toledo-Mendoza.git
```

2. Instalar las dependencias:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn shap optuna tensorflow joblib jupyter
```

3. Abrir `TP-clasificacion-AA1.ipynb` con Jupyter Notebook o Google Colab y ejecutar las celdas en orden.

- El notebook se ejecutó con Python 3.14. La sección de PyCaret (ítem 6) se ejecutó aparte con Python 3.11 (pip install pycaret), usando los archivos data_pycaret_train.csv y data_pycaret_test.csv.
- El KNN de la imputación y la búsqueda con Optuna tardan varios minutos.
- El dataset weatherAUS_2026C2.csv debe estar en la misma carpeta que el notebook.

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
