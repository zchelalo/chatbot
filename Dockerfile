FROM python:3.9-slim

# Configura variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Instala las dependencias de tu proyecto FastAPI
COPY requirements.txt .
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"
RUN pip install -r requirements.txt
RUN pip install pydantic==2.4.2

# Copia los archivos de tu proyecto FastAPI
COPY . .

# Exponer puertos para FastAPI y Rasa
EXPOSE 8000
EXPOSE 5005

# Comando para iniciar tanto FastAPI como el servidor de Rasa
CMD ["bash", "-c", "python src/main.py & rasa run -m models --enable-api --cors *"]