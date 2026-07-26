# 🏠 House Price Prediction System

A Machine Learning web application that predicts house prices using **Linear Regression**. The project is built with **FastAPI** for the backend and **Streamlit** for the frontend, allowing users to enter house details and receive instant price predictions.

---

## 🚀 Live Demo

### 🌐 Streamlit Frontend
https://house-price-prediction-4eguec7txdweba2n2gbfwy.streamlit.app/

### ⚡ FastAPI Backend
https://house-price-prediction-t7vc.onrender.com

### 📖 API Documentation (Swagger)
https://house-price-prediction-t7vc.onrender.com/docs

---

## 📌 Features

- Predict house prices using Machine Learning
- Interactive Streamlit user interface
- FastAPI REST API backend
- Automatic API documentation with Swagger
- Model performance metrics
- Trained model saved using Joblib
- Deployment on Render and Streamlit Community Cloud

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### Machine Learning
- Scikit-learn
- Linear Regression
- Pandas
- NumPy
- Joblib

### Visualization
- Matplotlib
- Seaborn

### Deployment
- Render
- Streamlit Community Cloud
- GitHub

---

## 📂 Project Structure

```
house-price-prediction/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model_loader.py
│   ├── predict.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── ml/
│   ├── train_model.ipynb
│   ├── model.pkl
│   ├── metrics.json
│   └── columns.pkl
│
├── dataset/
│   └── 01-USA_Housing.csv
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

Dataset: USA Housing Dataset

Features

- Avg. Area Income
- Avg. Area House Age
- Avg. Area Number of Rooms
- Avg. Area Number of Bedrooms
- Area Population

Target

- House Price

---

## 📈 Model Performance

| Metric | Value |
|---------|-------|
| MAE | 82,288.22 |
| MSE | 10,460,958,907.21 |
| RMSE | 102,278.83 |
| R² Score | 0.918 |

---

## 🧠 Machine Learning Workflow

```
Dataset
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Feature Selection
    │
    ▼
Train-Test Split
    │
    ▼
Linear Regression Model
    │
    ▼
Model Evaluation
    │
    ▼
Save model.pkl
    │
    ▼
FastAPI API
    │
    ▼
Streamlit Frontend
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/house-price-prediction.git
```

```bash
cd house-price-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Train the Model

```bash
python ml/train_model.py
```

or run

```
train_model.ipynb
```

---

## ▶ Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## ▶ Run Streamlit

```bash
streamlit run frontend/app.py
```

---

## 📡 API Endpoints

### Home

```
GET /
```

### Predict House Price

```
POST /predict
```

Sample Request

```json
{
  "avg_area_income": 79545.45,
  "avg_area_house_age": 5.68,
  "avg_area_number_of_rooms": 7.00,
  "avg_area_number_of_bedrooms": 4.09,
  "area_population": 23086.80
}
```

Sample Response

```json
{
  "Predicted Price": 1225941.57
}
```

---

### Model Metrics

```
GET /metrics
```

---

## 📸 Screenshots

### Streamlit Home

_Add screenshot here_

### Prediction Result

_Add screenshot here_

### Swagger API

_Add screenshot here_

---

## 🎯 Future Improvements

- Random Forest Regressor
- XGBoost Regressor
- CSV Upload Prediction
- Prediction History
- User Authentication
- Docker Support
- CI/CD Pipeline
- Cloud Database

---

## 👨‍💻 Author

**Mohd Faizy**

GitHub:
https://github.com/Faizyzaidi

LinkedIn:
(Add your LinkedIn profile)

---

## ⭐ If you found this project useful, please consider giving it a Star!