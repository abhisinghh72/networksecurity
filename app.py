import sys
import os

import certifi
from dotenv import load_dotenv
import pandas as pd
import pymongo

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.constant.training_pipeline import (
    DATA_INGESTION_COLLECTION_NAME,
    DATA_INGESTION_DATABASE_NAME
)

# ENV SETUP
load_dotenv()
mongo_db_url = os.getenv("MONGODB_URL_KEY")

ca = certifi.where()

# MONGO
client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

# FASTAPI APP 
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates
templates = Jinja2Templates(directory="templates")

# ROUTES

@app.get("/", tags=["Home"])
async def index():
    return RedirectResponse(url="/docs")


# TRAINING ROUTE
@app.get("/train", tags=["Training"])
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training completed successfully")

    except Exception as e:
        raise NetworkSecurityException(e, sys)

# PREDICTION ROUTE 
@app.post("/predict", tags=["Prediction"])
async def predict_route(request: Request, file: UploadFile = File(...)):
    try:
        # Read CSV
        df = pd.read_csv(file.file)

        if df.empty:
            return {"error": "Uploaded file is empty"}

        # Load trained model (contains preprocessor + model)
        model = load_object("final_model/model.pkl")

        # Optional: column validation
        if hasattr(model, "feature_names_in_"):
            missing_cols = [col for col in model.feature_names_in_ if col not in df.columns]
            if missing_cols:
                return {"error": f"Missing columns: {missing_cols}"}

        # Predict
        y_pred = model.predict(df)
        df["predicted_column"] = y_pred

        # Save output
        os.makedirs("prediction_output", exist_ok=True)
        df.to_csv("prediction_output/output.csv", index=False)

        # Convert to HTML
        table_html = df.to_html(classes="table table-striped")

        return templates.TemplateResponse(
            "table.html",
            {
                "request": request,
                "table": table_html
            }
        )

    except Exception as e:
        return {"error": str(e)}


# MAIN
if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8080)