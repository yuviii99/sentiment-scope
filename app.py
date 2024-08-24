from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import joblib

app = FastAPI()

# Load the model and vectorizer once when the app starts
vectorizer = joblib.load('vectorizer.joblib')
model = joblib.load('model.pkl')

@app.get('/predict/')
async def query_predict(query: str):
    try:
        # Convert query to vectorised data
        query_vector = vectorizer.transform([query])
        prediction = model.predict(query_vector)
        sentiments = ['negative', 'neutral', 'positive']
        return {"sentiment": sentiments[prediction[0] + 1]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get('/')
async def docs_redirect():
    return RedirectResponse(url='/docs')
