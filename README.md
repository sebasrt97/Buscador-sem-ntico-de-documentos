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