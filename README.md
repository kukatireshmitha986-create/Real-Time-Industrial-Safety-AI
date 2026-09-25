# AI-Powered Real-Time Industrial Safety Monitoring and Violation Detection System

An AI-powered **Deep Learning and Computer Vision** system for real-time industrial safety monitoring. The system uses **YOLO11, OpenCV, Python, FastAPI, React, and SQLite** to detect workers without helmets, identify safety violations, automatically capture evidence, store violation records, and display them through a web-based dashboard.

## 📌 Project Overview

Industrial workplaces require continuous monitoring to ensure that workers follow safety regulations. Manual monitoring can be difficult in large industrial environments and may result in missed safety violations.

This project provides an automated AI-based safety monitoring solution that can:

- Detect heads and helmets in real time
- Identify workers without helmets
- Display safety violation warnings
- Capture screenshots as evidence
- Store violation records in SQLite
- Provide violation data through REST APIs
- Display safety events through a React dashboard

The project combines **Deep Learning, Computer Vision, Backend Development, Database Management, and Frontend Development** into one complete real-time application.

## 🎯 Objectives

- Develop a real-time industrial safety monitoring system
- Use Deep Learning for object detection
- Detect helmets using YOLO11
- Detect heads without helmets
- Automatically identify safety violations
- Capture visual evidence of violations
- Store safety events in a database
- Provide REST APIs for event management
- Build a professional monitoring dashboard
- Demonstrate an end-to-end AI application

## 🧠 Deep Learning

This is primarily a **Deep Learning and Computer Vision project** because it uses a trained YOLO11 neural network for object detection.

The Deep Learning workflow is:

    Training Dataset
          ↓
    YOLO11 Neural Network
          ↓
    Model Training
          ↓
    Trained Model
          ↓
    Real-Time Inference
          ↓
    Head / Helmet Detection
          ↓
    Safety Violation Detection

The Deep Learning model is combined with OpenCV, FastAPI, SQLite, and React to create a complete real-time system.

## 🚀 Key Features

### 🤖 Real-Time AI Detection

The system uses a trained **YOLO11n** object detection model to analyze webcam frames in real time.

### ⛑️ Helmet Detection

The trained model detects two classes:

    Class 0 = Head
    Class 1 = Helmet

### ⚠️ No-Helmet Detection

When a head is detected without a corresponding helmet, the system identifies it as a safety violation.

Example:

    SAFETY VIOLATION DETECTED
    HEAD - NO HELMET

### 📸 Automatic Evidence Capture

When a safety violation is detected, the system automatically captures a screenshot and stores it in the screenshots directory.

Example:

    violation_20260925_091606.jpg
    violation_20260925_091611.jpg

### 🗄️ SQLite Event Logging

Every detected violation can be stored with:

- Event ID
- Timestamp
- Violation type
- Confidence score
- Screenshot path
- Status

### ⚡ FastAPI Backend

FastAPI provides REST APIs for:

- Backend health
- Safety events
- Recent events
- Event count
- Individual event details
- Evidence image access

### 📊 React Dashboard

The web dashboard provides:

- Backend status
- Total violations
- Recent violations
- Live monitoring status
- Violation table
- Confidence information
- Evidence viewing
- System architecture
- Technology information

### 🔄 Automatic Dashboard Refresh

The dashboard periodically refreshes the event information so newly detected violations can appear automatically.

### 📷 Evidence Viewer

Users can click the evidence button to view the captured violation image.

## 🏗️ System Architecture

    ┌─────────────────┐
    │     Webcam      │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │     OpenCV      │
    │ Video Capture   │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │     YOLO11      │
    │ Deep Learning   │
    │ Object Detection│
    └────────┬────────┘
             │
       ┌─────┴─────┐
       │           │
       ▼           ▼
    Head        Helmet
    Detection   Detection
       │           │
       └─────┬─────┘
             │
             ▼
    ┌─────────────────┐
    │ Violation Logic │
    │ Head without    │
    │ Helmet          │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Evidence Capture│
    │   Screenshot    │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │     SQLite      │
    │ Safety Events   │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │     FastAPI     │
    │    REST API     │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ React Dashboard │
    └─────────────────┘

## 📚 Dataset

The project uses the **Helmet Detection Dataset** downloaded from Kaggle.

Kaggle Dataset:

https://www.kaggle.com/datasets/npk7264/helmet-dataset

Dataset information:

- 875 images
- YOLO-format annotations
- Train, validation, and test sets
- Two detection classes
- Dataset license: CC BY 4.0

The dataset contains:

    dataset/
    ├── train/
    ├── valid/
    ├── test/
    ├── data.yaml
    ├── README.dataset.txt
    └── README.roboflow.txt

The dataset classes used in this project are:

    Class 0 → Head
    Class 1 → Helmet

The dataset is excluded from the GitHub repository because of its size.

## 📈 Model Training

The project uses **YOLO11n** from the Ultralytics framework.

Training configuration:

    Model: YOLO11n
    Image Size: 640 × 640
    Epochs: 20
    Batch Size: 8
    Workers: 2
    Patience: 5

Training script:

    training/train.py

The model was trained using:

    dataset/data.yaml

The best trained model is generated under the YOLO training output directory.

## 📊 Model Performance

The trained model achieved approximately:

    Precision:   0.968
    Recall:      0.909
    mAP50:       0.968
    mAP50-95:    0.683

These values are based on the project's training and validation results.

## 🧪 Model Testing

The trained model was tested on the test images using:

    training/test_model.py

The testing script runs YOLO predictions on the test dataset and saves the generated prediction images.

Test prediction output is generated inside the YOLO runs directory.

## 🖥️ Real-Time Detection

Real-time detection is implemented in:

    training/realtime_detection.py

The application performs the following operations:

1. Opens the webcam
2. Captures video frames
3. Runs YOLO11 inference
4. Detects heads
5. Detects helmets
6. Compares detections
7. Identifies no-helmet violations
8. Draws bounding boxes
9. Displays safety status
10. Captures evidence screenshots
11. Stores violation events in SQLite

Press:

    Q

to stop the real-time monitoring window.

## 🗃️ Database

The project uses:

    SQLite

Database file:

    detections/safety_events.db

The database stores:

    id
    timestamp
    violation_type
    confidence
    screenshot_path
    status

Example event:

    ID: 1
    Violation: No Helmet
    Confidence: 78.24%
    Status: Open

The SQLite database is excluded from GitHub using .gitignore.

## ⚡ Backend

Backend technologies:

    Python
    FastAPI
    SQLite
    Uvicorn

Backend file:

    backend/server.py

Backend URL:

    http://127.0.0.1:8000

FastAPI documentation:

    http://127.0.0.1:8000/docs

## 🔌 API Endpoints

### Health Check

    GET /api/health

Returns the status of the backend, database, and screenshot directory.

Example response:

    {
        "status": "success",
        "backend": "running",
        "database": "SQLite",
        "database_exists": true,
        "screenshots_exists": true
    }

### Get All Events

    GET /api/events

Returns all recorded safety violation events.

### Get Recent Events

    GET /api/events/recent

Returns the latest safety violation events.

### Get Event Count

    GET /api/events/count

Returns the total number of recorded violations.

### Get Individual Event

    GET /api/events/{event_id}

Returns details for a specific safety event.

### Evidence Images

    GET /screenshots/{filename}

Provides access to captured evidence screenshots.

## ⚛️ Frontend

The frontend is developed using:

    React
    Vite
    JavaScript
    CSS

Frontend directory:

    frontend/

Main files:

    frontend/
    ├── public/
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   ├── index.css
    │   └── main.jsx
    ├── package.json
    └── vite.config.js

## 📊 Dashboard

The React dashboard contains the following sections:

### System Status

Shows whether the FastAPI backend is online.

### Total Violations

Displays the total number of recorded safety violations.

### Recent Violations

Displays recently detected safety events.

### Live Monitoring

Displays the current AI monitoring status.

### Violation Table

The table displays:

    ID
    Timestamp
    Violation
    Confidence
    Status
    Evidence

### Evidence Viewer

Users can select an event and view its captured screenshot.

## 📸 Project Screenshots

The following screenshots demonstrate the real-time AI detection and evidence capture functionality.

### 🤖 Real-Time AI Safety Detection

![Real-Time Safety Violation Detection](screenshots/violation_20260925_091606.jpg)

### ⚠️ No-Helmet Violation Detection

![No Helmet Violation](screenshots/violation_20260925_091611.jpg)

### 📷 Additional Detection Evidence

![Additional Safety Detection](screenshots/class_inspection.jpg)

### 📸 Previous Violation Evidence

![Violation Evidence](screenshots/violation_20260923_211640.jpg)

### 📸 Previous Violation Detection

![Violation Detection](screenshots/violation_20260923_211645.jpg)

### 📸 Safety Monitoring Evidence

![Safety Monitoring Evidence](screenshots/violation_20260923_211707.jpg)

### 📸 Latest Previous Detection

![Latest Previous Detection](screenshots/violation_20260924_200255.jpg)

> These screenshots show the AI detection output and captured evidence generated by the real-time monitoring system.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | AI and backend development |
| YOLO11 | Deep Learning object detection |
| Ultralytics | YOLO training and inference |
| OpenCV | Real-time video processing |
| FastAPI | REST API backend |
| Uvicorn | FastAPI server |
| SQLite | Event database |
| React | Web dashboard |
| Vite | Frontend development |
| JavaScript | Frontend logic |
| CSS | Dashboard styling |

## 📁 Project Structure

    Real-Time-Industrial-Safety-AI/
    │
    ├── backend/
    │   └── server.py
    │
    ├── frontend/
    │   ├── public/
    │   ├── src/
    │   │   ├── App.jsx
    │   │   ├── App.css
    │   │   ├── index.css
    │   │   └── main.jsx
    │   ├── package.json
    │   └── vite.config.js
    │
    ├── training/
    │   ├── database.py
    │   ├── inspect_classes.py
    │   ├── realtime_detection.py
    │   ├── test_model.py
    │   └── train.py
    │
    ├── dataset/
    ├── models/
    ├── detections/
    ├── screenshots/
    ├── runs/
    ├── .gitignore
    ├── package-lock.json
    └── README.md

Large files and generated files such as the dataset, YOLO model weights, training outputs, SQLite database, screenshots, and virtual environment are excluded from GitHub using .gitignore.

## ⚙️ Installation

### 1. Clone the Repository

    git clone https://github.com/kukatireshmitha986-create/Real-Time-Industrial-Safety-AI.git

Move into the project:

    cd Real-Time-Industrial-Safety-AI

## 🐍 Python Environment Setup

Create a virtual environment:

    python -m venv venv

Activate the virtual environment:

    .\venv\Scripts\Activate.ps1

If PowerShell blocks activation, run:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then activate:

    .\venv\Scripts\Activate.ps1

Install the required Python packages:

    python -m pip install ultralytics opencv-python fastapi uvicorn

## ▶️ Run the Backend

Open PowerShell and run:

    cd D:\Real-Time-Industrial-Safety-AI
    .\venv\Scripts\Activate.ps1
    cd backend
    python server.py

The backend will run at:

    http://127.0.0.1:8000

FastAPI documentation:

    http://127.0.0.1:8000/docs

## ⚛️ Run the Frontend

Open another PowerShell terminal:

    cd D:\Real-Time-Industrial-Safety-AI\frontend

Install dependencies:

    npm install

Start the frontend:

    npm run dev

The React application will normally run at:

    http://localhost:5173

## 📷 Run Real-Time AI Monitoring

Open another PowerShell terminal:

    cd D:\Real-Time-Industrial-Safety-AI
    .\venv\Scripts\Activate.ps1
    python training/realtime_detection.py

The webcam will open and begin real-time safety monitoring.

Press Q to stop the monitoring application.

## 🔄 Complete System Execution

### Terminal 1 — Backend

    cd D:\Real-Time-Industrial-Safety-AI
    .\venv\Scripts\Activate.ps1
    cd backend
    python server.py

### Terminal 2 — Frontend

    cd D:\Real-Time-Industrial-Safety-AI\frontend
    npm run dev

### Terminal 3 — AI Monitoring

    cd D:\Real-Time-Industrial-Safety-AI
    .\venv\Scripts\Activate.ps1
    python training/realtime_detection.py

Then open the dashboard:

    http://localhost:5173

## 🔄 End-to-End Workflow

    Webcam
       ↓
    OpenCV Video Capture
       ↓
    YOLO11 Deep Learning Model
       ↓
    Head / Helmet Detection
       ↓
    Safety Violation Logic
       ↓
    No Helmet Detected
       ↓
    Evidence Screenshot
       ↓
    SQLite Database
       ↓
    FastAPI REST API
       ↓
    React Dashboard

## 🧪 Example Detection

When a person is detected without a helmet, the system displays:

    HEAD - NO HELMET
    SAFETY VIOLATION DETECTED

The system then:

1. Detects the head
2. Checks for a corresponding helmet
3. Identifies the safety violation
4. Draws a red bounding box
5. Captures an evidence screenshot
6. Stores the event in SQLite
7. Provides event information through FastAPI
8. Displays the event in the React dashboard

## 📸 Evidence Management

Captured evidence is stored in:

    screenshots/

Example:

    screenshots/
    ├── violation_20260925_091606.jpg
    ├── violation_20260925_091611.jpg
    ├── class_inspection.jpg
    ├── violation_20260923_211640.jpg
    ├── violation_20260923_211645.jpg
    ├── violation_20260923_211707.jpg
    └── violation_20260924_200255.jpg

The FastAPI backend provides the screenshots to the React dashboard.

## 🔐 Safety and Data Considerations

This project is intended as an academic and prototype industrial safety monitoring system.

Real-world deployment should consider:

- Camera placement
- Lighting conditions
- Detection accuracy
- False positives
- False negatives
- Worker privacy
- Data retention
- Secure access control
- Network security
- Hardware performance
- Site-specific model evaluation

The system should be thoroughly evaluated before being used for real workplace safety decisions.

## 📈 Future Enhancements

Possible future improvements include:

- Real-time alert notifications
- Email alerts
- SMS notifications
- Audio alarms
- Multi-worker tracking
- Safety vest detection
- Additional PPE detection
- Restricted-area detection
- CCTV/IP camera integration
- Advanced safety analytics
- Daily safety reports
- Monthly safety reports
- User authentication
- Role-based access control
- Cloud deployment
- Docker deployment
- Mobile monitoring application
- Multi-class industrial safety detection

## 🎓 Academic Value

This project demonstrates practical knowledge of:

- Deep Learning
- Computer Vision
- Object Detection
- YOLO
- Real-Time AI
- OpenCV
- Python
- REST APIs
- FastAPI
- React
- SQLite
- Full-Stack Development
- AI-Based Safety Monitoring
- Evidence Management

The project demonstrates how a Deep Learning model can be integrated with backend services, databases, and a frontend dashboard to create an end-to-end AI application.

## 💼 Resume Description

**AI-Powered Real-Time Industrial Safety Monitoring and Violation Detection System**

Developed a Deep Learning-based real-time industrial safety monitoring system using YOLO11 and OpenCV to detect heads and helmets from webcam video streams. Implemented automated no-helmet violation detection, evidence screenshot capture, SQLite event logging, FastAPI REST APIs, and a React-based monitoring dashboard.

## 📌 Project Highlights

    🤖 YOLO11 Deep Learning
    📷 Real-Time Webcam Monitoring
    ⛑️ Helmet Detection
    👤 Head Detection
    ⚠️ No-Helmet Violation Detection
    📸 Automatic Evidence Capture
    🗄️ SQLite Event Logging
    ⚡ FastAPI REST API
    ⚛️ React Dashboard
    📊 Confidence Visualization
    🔄 Automatic Dashboard Refresh
    🧠 Computer Vision
    🎯 Real-Time AI Inference

## 👩‍💻 Author

**Reshmitha Kukati**

GitHub:

https://github.com/kukatireshmitha986-create

## 📜 License

This project is developed for educational and academic purposes.

The dataset used in this project remains subject to the original dataset provider's licensing terms.

## ⭐ Conclusion

The **AI-Powered Real-Time Industrial Safety Monitoring and Violation Detection System** demonstrates the practical application of Deep Learning and Computer Vision for industrial safety monitoring.

The complete system combines:

    Deep Learning
          +
    YOLO11
          +
    Computer Vision
          +
    Real-Time Detection
          +
    Evidence Capture
          +
    SQLite
          +
    FastAPI
          +
    React

The project provides an end-to-end real-time AI safety monitoring solution capable of detecting no-helmet violations, recording safety events, capturing evidence, and presenting the results through a web dashboard.
