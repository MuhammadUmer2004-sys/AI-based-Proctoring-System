 AI-based-Proctoring-System

🎓 AI-Powered Exam Proctoring Tool
An intelligent web-based proctoring system designed to monitor online exams in real-time using computer vision and AI. This tool enhances exam integrity by detecting suspicious behaviors like multiple faces, phone usage, no face presence, and gaze direction (looking away from the screen).

🚀 Features
👁️‍🗨️ **Real-Time Monitoring via Webcam**
👤 **Multiple Face Detection** – Alerts when more than one person appears.
🙈 **No Face Detected** – Alerts when the candidate leaves the frame.
👀 **Gaze Tracking** – Detects if the user looks left or right (away from the screen).
📱 **Phone Detection** – Detects the presence of mobile phones.
🛑 **Alert Dashboard** – Live alerts with visual indicators for all suspicious behavior.

🛠️ Tech Stack

🎨 Frontend
**React.js**
**Webcam API** – For live video feed
**Axios** – HTTP client for communicating with the Flask backend

⚙️ Backend
**Flask (Python)**
**Flask-CORS** – Cross-Origin support for API
**OpenCV** – Image preprocessing and handling
**REST APIs** – Exposes endpoints to receive webcam frames and return alerts

🧠 AI / ML Models
**YOLOv5** – Real-time object detection (used for mobile phone detection)
**dlib** – Facial landmark detection
**face_recognition** – Face detection and direction tracking
**Custom Alert Logic** – To trigger alerts based on behavior rules

📂 Folder Structure

exam-proctoring-tool/
│
├── backend/
│ ├── app.py # Main Flask application
│ ├── config.py # Configurations and constants
│ ├── detectors/
│ │ ├── face_detector.py # Detects presence and number of faces
│ │ ├── gaze_tracker.py # Tracks face direction (left/right/center)
│ │ └── multi_face_checker.py # Checks for multiple faces
│ │
│ ├── models/
│ │ └── yolov5/
│ │ ├── yolov5s.pt # Pretrained YOLOv5 model
│ │ ├── detect.py # YOLOv5 detection logic
│ │ └── utils/ # Helper utilities
│ │
│ ├── static/
│ │ └── logs/ # Optional: save screenshots/logs
│ │
│ ├── utils/
│ │ ├── alerts.py # Alert trigger and logic
│ │ └── logger.py # Event logging
│ │
│ ├── requirements.txt # Python dependencies
│ └── README.md # Backend-specific readme
│
├── frontend/
│ ├── public/
│ │ ├── index.html # Root HTML file
│ │ └── favicon.ico
│ │
│ ├── src/
│ │ ├── components/
│ │ │ ├── WebcamFeed.jsx # Webcam feed component
│ │ │ ├── Alerts.jsx # Alert component
│ │ │ └── Navbar.jsx
│ │ │
│ │ ├── pages/
│ │ │ └── Home.jsx
│ │ │
│ │ ├── services/
│ │ │ └── api.js # API communication logic
│ │ │
│ │ ├── App.js
│ │ ├── index.js
│ │ └── styles/
│ │ └── main.css
│ │
│ ├── .env # API base URL
│ ├── package.json # React dependencies
│ └── README.md # Frontend-specific readme
│
├── .gitignore
├── LICENSE
└── README.md # Project overview (this file)

🧪 Setup & Installation
1. Clone the Repository
```bash
git clone https://github.com/yourusername/exam-proctoring-tool.git
cd exam-proctoring-tool

2. Setup Backend (Flask)
cd backend
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python app.py

3. Setup Frontend (React)
cd ../frontend
npm install
npm start

Make sure your backend is running on http://localhost:5000 and frontend on http://localhost:3000.
📈 Future Improvements

🧠 Add AI-based cheating behavior prediction (using LSTM/CNN)
📹 Record suspicious clips
💾 Upload reports to cloud storage (e.g., Firebase, S3)
🛡️ Admin panel for manual review

👤 Author
Muhammad Umer
Github: https://github.com/MuhammadUmer2004-sys

📄 License
This project is licensed under the MIT License.
