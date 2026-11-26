# Predicción de lluvia en Australia: inferencia con Docker

Esta carpeta contiene lo necesario para predecir si lloverá al día siguiente (`RainTomorrow`) con la red neuronal optimizada del trabajo práctico.

## Contenido

| Archivo | Descripción |
|---|---|
| `inferencia.py` | Script que preprocesa los datos nuevos y genera las predicciones |
| `requirements.txt` | Librerías necesarias para la inferencia, con las mismas versiones usadas en el entrenamiento |
| `preprocesamiento.joblib` | Imputers KNN y scalers por estado, scaler final, mapeos (estado, dirección del viento, coordenadas) y orden de columnas |
| `modelo.keras` | Red neuronal optimizada, entrenada en el notebook |
| `Dockerfile` | Instrucciones para construir la imagen |
| `ejemplo.csv` | Archivo de ejemplo con 10 días para probar la inferencia |

Los archivos `preprocesamiento.joblib`, `modelo.keras`, `requirements.txt` y `ejemplo.csv` se generan desde el notebook (ítem 9). El modelo no se entrena dentro del contenedor: la imagen solo hace inferencia.

## Requisitos

Tener instalado Docker (por ejemplo, Docker Desktop) y que esté en ejecución.

## 1. Construir la imagen

Desde esta carpeta (`docker`):

```bash
docker build -t lluvia-australia:v1 .
```

La primera vez tarda varios minutos, porque instala TensorFlow.

## 2. Ejecutar el contenedor

El contenedor recibe dos argumentos: el archivo de entrada y el archivo de salida. Los archivos se comparten con el contenedor montando la carpeta actual en `/datos`.

**Linux, macOS o Git Bash:**

```bash
docker run --rm -v "$(pwd):/datos" lluvia-australia:v1 /datos/ejemplo.csv /datos/predicciones.csv
```

**Windows (PowerShell):**

```powershell
docker run --rm -v "${PWD}:/datos" lluvia-australia:v1 /datos/ejemplo.csv /datos/predicciones.csv
```

**Windows (CMD):**

```cmd
docker run --rm -v "%cd%:/datos" lluvia-australia:v1 /datos/ejemplo.csv /datos/predicciones.csv
```

Al terminar, el archivo `predicciones.csv` queda en la carpeta actual.

Para predecir otros datos, se copia el archivo CSV en esta carpeta y se cambia `ejemplo.csv` por su nombre. No hace falta volver a construir la imagen.

## Formato de los datos

**Entrada:** un CSV con las columnas originales del dataset `weatherAUS`, una fila por día y estación:

`Date, Location, MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustDir, WindGustSpeed, WindDir9am, WindDir3pm, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm, Temp9am, Temp3pm, RainToday`

- Puede tener valores faltantes: se imputan con los mismos imputers KNN por estado que se ajustaron en el entrenamiento.
- Si falta `RainToday`, se deduce de `Rainfall` (`Yes` si se registraron más de 1 mm).
- `Location` debe ser una de las 49 estaciones del dataset original. Si aparece otra, el script termina con un mensaje de error.
- Si el archivo tiene otras columnas (por ejemplo `RainTomorrow`), se ignoran para la predicción y se conservan en la salida.

**Salida:** el mismo CSV con dos columnas nuevas:

- `Prob_lluvia`: probabilidad predicha de que llueva al día siguiente.
- `RainTomorrow_pred`: `Yes` si la probabilidad es mayor o igual a 0.5, `No` si es menor.

## Cuándo hay que volver a construir la imagen

- Si se reentrena el modelo (nuevos `modelo.keras` o `preprocesamiento.joblib`).
- Si se modifica `inferencia.py` o `requirements.txt`.

Para predecir datos nuevos no hace falta: alcanza con pasar otro archivo al ejecutar el contenedor.
