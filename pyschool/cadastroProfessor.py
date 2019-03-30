import sys
import os.path
import shutil

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from interface.escolherMateriasDialog import *
#from pyschool.interface.escolherMateriasDialog import *
from database import database
#from pyschool.database import database
from interface.cadastroProfessorWindow import *
#from pyschool.interface.cadastroProfessorWindow import *
from endereco import *
#from pyschool.endereco import *
from professor import *
#from pyschool.professor import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_cadastroProfessor()
tela.setupUi(MainWindow)

Dialog = QtWidgets.QDialog()
dialog = Ui_Dialog()
dialog.setupUi(Dialog)

def confirmarMaterias():

    index = dialog.layout.count()
    itens = []
    for x in range(index):
        itens.append(dialog.layout.itemAt(x).widget())

    materias_selecionadas = []

    for x in itens:
        if x.isChecked():
            materias_selecionadas.append(x.text())
    Dialog.close()

    tela.lineMaterias.setText(", ".join(materias_selecionadas))
    global materias_confirmadas
    materias_confirmadas = materias_selecionadas

def escolherMaterias():

    materias = database.mostrarMaterias()

    for i, v in enumerate(materias):
        materias[i] = QCheckBox(v)
        materias[i].setStyleSheet("font: 25 15pt \"Malgun Gothic Semilight\";\n")
        dialog.layout.addWidget(materias[i])

    dialog.btnConfirmar.clicked.connect(confirmarMaterias)

    Dialog.show()
    Dialog.exec_()

def carregarFoto(event):

    global foto
    image = QFileDialog.getOpenFileName(None, 'Escolher foto', '', "Images(*.png *.jpeg *.jpg)")
    imagePath = image[0]

    if image[0] != "":
        pixmap = QPixmap(imagePath)

        #Salvando na pasta
        nome_arquivo = imagePath.split("/")[-1]

        # Pegar o endereço da pessoa + a pasta do projeto
        url = "/database/images/"
        urlCompleta = os.path.dirname(os.path.abspath(__file__)) + url

        # Tratando existência
        repetido = False
        cont = 1
        while os.path.exists(urlCompleta + nome_arquivo):
            repetido = True
            nome_arquivo = nome_arquivo.split(".")
            if cont == 1:
                nome_arquivo = nome_arquivo[0] + "({})".format(cont) + "." + nome_arquivo[-1]
            else:
                nome_arquivo = nome_arquivo[0][:-3] + "({})".format(cont) + "." + nome_arquivo[-1]
            cont += 1

        # Copia a imagem para a url dada
        if repetido:
            shutil.copy(imagePath, os.path.join(urlCompleta, nome_arquivo))
        else:
            shutil.copy(imagePath, urlCompleta)

        #Setando foto no label
        foto = os.path.join(urlCompleta, nome_arquivo)
        new_pixmap = QPixmap(os.path.join(urlCompleta, nome_arquivo))
        new_pixmap = new_pixmap.scaled(150, 180, QtCore.Qt.IgnoreAspectRatio)
        tela.lblFoto.setPixmap(new_pixmap)

def cadastrarProfessor():
    endereco = Endereco(tela.lineRua.text(),tela.lineBairro.text(),tela.spinNumero.text(),tela.lineCep.text(),
                        tela.lineCidade.text(),tela.cbEstado.currentText())
    database.inserirEndereco(endereco)

    id_endereco = database.retornarUltimoId("endereco")

    professor = Professor(tela.lineNome.text(),tela.dateNascimento.text(),tela.cbSexo.currentText(),tela.lineRg.text(),
                        tela.lineCpf.text(),tela.lineTelefone.text(),id_endereco, tela.lineEmail.text(),tela.lineSenha.text(),tela.cbEstadoCivil.currentText(),
                        foto,materias_confirmadas)
    database.inserirProfessor(professor)


    id_professor = database.retornarUltimoId("professor")
    database.inserirEnsino(id_professor, materias_confirmadas)

    tela.lineNome.setText("")
    tela.cbSexo.setCurrentIndex(0)
    tela.lineRg.setText("")
    tela.lineCpf.setText("")
    tela.lineTelefone.setText("")
    tela.lineRua.setText("")
    tela.lineBairro.setText("")
    tela.spinNumero.setValue(0)
    tela.lineCep.setText("")
    tela.lineCidade.setText("")
    tela.cbEstado.setCurrentIndex(0)
    tela.lineEmail.setText("")
    tela.lineSenha.setText("")
    tela.cbEstadoCivil.setCurrentIndex(0)
    definirIcone()
    tela.lineMaterias.setText("")

#Definir ícone inicial
def definirIcone():
    global foto
    pixmap = QPixmap(os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png")
    tela.lblFoto.setText(os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png")
    new_pixmap = pixmap.scaled(120, 110, QtCore.Qt.IgnoreAspectRatio)
    tela.lblFoto.setPixmap(new_pixmap)
    foto = os.path.dirname(os.path.abspath(__file__))+"/interface/icons/perfil.png"

#Definindo ícone inicial
definirIcone()

#Evento de carregar foto
tela.lblFoto.mousePressEvent = carregarFoto

#Botão cadastrar acionado
tela.btnCadatrar.clicked.connect(cadastrarProfessor)

#Botão matérias acionado
tela.btnMaterias.clicked.connect(escolherMaterias)

MainWindow.show()
sys.exit(app.exec_())