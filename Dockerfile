# 1. Imagen base
FROM python:3.11-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# 3. Copiar y instalar las dependencias
# Esto asegura que el entorno de ChromaDB y Gradio esté listo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el código de la aplicación (el script)
COPY . .

# 5. Exponer el puerto de la aplicación Gradio
# Gradio usa el puerto 7860 por defecto
EXPOSE 7860

# 6. Comando para iniciar el script
# Asegúrate de que "mi_script.py" sea el nombre de tu archivo.
CMD [ "python", "chroma.py" ]