from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastai.vision.all import *
import base64
import re
import os

app = FastAPI()

# CORS (optional but helpful in development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static and Template files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load model
learn = load_learner("model/accident_detector.pkl")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict_upload/")
async def predict_upload(data: dict):
    image_data = re.sub('^data:image/.+;base64,', '', data['image'])
    img_bytes = base64.b64decode(image_data)
    img = PILImage.create(img_bytes)
    pred, pred_idx, probs = learn.predict(img)
    return JSONResponse(content={"prediction": pred, "confidence": f"{probs[pred_idx]*100:.2f}%"})

@app.post("/predict_webcam/")
async def predict_webcam(data: dict):
    image_data = re.sub('^data:image/.+;base64,', '', data['image'])
    img_bytes = base64.b64decode(image_data)
    img = PILImage.create(img_bytes)
    pred, pred_idx, probs = learn.predict(img)
    return JSONResponse(content={"prediction": pred, "confidence": f"{probs[pred_idx]*100:.2f}%"})
