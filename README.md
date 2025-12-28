# Insurance Premium Predictor
A Machine Learning–based insurance premium prediction system built using **FastAPI** for the backend and **Streamlit** for the frontend.
The application predicts an insurance premium category based on user details such as age, BMI, income, lifestyle risk, city tier, and occupation.

## About the Project
This project demonstrates how a trained Machine Learning model can be deployed as a REST API and accessed through a simple web interface.  
It focuses on clean backend–frontend separation and real-world ML deployment practices.

## Features
- Insurance premium prediction using Machine Learning  
- FastAPI backend with request and response validation  
- Streamlit-based interactive frontend  
- API health-check endpoint  
- Clean and modular project structure  

## Tech Stack
- **Language:** Python  
- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **Machine Learning:** Scikit-learn  
- **Data Processing:** Pandas, NumPy  

## Project Structure
```
insurance-premium-predictor/
├── app.py          # FastAPI backend
├── frontend.py     # Streamlit frontend
├── insurance.csv   # Dataset
├── requirements.txt
├── README.md
└── model/          # Model and prediction logic
```
## How to Run the Project
### 1. Install dependencies
```
pip install -r requirements.txt
```
### 2. Start the FastAPI backend
```
uvicorn app:app --reload
```
Backend runs at:
```
http://127.0.0.1:8000
```
### 3. Run the Streamlit frontend
```
streamlit run frontend.py
```

## 🔗 API Endpoints
- `GET /` – Welcome endpoint  
- `GET /health` – API health check  
- `POST /predict` – Insurance premium prediction  

## Dataset
The dataset contains structured insurance-related features including demographic information, lifestyle risk indicators, income level, city tier, and occupation category.

## Purpose
This project is intended for learning and demonstrating:
- Machine Learning model deployment  
- API-based ML systems  
- End-to-end ML application development  
