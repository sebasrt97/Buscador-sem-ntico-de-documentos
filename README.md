# Uso
## Ejecuta el Script:

# Bash

```
python chroma.py
```
## Accede a la Interfaz: Se abrirá una URL local (por defecto http://127.0.0.1:7860).

* Pestaña "Carga de Archivos":

Sube uno o varios archivos JSON.

Haz clic en "Cargar Documentos a ChromaDB".

Verifica el resumen en el Estado de la Operación.

* Pestaña "Consulta Semántica":

Introduce tu pregunta en el campo "Tu Pregunta/Consulta".

Haz clic en "Buscar Documento".

El resultado mostrará el fragmento de texto más relevante encontrado, su archivo fuente y la puntuación de distancia.

* Enviorement necesarios:

```
pip install gradio
pip install chromadb
```

## Docker

Se creo el archivo requirements.txt donde iria gradio y chromadb

Se creo DockerFile para la creacion de la imagen 

Pasos: 

docker build -t app .

docker run -d -p 7860:7860 --name app(se asgina el nombre del contenedor) app 

Tambien hubo que cambiar el script con "app.launch(server_name="0.0.0.0", server_port=7860)"