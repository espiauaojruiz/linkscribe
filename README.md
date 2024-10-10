## Linkscribe

Este proyecto clasifica sitios web basándose en su contenido textual. Utiliza FastAPI para crear una API RESTful, NLP y Webscraping.

### Requisitos

- Python 3.8+
- Instala las dependencias con `pip install -r requirements.txt`
- Instala el modelo de NLP en-core-web-lg `python -m spacy download en_core_web_md`

### Uso

Para ejecutar el servidor, desde el diractorio raiz de la aplicación ejecuta `fastapi run app/main.py`