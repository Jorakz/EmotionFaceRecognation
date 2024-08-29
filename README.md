## EmotionFaceRecognition 
EmotionFaceRecognition is a Python-based program that uses a webcam to scan faces and predict one of seven different emotions: angry, sad, happy, fear, neutral, disgust, and surprise. The program leverages OpenCV for real-time face detection and a pre-trained Convolutional Neural Network (CNN) model for emotion recognition.

## Features

**Real-Time Emotion Detection:** Uses your webcam to detect and predict emotions in real-time.

**Seven Emotion Categories:** Recognizes seven different emotions: angry, sad, happy, fear, neutral, disgust, and surprise.

**Pre-Trained CNN Model:** The model has been trained on two dataset.

## Model accuracy
"best_model_emotion_7" has accuracy:

__Training Accuracy:__ 77.69% 

__Validation Accuracy:__ 67.57%

__Test Accuracy:__ 66.65%

## Datasets

The CNN model was trained on the following datasets:

**FER-2013:** FER-2013 on Kaggle

**Natural Human Face Images for Emotion Recognition:** Natural Human Face Images for Emotion Recognition on Kaggle

**<sub> All images were preprocessed and resized to 48x48 pixels to fit the model's input requirements. </sub>**

## Files

**"main.py":** This is the entry point of the program. It likely initializes the application, loads the necessary modules, and starts the GUI.

**"import_csv.py":** Script imports images, scales pixel values from 255 to 0 (inverting the grayscale values), and exports the processed data to a CSV file. This is useful for preparing datasets for training or analysis.

**"image_editor.py":** Script resizes images to 48x48 pixels. Resizing is a common preprocessing step in machine learning, particularly when standardizing input sizes for a model.

**"prediction.py":** File uses the webcam to capture images and classify them into one of seven different emotions. It likely uses a pre-trained neural network model for this task.

**"widgets.py":** Contains the definitions and functionalities for the various widgets in the Qt GUI application. This file might define buttons, sliders, labels, and other interactive elements.

**"window_ui.py":** Responsible for updating and managing the widget parameters, such as setting default values, updating states based on user interactions, and managing the layout.

**haarcascade_frontalface_default.xml:** An XML file containing pre-trained data for the Haar Cascade algorithm, which is used for detecting faces in images. It includes coefficients for identifying facial features like the nose, eyes, and mouth.

**"best_model_emotion_7"**: pre-trained CNN model for face emotion recognation by 7 different type of emotion wich work with grayscale images 48x48 pixels 


