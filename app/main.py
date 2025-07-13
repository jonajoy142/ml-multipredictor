from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("app/model.joblib")

# FastAPI app
app = FastAPI()

# Input schema
class HouseFeatures(BaseModel):
    OverallQual: int
    GrLivArea: int
    GarageCars: int
    TotalBsmtSF: int

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "House Price Predictor is running!"}

# Prediction endpoint
@app.post("house_price/predict")
def predict_price(features: HouseFeatures):
    X = np.array([[features.OverallQual, features.GrLivArea, features.GarageCars, features.TotalBsmtSF]])
    prediction = model.predict(X)[0]
    return {"predicted_price": round(prediction, 2)}
