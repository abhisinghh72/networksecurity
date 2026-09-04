import sys
import os

import certifi
from dotenv import load_dotenv
import pandas as pd
from networksecurity.utils.ml_utils import model
import pymongo

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run
from networksecurity.constant.training_pipeline import TARGET_COLUMN

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
async def predict_route(
    request: Request,
    file: UploadFile = File(...)
):
    try:

        # Read CSV
        df = pd.read_csv(file.file)

        if df.empty:
            return {"error": "Uploaded file is empty"}

        # Load model
        model = load_object("final_model/model.pkl")

        # Load preprocessor
        preprocessor = load_object("final_model/preprocessor.pkl")

        # Remove target column if present
        if TARGET_COLUMN in df.columns:
            df = df.drop(columns=[TARGET_COLUMN])

        # Transform input
        x_transformed = preprocessor.transform(df)

        # Predict
        y_pred = model.predict(x_transformed)

        # Add prediction
        df["predicted_column"] = y_pred

        # Save prediction
        os.makedirs("prediction_output", exist_ok=True)

        df.to_csv(
            "prediction_output/output.csv",
            index=False
        )

        # Convert to HTML
        table_html = df.to_html(
            classes="table table-striped"
        )

        # Return HTML page
        return templates.TemplateResponse(
            request=request,
            name="table.html",
            context={
                "request": request,
                "table": table_html
            }
        )

    except Exception as e:

        import traceback
        traceback.print_exc()

        return {
            "error": str(e)
        }
# MAIN
if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8080)