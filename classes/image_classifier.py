import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import streamlit as st
import json
from streamlit_extras.colored_header import colored_header

class ImageClassificationService:
    def __init__(self, title, model_path, class_labels, json_data_path=None):
        self.title = title
        self.model = tf.keras.models.load_model(model_path)
        self.class_labels = class_labels
        self.json_data = self.load_json(json_data_path) if json_data_path else None


    @staticmethod
    def load_json(path):
        if path:
            with open(path, 'r') as f:
                return json.load(f)
        return None

    def predict(self, image):
        # Resize the image to match the input shape of the model
        image = cv2.resize(image, (224, 224))
        # Preprocess the image
        image = preprocess_input(image)
        # Convert the image to a numpy array and add a batch dimension
        image = np.expand_dims(image, axis=0)
        # Make a prediction using the loaded model
        prediction = self.model.predict(image)
        # Get the predicted class label
        class_index = np.argmax(prediction)
        # Convert the image from BGR to RGB
        image = cv2.cvtColor(image[0], cv2.COLOR_BGR2RGB)
        return image, self.class_labels[class_index]

    def display(self, image, predicted_class):
        # Display the uploaded image and the predicted class label
        st.image(image, caption=f"Predicted class: {predicted_class}", use_column_width=True)

    def classify_image(self, uploaded_file):
        if uploaded_file is not None:
            # Read the uploaded image as a numpy array
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1)
            image, predicted_class = self.predict(image)
            self.display(image, predicted_class)
            return predicted_class

    def display_info(self, predicted_class):
        if self.json_data and predicted_class in self.json_data:
            colored_header(label=predicted_class + " Metadata",
                           description=self.json_data[predicted_class]["metadata"],
                           color_name="blue-green-70")
            colored_header(label=predicted_class,
                           description=self.json_data[predicted_class]["description"],
                           color_name="blue-green-70")
            colored_header(label=predicted_class + " in the Philippines",
                           description=self.json_data[predicted_class]["ph"],
                           color_name="blue-green-70")
