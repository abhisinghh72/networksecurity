# 🚀 Network Security: Phishing Detection System

An end-to-end **Machine Learning + MLOps project** for detecting phishing websites, built with a production-ready pipeline and deployed on AWS using CI/CD.


## 📌 Overview

This project detects whether a given website is **phishing or legitimate** using a trained machine learning model.

It includes:
- Full ML pipeline (data → model → prediction)
- Experiment tracking with MLflow
- Cloud storage (AWS S3)
- Containerization (Docker)
- CI/CD automation (GitHub Actions)
- Deployment on AWS EC2
- REST API using FastAPI

---

## 🏗️ Project Architecture

```
Data → Pipeline → MLflow → S3 → Docker → ECR → GitHub Actions → EC2 → FastAPI API
```

---

## ⚙️ Tech Stack

### 👨‍💻 Backend & ML
- Python
- Scikit-learn
- Pandas
- NumPy

### 🚀 API
- FastAPI
- Uvicorn

### 📦 MLOps & Tracking
- MLflow
- DagsHub

### ☁️ Cloud & DevOps
- AWS S3
- AWS ECR
- AWS EC2
- Docker

### 🔄 CI/CD
- GitHub Actions
- Self-hosted Runner

---

## 📂 Project Structure

```
networksecurity/
│
├── components/           # Data ingestion, transformation, training
├── pipeline/             # Training & prediction pipelines
├── cloud/                # AWS S3 sync logic
├── utils/                # Helper utilities
├── entity/               # Config & artifact entities
├── exception/            # Custom exception handling
├── logging/              # Logging module
│
├── app.py                # FastAPI app
├── main.py               # Pipeline runner
├── requirements.txt
├── Dockerfile
└── .github/workflows     # CI/CD pipeline
```

---

## 🔬 Features

- Modular ML pipeline (production-ready structure)
- Automated training & prediction workflows
- Experiment tracking with MLflow + DagsHub
- Model & artifacts stored in AWS S3
- Dockerized application
- CI/CD pipeline using GitHub Actions
- Auto deployment on EC2
- FastAPI REST endpoints for real-time predictions

---

## 📡 API Endpoints

### Home  
GET /

### Train Model  
GET /train

### Predict  
POST /predict

---

## 🐳 Docker Setup

### Build Image
```
docker build -t networksecurity .
```

### Run Container
```
docker run -d -p 8080:8080 networksecurity
```

---

## ☁️ AWS Deployment Flow

1. Push code to GitHub  
2. GitHub Actions triggers CI/CD  
3. Docker image is built  
4. Image pushed to AWS ECR  
5. EC2 pulls latest image  
6. Container runs automatically  

---

## 🔄 CI/CD Pipeline

The pipeline includes:
- Code checkout  
- Build Docker image  
- Push to AWS ECR  
- Deploy to EC2  

---

## 📊 Experiment Tracking

- Integrated MLflow with DagsHub  
- Tracks:
  - Accuracy
  - Precision
  - Recall
  - F1-score  
- Enables comparison across multiple runs  

---

## 📦 Storage

- AWS S3 for:
  - Model artifacts  
  - Pipeline outputs  
  - Versioned storage  

---

## 🌐 Live API

```
http://13.217.93.214:8080/docs
```

Swagger UI for testing endpoints.

---

## 🚀 How to Run Locally

```
# Clone repo
git clone https://github.com/abhisinghh72/networksecurity.git

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
```

---

## 🎯 Use Cases

- Detect phishing URLs  
- Integrate into browser extensions  
- Security and fraud detection systems  

---

## 📈 Future Improvements

- Browser extension for real-time URL checking  
- Frontend dashboard  
- Advanced models (XGBoost, Deep Learning)  
- Real-time prediction system  

---

## 👤 Author

Abhishek Singh
