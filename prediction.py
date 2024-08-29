import cv2
import numpy as np
from keras.models import load_model
model = load_model('best_model_emotion_7.h5')

def register_face(frame):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                              flags=cv2.CASCADE_SCALE_IMAGE)

    return faces, gray
def analize_image(gray,frame,faces):
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        formatted_arr, emotion_index = process_image(face_roi)

    return frame, formatted_arr, emotion_index

def process_image(face_roi):

    face_roi_resized = cv2.resize(face_roi, (48, 48))
    face_roi_normalized = face_roi_resized / 255.0
    formatted_arr, emotion_index = predict_emotion(face_roi_normalized)
    return formatted_arr, emotion_index

def redact_result(emotion_prediction):
    percent_arr = np.around(emotion_prediction * 100, decimals=2)
    formatted_arr = np.array([[x for x in row] for row in percent_arr])
    return formatted_arr

def predict_emotion(face_roi_normalized):

    emotion_prediction = model.predict(np.array([face_roi_normalized]))
    formatted_arr = redact_result(emotion_prediction)
    emotion_index = np.argmax(emotion_prediction)
    return formatted_arr, emotion_index