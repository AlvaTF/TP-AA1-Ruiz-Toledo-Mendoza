FROM python:3.14-slim

WORKDIR /app

# Primero las dependencias, así Docker reutiliza esta capa si solo cambia el código
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Script de inferencia, preprocesamiento (imputers y scalers) y modelo entrenado
COPY inferencia.py preprocesamiento.joblib modelo.keras ./
# Sin GPU: se ocultan los mensajes informativos de TensorFlow
ENV CUDA_VISIBLE_DEVICES=-1 TF_CPP_MIN_LOG_LEVEL=3

ENTRYPOINT ["python", "inferencia.py"]
