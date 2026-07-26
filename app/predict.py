import numpy as np
from app.model_loader import model

def predict_price(data):

    features = np.array([[
        data.avg_area_income,
        data.avg_area_house_age,
        data.avg_area_number_of_rooms,
        data.avg_area_number_of_bedrooms,
        data.area_population
    ]])

    prediction = model.predict(features)

    return float(prediction[0])