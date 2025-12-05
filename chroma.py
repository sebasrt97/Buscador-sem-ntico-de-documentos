import gradio as gr
import chromadb
import uuid
import json
import os
from typing import List, Dict, Any

## Usar prueba 2

# 1. Configuración de ChromaDB
chroma_client = chromadb.Client()
COLLECTION_NAME = "documentos"
collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME)

# 2. Funciones Lógicas Esenciales
def cargar_documento(file_path):
    """Carga un archivo JSON asumiendo que es válido."""
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Asume que el contenido relevante está en 'content'
    document_content = data.get('content', str(data))
    doc_id = str(uuid.uuid4())
    
    collection.add(
        documents=[document_content],
        metadatas=[{"file_name": os.path.basename(file_path)}],
        ids=[doc_id]
    )
    return f"Cargado: {os.path.basename(file_path)}"

def subir_multiples_archivos_simple(file_list):
    """Itera y carga. Devuelve el resultado del último archivo."""
    # Eliminamos la verificación 'if not file_list:'
    for f in file_list:
        resultado = cargar_documento(f.name)
    return resultado

def realizar_consulta_simple(query):
    """Busca el documento más relevante sin verificación de existencia de documentos."""
    
    results = collection.query(
        query_texts=[query],
        n_results=1,
        include=['documents', 'metadatas']
    )
    
    # Asume que siempre habrá un resultado (aunque sea vacío)
    documento = results['documents'][0][0]
    file_name = results['metadatas'][0][0]['file_name']
    
    return f"Fuente: {file_name}\nContenido:\n{documento}"

# 3. Definición de la Interfaz Gradio
with gr.Blocks() as tab_carga:
    file_uploader = gr.File(label="JSONs", file_count="multiple", file_types=[".json"])
    btn_cargar = gr.Button("Cargar")
    output_carga = gr.Textbox(label="Estado")
    
    btn_cargar.click(
        fn=subir_multiples_archivos_simple,
        inputs=file_uploader,
        outputs=output_carga
    )

with gr.Blocks() as tab_consulta:
    input_query = gr.Textbox(label="Pregunta")
    btn_consultar = gr.Button("Buscar")
    output_documento = gr.Textbox(label="Resultado", lines=10)
    
    btn_consultar.click(
        fn=realizar_consulta_simple,
        inputs=input_query,
        outputs=output_documento
    )

app = gr.TabbedInterface(
    [tab_carga, tab_consulta], 
    ["Carga", "Consulta"]
)

if __name__ == "__main__":
    app.launch()