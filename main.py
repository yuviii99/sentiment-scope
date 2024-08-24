from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import joblib

app = FastAPI()

@app.get('/')
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response