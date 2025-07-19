from flask import Flask, Response, request
from flask_cors import CORS
import cv2
import face_recognition
import numpy as np
import torch
import os
from gaze_tracker import is_looking_away
from yolov5_detector import detect_objects

app = Flask(__name__)
CORS(app)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

@app.route('/')
def index():
    return 'Proctoring Server Running'

@app.route('/video_feed', methods=['POST'])
def video_feed():
    file = request.files['frame']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    alerts = []
    face_locations = face_recognition.face_locations(img)
    if len(face_locations) == 0:
        alerts.append('No face detected')
    elif len(face_locations) > 1:
        alerts.append('Multiple faces detected')
    if len(face_locations) == 1:
        face_landmarks = face_recognition.face_landmarks(img)
        if not is_looking_away(face_landmarks):
            alerts.append('Possible distraction (looking away)')
    objects = detect_objects(img, model)
    if 'cell phone' in objects:
        alerts.append('Phone detected')
    return {'alerts': alerts}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
