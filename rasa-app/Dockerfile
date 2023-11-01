# Utiliza una imagen base que incluye Python
FROM python:3.9-slim

# Configura variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el código de la aplicación de Rasa
COPY . .

# Exponer el puerto para la API de Rasa
EXPOSE 5005

# Comando para iniciar la aplicación de Rasa
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*"]