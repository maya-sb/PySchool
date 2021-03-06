from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 414)
        Dialog.setStyleSheet("QDialog{\n""background-color: rgb(21, 143, 181)\n""}")

        self.btnConfirmar = QtWidgets.QPushButton(Dialog)
        self.btnConfirmar.setGeometry(QtCore.QRect(140, 370, 111, 31))
        self.btnConfirmar.setStyleSheet("font: 25 10pt \"Malgun Gothic Semilight\";\n""border: 0.7px solid grey;\n""border-radius: 10px;\n""background-color: rgb(255, 123, 28);\n")
        self.btnConfirmar.setObjectName("btnConfirmar")

        self.frameLaranja = QtWidgets.QFrame(Dialog)
        self.frameLaranja.setGeometry(QtCore.QRect(10, 0, 381, 10))
        self.frameLaranja.setStyleSheet("background-color: rgb(255, 123, 28);\n"
"border-radius: 0.2px;\n"
"")
        self.frameLaranja.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLaranja.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLaranja.setObjectName("frameLaranja")

        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 381, 351))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 358, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Escolher Matéria"))
        self.btnConfirmar.setText(_translate("Dialog", "Confirmar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())