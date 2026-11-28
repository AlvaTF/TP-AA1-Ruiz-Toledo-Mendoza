"""
Inferencia del modelo de predicción de lluvia (RainTomorrow).

Uso:
    python inferencia.py <archivo_entrada.csv> <archivo_salida.csv>

El archivo de entrada debe tener las columnas originales del dataset weatherAUS
(Date, Location, MinTemp, ..., RainToday), una fila por día y estación.
Puede tener valores faltantes: se imputan igual que en el entrenamiento.

El archivo de salida tiene las mismas columnas de entrada y dos columnas nuevas:
    - Prob_lluvia: probabilidad predicha de que llueva al día siguiente
    - RainTomorrow_pred: "Yes" si la probabilidad es mayor o igual al umbral, "No" si no
"""

import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

CARPETA = Path(__file__).resolve().parent
ARCHIVO_PREPROCESAMIENTO = CARPETA / "preprocesamiento.joblib"
ARCHIVO_MODELO = CARPETA / "modelo.keras"

UMBRAL = 0.5

COLUMNAS_REQUERIDAS = [
    "Date", "Location", "MinTemp", "MaxTemp", "Rainfall", "Evaporation", "Sunshine",
    "WindGustDir", "WindGustSpeed", "WindDir9am", "WindDir3pm", "WindSpeed9am",
    "WindSpeed3pm", "Humidity9am", "Humidity3pm", "Pressure9am", "Pressure3pm",
    "Cloud9am", "Cloud3pm", "Temp9am", "Temp3pm", "RainToday",
]


def validar_entrada(df, prep):
    """Verifica que estén todas las columnas y que las ubicaciones sean conocidas."""
    faltantes = [c for c in COLUMNAS_REQUERIDAS if c not in df.columns]
    if faltantes:
        sys.exit(f"Error: faltan columnas en el archivo de entrada: {faltantes}")

    desconocidas = sorted(set(df["Location"]) - set(prep["state_map"]))
    if desconocidas:
        sys.exit(f"Error: ubicaciones que el modelo no conoce: {desconocidas}")


def preprocesar(df_crudo, prep):
    """Aplica a los datos nuevos los mismos pasos que se aplicaron en el notebook."""
    df = df_crudo.copy()

    columnas_knn = prep["columnas_knn"]
    columnas_log = prep["columnas_log"]
    num_cols = prep["num_cols"]

    # Mes en forma cíclica
    mes = pd.to_datetime(df["Date"]).dt.month
    df["Mes_sin"] = np.sin(2 * np.pi * mes / 12)
    df["Mes_cos"] = np.cos(2 * np.pi * mes / 12)

    # Dirección del viento en forma cíclica (seno y coseno del ángulo)
    for col in ["WindGustDir", "WindDir9am", "WindDir3pm"]:
        angulos = df[col].map(prep["wind_map"])
        df[f"{col}_sin"] = np.sin(np.deg2rad(angulos))
        df[f"{col}_cos"] = np.cos(np.deg2rad(angulos))

    # Cloud = 9 significa cielo no visible: se trata como faltante
    df[["Cloud9am", "Cloud3pm"]] = df[["Cloud9am", "Cloud3pm"]].replace(9, np.nan)

    # Imputación KNN por estado, con los scalers e imputers ajustados en train
    df["State"] = df["Location"].map(prep["state_map"])
    df[columnas_knn] = df[columnas_knn].astype(float)
    datos_knn = df[columnas_knn].copy()
    datos_knn[columnas_log] = np.log1p(datos_knn[columnas_log])

    for state in df["State"].unique():
        mask = df["State"] == state
        scaler = prep["scalers"][state]
        imputer = prep["imputers"][state]

        escalado = scaler.transform(datos_knn.loc[mask, columnas_knn])
        imputado = imputer.transform(escalado)
        imputado = pd.DataFrame(scaler.inverse_transform(imputado),
                                columns=columnas_knn, index=datos_knn.index[mask])
        imputado[columnas_log] = np.expm1(imputado[columnas_log])

        # Solo se completan los valores faltantes
        df.loc[mask, columnas_knn] = df.loc[mask, columnas_knn].fillna(imputado)

    # RainToday: si falta, se deduce de Rainfall (llueve si se registró más de 1 mm)
    rain_today = df["RainToday"].map({"Yes": 1, "No": 0})
    df["RainToday"] = rain_today.fillna((df["Rainfall"] > 1).astype(int))

    # Coordenadas de la ubicación
    df["Lat"] = df["Location"].map(lambda x: prep["location_coords"][x][0])
    df["Lon"] = df["Location"].map(lambda x: prep["location_coords"][x][1])

    # Mismo orden de columnas que en el entrenamiento
    X = df[prep["columnas_modelo"]].copy()

    # Transformación logarítmica y estandarización final
    X[columnas_log] = np.log1p(X[columnas_log])
    X[num_cols] = prep["scaler_final"].transform(X[num_cols])

    return X.astype("float32")


def main():
    if len(sys.argv) != 3:
        sys.exit("Uso: python inferencia.py <archivo_entrada.csv> <archivo_salida.csv>")

    entrada, salida = sys.argv[1], sys.argv[2]

    from tensorflow import keras

    prep = joblib.load(ARCHIVO_PREPROCESAMIENTO)
    modelo = keras.models.load_model(ARCHIVO_MODELO)

    datos = pd.read_csv(entrada)
    validar_entrada(datos, prep)

    X = preprocesar(datos, prep)
    probabilidades = modelo.predict(X.values, verbose=0).ravel()

    datos["Prob_lluvia"] = probabilidades.round(4)
    datos["RainTomorrow_pred"] = np.where(probabilidades >= UMBRAL, "Yes", "No")
    datos.to_csv(salida, index=False)

    print(f"Predicciones guardadas en {salida}")
    print(f"Filas procesadas: {len(datos)}")
    print(f"Días con lluvia predicha: {(datos['RainTomorrow_pred'] == 'Yes').sum()}")


if __name__ == "__main__":
    main()
