from fastapi import FastAPI
from pydantic import BaseModel
from .model import Model
from .scrap_tool import ScrapTool
from .nlp_tool import NLPTool
from .response_data import ResponseData
from .response import Response

app = FastAPI()

class UrlRequest(BaseModel):
  url: str


@app.post("/classificate")
async def classificate(url_request: UrlRequest):
  response_data = ResponseData()
  response = Response()
  scrap_tool = ScrapTool()
  nlp_tool = NLPTool()
  model = Model()
  try:
    df = model.eda('data/dataset.csv')
    trained_model, fitted_vectorizer = model.train(df)

    website_url = url_request.url
    web = dict(scrap_tool.scrap(website_url))
    if web:
      text = nlp_tool.clean_text(web["content"])
      t = fitted_vectorizer.transform([text])
      prediction = trained_model.predict(t)
      response.status = 200
      response.message = 'OK'
      response.data = response_data
      response_data.title = web['title']
      response_data.description = web['description']
      response_data.preview_link = web['preview']
      response_data.category_int = int(prediction[0])
      response_data.category_str = df['Category'].unique()[prediction[0]]
  except Exception as e:
    response.status = 500
    response.message = str(e)
    response.data = None
    print(e)
  finally:
    return response.to_dict()
