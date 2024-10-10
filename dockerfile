FROM python:3.10

WORKDIR /linkscribe

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && python3 -m spacy download en_core_web_md

CMD ["fastapi", "run", "app/main.py"]
