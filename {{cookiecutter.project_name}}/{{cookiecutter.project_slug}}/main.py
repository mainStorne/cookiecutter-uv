{% if cookiecutter.serverless == 'Functions' %}
from fastapi import FastAPI
from mangum.handlers.api_gateway import HTTPGateway
from mangum import Mangum
from src import api

app = FastAPI(root_path="{{cookiecutter.root_path}}")
app.include_router(api)

handler = Mangum(app, custom_handlers=[HTTPGateway], api_gateway_base_path="{{cookiecutter.root_path}}")

if __name__ == '__main__':
  import uvicorn
  uvicorn.run('__main__:app', host='0.0.0.0', port=8000, reload=True)
{% else %}
from fastapi import FastAPI
from src import api
import uvicorn

app = FastAPI(root_path="{{cookiecutter.root_path}}")
app.include_router(api)

if __name__ == '__main__':
  uvicorn.run('__main__:app', host='0.0.0.0', port=8000, reload=True)
{% endif %}