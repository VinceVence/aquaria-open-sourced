# yolo_service.py
import cv2
import numpy as np
from ultralytics import YOLO

class YOLOService:
    def __init__(self, model_path, resize=None):
        self.model = YOLO(model_path)
        self.resize = resize

    def detect(self, img_path):
        # Read the image
        img = cv2.imdecode(np.fromstring(img_path.read(), np.uint8), cv2.IMREAD_COLOR)

        # Resize the image if resize parameter is set
        if self.resize is not None:
            img = cv2.resize(img, self.resize)

        # Pass the image through the detection model and get the result
        detect_result = self.model(img)

        # Plot the detections
        detect_img = detect_result[0].plot()

        # Convert the image to RGB format
        detect_img = cv2.cvtColor(detect_img, cv2.COLOR_BGR2RGB)

        return detect_img
