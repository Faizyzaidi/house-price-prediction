from fastapi import FastAPI
from app.schemas import HouseData
from app.predict import predict_price
import json

app = FastAPI(
    title="House Price Prediction API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is Running"
    }

@app.get("/metrics")
def metrics():

    with open("ml/metrics.json") as f:
        return json.load(f)


@app.post("/predict")
def predict(data: HouseData):

    price = predict_price(data)

    return {
        "Predicted Price": round(price,2)
    }