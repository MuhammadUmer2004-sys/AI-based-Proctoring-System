def detect_objects(img, model):
    import torch
    import cv2
    results = model(img)
    detected = results.pandas().xyxy[0]['name'].tolist()
    return detected
