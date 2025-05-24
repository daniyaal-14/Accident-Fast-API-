# 🚗 Accident Detection System using FastAI + FastAPI + OpenCV

This is a complete end-to-end accident detection web application using deep learning. It allows users to either upload an image or use their webcam to detect if an accident has occurred in the image. Built with FastAI for the model, FastAPI for the backend, and HTML/CSS/JavaScript for the frontend.

---

## 📁 Folder & File Structure

Your project should be structured like this:

Accident-FastAPI-Project/
├── models/
│   └── accident_model.pkl              → Trained FastAI model file
├── static/
│   └── style.css                       → Styling for the frontend
├── templates/
│   └── index.html                      → Main web page with upload + webcam
├── main.py                             → FastAPI backend
├── requirements.txt                    → Required Python libraries
├── README.md                           → You’re reading it now
└── .env (optional)                     → For storing SendGrid API credentials

---

## ✅ Features

- Accident detection via image upload
- Accident detection via webcam capture
- Clean UI with two options
- Optional: Send SOS email using SendGrid when accident is detected

---

## 🛠️ How to Set Up and Run the Project (for Beginners)

**Step 1: Download the project**

Option 1: Clone using Git  
→ git clone https://github.com/<your-username>/Accident-FastAPI-Project.git  
→ cd Accident-FastAPI-Project

Option 2: Download ZIP  
→ Click the green "Code" button on GitHub → "Download ZIP"  
→ Extract and open the folder

---

**Step 2: Install Python (if not installed)**  
→ Download from https://www.python.org/downloads/  
→ Make sure Python 3.9 or above is installed  
→ Check using: python --version

---

**Step 3: Create and Activate Virtual Environment**

Windows:  
→ python -m venv venv  
→ venv\Scripts\activate

Mac/Linux:  
→ python3 -m venv venv  
→ source venv/bin/activate

---

**Step 4: Install Requirements**

→ pip install -r requirements.txt

---

**Step 5: Place the Model File**

Make sure you have the trained model file named `accident_model.pkl` inside the `models/` folder.

models/  
└── accident_model.pkl

---

**Step 6: Run the FastAPI App**

→ uvicorn main:app --reload

Then open your browser and go to:

http://127.0.0.1:8000

You will see the web app with two buttons:

- Upload Image and Predict
- Open Webcam and Predict

---

## 📸 Webcam Functionality

When you click "Open Webcam and Predict", a JavaScript function will capture a photo from your live camera and send it to the backend for prediction.

Make sure you allow browser permission to use your webcam.

---

## 💌 Optional: SOS Email Alert (Using SendGrid)

If you want to receive an email when an accident is detected:

**Step 1: Create a SendGrid Account**

→ https://sendgrid.com  
→ Generate an API Key  
→ Verify your sender email

**Step 2: Create a .env File in Project Root**

Create a file named `.env` (no filename, just `.env`) and paste:

SENDGRID_API_KEY=your_sendgrid_api_key  
SENDER_EMAIL=your_verified_email@example.com  
RECEIVER_EMAIL=your_target_email@example.com

**Note:** This file is ignored from Git using `.gitignore` and must NOT be uploaded to GitHub.

---

**Step 3: Send Email from the Code**

The FastAPI backend has built-in support using SendGrid. If enabled and keys are configured, it will automatically send an email if an accident is detected.

---

## 🌐 Deployment

This app is built to run locally, but can be deployed on:

- Heroku
- Railway
- Render
- Any VPS or personal website

Make sure to include the `.pkl` model, dependencies, and environment variables during deployment.

---

## 🧪 File Overview

1. `main.py` → FastAPI app with all prediction logic
2. `templates/index.html` → HTML page with webcam and upload support
3. `static/style.css` → Styling
4. `models/accident_model.pkl` → Trained accident detection model
5. `.env` → Email credentials (optional)
6. `requirements.txt` → All required libraries

---

## 📦 GitHub Upload Steps

To upload this to your GitHub repository:

→ git init  
→ git remote add origin https://github.com/<your-username>/<repo-name>.git  
→ git add .  
→ git commit -m "Initial commit"  
→ git branch -M main  
→ git push -u origin main

If you face push issues due to secrets, remove `.env` or reset commit history.

---

## 💼 LinkedIn Caption (To Share Your Project)

🚨 Real-Time Accident Detection App (FastAI + FastAPI)  
Proud to launch my deep learning-powered web app that detects car accidents from images or webcam input.  
Built with FastAI, FastAPI, OpenCV and deployed with a slick UI!  

💡 Features:  
- Upload or use webcam to detect accidents  
- Optionally receive SOS email alerts using SendGrid  

🔗 GitHub: https://github.com/daniyaal-14/Accident-Fast-API-
#DeepLearning #FastAI #OpenCV #FastAPI #ComputerVision #Python

---

## 👨‍💻 Author

Your Name  
Email: iqbaldaniyal20@gmail.com  
LinkedIn: https://www.linkedin.com/in/iqbaldaniyal20/

---

## ⭐ Like This Project?

Star this repo and share it! Feel free to fork, contribute, or reach out.

