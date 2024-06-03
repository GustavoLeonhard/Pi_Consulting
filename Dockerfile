# Usamos una imagen oficial de Python como base
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /star_wars

# Copiamos el archivo de requisitos al directorio de trabajo
COPY requirements.txt .

# Instalamos las dependencias especificadas en el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el contenido del proyecto al directorio de trabajo dentro del contenedor
COPY star_wars .

# Exponemos el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]