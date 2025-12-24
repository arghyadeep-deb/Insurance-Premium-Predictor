from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import InsuranceData
from schema.pred_response import PredictionResponse
from model.predict import predict_output, MODEL_VERSION, model
import numpy as np
import pandas as pd

app=FastAPI()
        
#human readable endpoints
@app.get('/')
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

#health check endpoint(machine readable)
@app.get('/health')
def health_check():
    return {"status": "API is healthy",
            "model_version": MODEL_VERSION,
            "model_loaded": model is not None}

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: InsuranceData):
    user_input={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'income_lpa': data.income_lpa,
        'city_tier': data.city_tier,
        'occupation': data.occupation
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(content={"response": prediction})
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)