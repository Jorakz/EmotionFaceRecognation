import prediction as pred
import window_ui as ui
from PyQt5 import QtCore, QtGui, QtWidgets

import cv2
from PyQt5.Qt import *

emotion_labels = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sadness', 'Surprise', 'Neutral']

class ThreadOpenCV(QThread):
    changePixmap = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()



    def run(self):
        self.var_work = True
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


        while self.var_work:

            ret, frame = cap.read()

            faces, gray = pred.register_face(frame)

            if ret:
                if(type(faces) != tuple):
                    frame, formatted_arr, emotion_index = pred.analize_image(gray, frame, faces)
                    global angry, disgust, fear, happy, sadness, surprise, neutral, id
                    angry = int(formatted_arr[0][0])
                    disgust = int(formatted_arr[0][1])
                    fear = int(formatted_arr[0][2])
                    happy = int(formatted_arr[0][3])
                    sadness = int(formatted_arr[0][4])
                    surprise = int(formatted_arr[0][5])
                    neutral = int(formatted_arr[0][6])
                    id = emotion_index

                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape

                bytesPerLine = ch * w
                convertToQtFormat = QImage(
                    rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)

                p = convertToQtFormat.scaled(941, 821, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)


                if cv2.waitKey(1) == ord('q'):
                    break

            self.msleep(50)

            cv2.destroyAllWindows()

    def stop(self):
        self.var_work = False
        self.quit()


class Window(QtWidgets.QWidget, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_start.clicked.connect(self.can)
        self.button_stop.clicked.connect(self.cancel)

        self.thread = ThreadOpenCV()                                      # +++
        self.thread.changePixmap.connect(self.setImage)                   # +++

    def cancel(self):
         self.thread.stop()
    def can(self):
        self.thread.start()                                               # +++

    def setImage(self, image):

        self.imgLabel.setPixmap(QPixmap.fromImage(image))
        global angry,disgust,fear,happy,sadness, surprise, neutral,id,emotion_labels
        self.bar_anger.setValue(angry)
        self.bar_disgust.setValue(disgust)
        self.bar_fear.setValue(fear)
        self.bar_happy.setValue(happy)
        self.bar_sadness.setValue(sadness)
        self.bar_surprice.setValue(surprise)
        self.bar_neutral.setValue(neutral)
        self.result.setText(emotion_labels[id])

