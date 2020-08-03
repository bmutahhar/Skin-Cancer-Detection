import json
import os

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog

from prediction import Prediction

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model

accuracies = json.load(open('./Models/accuracies.json'))
modelCNN = load_model('./Models/modelCNN.h5')
modelVGG = load_model('./Models/modelVGG.h5')


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(438, 188)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 0, 431, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 130, 191, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.convertPredictButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convertPredictButton.setFont(font)
        self.convertPredictButton.setObjectName("convertPredictButton")
        self.horizontalLayout_3.addWidget(self.convertPredictButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelPushButton.setFont(font)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 35, 411, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sourceLabel = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sourceLabel.setFont(font)
        self.sourceLabel.setObjectName("sourceLabel")
        self.horizontalLayout.addWidget(self.sourceLabel)
        self.sourceLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sourceLineEdit.setFont(font)
        self.sourceLineEdit.setReadOnly(True)
        self.sourceLineEdit.setObjectName("sourceLineEdit")
        self.horizontalLayout.addWidget(self.sourceLineEdit)
        self.sourcePushButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sourcePushButton.setFont(font)
        self.sourcePushButton.setObjectName("sourcePushButton")
        self.horizontalLayout.addWidget(self.sourcePushButton)
        self.cnnRadioButton = QtWidgets.QRadioButton(self.frame)
        self.cnnRadioButton.setGeometry(QtCore.QRect(130, 90, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cnnRadioButton.setFont(font)
        self.cnnRadioButton.setObjectName("cnnRadioButton")
        self.vggRadioButton = QtWidgets.QRadioButton(self.frame)
        self.vggRadioButton.setGeometry(QtCore.QRect(210, 90, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vggRadioButton.setFont(font)
        self.vggRadioButton.setObjectName("vggRadioButton")
        self.convertPredictButton.setEnabled(False)
        self.cnnRadioButton.setChecked(True)
        self.cnnRadioButton.setEnabled(False)
        self.vggRadioButton.setEnabled(False)
        self.input = None
        self.output = None
        self.prediction = Prediction()
        self.prediction.setupUi()

        self.retranslateUi(Dialog)
        self.sourcePushButton.clicked.connect(self.browseImage)
        self.convertPredictButton.clicked.connect(self.Predict)
        self.cancelPushButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Skin Cancer Detector"))
        Dialog.setWindowTitle(_translate("Dialog", "Skin Cancer Detector"))
        Dialog.setWindowFlags(
            QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint
        )
        Dialog.setWindowIcon(QIcon('./Icons/icon.png'))

        self.convertPredictButton.setText(_translate("Dialog", "Predict"))
        self.cancelPushButton.setText(_translate("Dialog", "Close"))
        self.sourceLabel.setText(_translate("Dialog", "Image Path"))
        self.sourceLineEdit.setPlaceholderText(_translate("Dialog", "Select the Image path"))
        self.sourcePushButton.setText(_translate("Dialog", "Browse"))
        self.cnnRadioButton.setText(_translate("Dialog", "CNN"))
        self.vggRadioButton.setText(_translate("Dialog", "VGG16"))

    def browseImage(self):
        output = QFileDialog.getOpenFileName(None, "Select Input Image to Predict", filter="JPG files (*.jpg)")
        if output[0]:
            self.sourceLineEdit.setText(output[0])
            self.prediction.setImage(output[0])
            self.cnnRadioButton.setEnabled(True)
            self.vggRadioButton.setEnabled(True)
            self.convertPredictButton.setEnabled(True)

    def vec2word(self, pred):
        labels_dict = {
            0: 'akiec',
            1: 'bcc',
            2: 'bkl',
            3: 'df',
            4: "nv",
            5: 'vasc',
            6: 'mel',
        }
        lesion_type_dict = {
            'akiec': 'Actinic Keratose',
            'bcc': 'Basal Cell Carcinoma',
            'bkl': 'Benign Keratosis-like Lesion',
            'df': 'Dermatofibroma',
            'nv': 'Melanocytic Nevi',
            'vasc': 'Vascular Lesion',
            'mel': 'Melonoma'
        }
        pred = np.argmax(pred)
        return lesion_type_dict.get(labels_dict.get(pred))

    def Predict(self):
        img = cv2.imread(self.sourceLineEdit.text())
        img = cv2.resize(img, (28, 28))
        if self.cnnRadioButton.isChecked():
            accuracy = accuracies[0]['CNN']
            pred = modelCNN.predict(img.reshape(1, 28, 28, 3))
        else:
            accuracy = accuracies[1]['VGG']
            pred = modelVGG.predict(img.reshape(1, 28, 28, 3))

        pred = self.vec2word(pred)
        self.prediction.setImage(self.sourceLineEdit.text())
        self.prediction.setInput(os.path.basename(self.sourceLineEdit.text()))
        self.prediction.setOutput(pred, str(round(accuracy * 100, 2)))
        self.prediction.showDialog()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
