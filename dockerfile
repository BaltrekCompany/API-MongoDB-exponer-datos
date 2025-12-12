# Usamos una imagen ligera de Python
FROM python:3.11-slim

WORKDIR /app

# Copiamos requirements primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Exponemos el puerto 5050 (para mantener la compatibilidad con tu docker-compose)
EXPOSE 5050

# Comando para iniciar FastAPI
# host 0.0.0.0 permite que se vea desde fuera del contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]