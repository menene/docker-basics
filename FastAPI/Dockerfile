# Usa la imagen oficial de Python para FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY ./requirements.txt .
COPY ./main.py .

# Instala las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto en el que FastAPI escucha
EXPOSE 80

# Comando por defecto para ejecutar la aplicación usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
