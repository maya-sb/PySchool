from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verAlunos(object):
    def setupUi(self, verAlunos):
        verAlunos.setObjectName("verAlunos")
        verAlunos.resize(370, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(verAlunos.sizePolicy().hasHeightForWidth())
        verAlunos.setSizePolicy(sizePolicy)
        verAlunos.setMinimumSize(QtCore.QSize(370, 380))
        verAlunos.setMaximumSize(QtCore.QSize(370, 380))
        self.centralwidget = QtWidgets.QWidget(verAlunos)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background-color:  rgb(21, 143, 181);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 350, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.table.setFont(font)
        self.table.setStyleSheet("QHeaderView::section {\n"
"border: 2px solid rgb(255, 123, 28);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"font-size: 12px;\n"
" }\n"
"\n"
"QTableView {\n"
"background-color: #fff;\n"
"selection-background-color: rgb(255, 123, 28);\n"
"selection-color: #fff;\n"
"color: rgb(255, 123, 28); }")
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setCornerButtonEnabled(False)
        self.table.setObjectName("table")
        self.table.verticalHeader().setVisible(False)
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(12, 338, 123, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVoltar.sizePolicy().hasHeightForWidth())
        self.btnVoltar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnVoltar.setFont(font)
        self.btnVoltar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnVoltar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnVoltar.setStyleSheet("border: 2px solid rgb(255, 123, 28);;\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 123, 28);\n"
"color: #fff;\n"
"")
        self.btnVoltar.setObjectName("btnVoltar")
        self.tableAlunos = QtWidgets.QTableView(self.centralwidget)
        self.tableAlunos.setGeometry(QtCore.QRect(10, 10, 351, 311))
        self.tableAlunos.verticalHeader().setVisible(False)
        self.tableAlunos.setStyleSheet("QHeaderView::section {\n"
        "border: 2px solid rgb(255, 123, 28);\n"
        "border-radius: 15px;\n"
        "background-color: rgb(255, 123, 28);\n"
        "color: #fff;\n"
        "font-size: 12px;\n"
        " }\n"
        "\n"
        "QTableView {\n"
        "background-color: #fff;\n"
        "selection-background-color: rgb(255, 123, 28);\n"
        "selection-color: #fff;\n"
        "color: rgb(255, 123, 28); }")
        self.tableAlunos.setFont(font)
        verAlunos.setCentralWidget(self.centralwidget)
        self.retranslateUi(verAlunos)
        QtCore.QMetaObject.connectSlotsByName(verAlunos)

    def retranslateUi(self, verAlunos):
        _translate = QtCore.QCoreApplication.translate
        verAlunos.setWindowTitle(_translate("verAlunos", "Alunos"))
        self.btnVoltar.setText(_translate("verAlunos", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verAlunos = QtWidgets.QMainWindow()
    ui = Ui_verAlunos()
    ui.setupUi(verAlunos)
    verAlunos.show()
    sys.exit(app.exec_())
