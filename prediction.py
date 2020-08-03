# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prediction.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class Prediction(object):
    def setupUi(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.setWindowModality(QtCore.Qt.WindowModal)
        self.Dialog.resize(530, 520)
        self.Dialog.setModal(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dialog.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(self.Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 10, 451, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InputLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InputLabel.setFont(font)
        self.InputLabel.setObjectName("InputLabel")
        self.horizontalLayout.addWidget(self.InputLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.layoutWidget_2 = QtWidgets.QWidget(self.Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 450, 451, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.OutputLabel = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.OutputLabel.setFont(font)
        self.OutputLabel.setObjectName("OutputLabel")
        self.horizontalLayout_2.addWidget(self.OutputLabel)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.ImageLabel = QtWidgets.QLabel(self.Dialog)
        self.ImageLabel.setGeometry(QtCore.QRect(20, 40, 491, 391))
        self.ImageLabel.setText("")
        self.ImageLabel.setPixmap(
            QPixmap("E:/IDM Download/skin-cancer-mnist-ham10000/HAM10000_images_part_1/ISIC_0024306.jpg"))
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prediction"))
        self.InputLabel.setText(_translate("Dialog", "Image Id:"))
        self.OutputLabel.setText(_translate("Dialog", "Output: "))
        Dialog.setWindowFlags(
            QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint
        )
        Dialog.setWindowIcon(QIcon('./Icons/icon.png'))

    def showDialog(self):
        self.Dialog.exec_()

    def setImage(self, path):
        self.ImageLabel.setPixmap(QPixmap(path))

    def setInput(self, inputText):
        self.lineEdit.setText(f"Displaying result for {inputText}")

    def setOutput(self, outputText,accuracy):
        self.textEdit.setText(f"There is a {accuracy}% chance that you have {outputText} cancer")


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Prediction()
#     ui.setupUi()
#     Dialog.show()
#     sys.exit(app.exec_())
