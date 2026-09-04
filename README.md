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
<img width="628" height="1599" alt="WhatsApp Image 2026-05-01 at 11 32 55" src="https://github.com/user-attachments/assets/acecb203-201b-4a34-a6b5-b36a69bd2128" />


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

<img width="2880" height="1708" alt="WhatsApp Image 2026-05-01 at 11 33 27" src="https://github.com/user-attachments/assets/ab9abdf7-08ce-4f62-bcf6-78ab040e6e14" />

---

## 🐳 Docker Setup

### Build Image
```
docker build -t networksecurity .
```
<img width="2880" height="1720" alt="WhatsApp Image 2026-05-01 at 11 33 27 (1)" src="https://github.com/user-attachments/assets/c45089f4-18f8-4a07-bc67-17c2909b8a98" />

### Run Container
```
docker run -d -p 8080:8080 networksecurity
```
<img width="2880" height="1725" alt="WhatsApp Image 2026-05-01 at 11 33 28 (1)" src="https://github.com/user-attachments/assets/3ae82d2e-274d-48d1-9f7d-70add1ea247c" />

---

## ☁️ AWS Deployment Flow

1. Push code to GitHub  
2. GitHub Actions triggers CI/CD  
3. Docker image is built  
4. Image pushed to AWS ECR  
5. EC2 pulls latest image  
6. Container runs automatically

<img width="2880" height="1731" alt="WhatsApp Image 2026-05-01 at 11 33 29" src="https://github.com/user-attachments/assets/d1bcc0da-b7c1-4c56-9638-1c82ac9f21ae" />

---

## 🔄 CI/CD Pipeline

The pipeline includes:
- Code checkout  
- Build Docker image  
- Push to AWS ECR  
- Deploy to EC2  

<img width="2880" height="1725" alt="WhatsApp Image 2026-05-01 at 11 33 28 (1)" src="https://github.com/user-attachments/assets/5c1183cd-a7cd-48f7-b485-635fffda7c36" />

---

## 📊 Experiment Tracking

- Integrated MLflow with DagsHub  
- Tracks:
  - Accuracy
  - Precision
  - Recall
  - F1-score  
- Enables comparison across multiple runs
  
<img width="2880" height="1735" alt="WhatsApp Image 2026-05-01 at 11 33 28 (2)" src="https://github.com/user-attachments/assets/4e980d11-2678-4f95-ba0a-7ed0547c04ee" />

---

## 📦 Storage

- AWS S3 for:
  - Model artifacts  
  - Pipeline outputs  
  - Versioned storage
    
<img width="2880" height="1724" alt="WhatsApp Image 2026-05-01 at 11 33 27 (2)" src="https://github.com/user-attachments/assets/d5b5a1bf-d22c-4fe2-9e05-1f4a10b7b844" />

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
