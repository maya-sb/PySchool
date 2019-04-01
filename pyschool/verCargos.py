import sys
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from database.database import Database
from interface.verCargosWindow import *

import cadastroCargo
import homeServidor
import homeAdm


# tela
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
tela = Ui_verCargos()
tela.setupUi(MainWindow)


def cadastrarCargos(id):
	cadastroCargo.startCadastroCargo(id)

def voltarHome(id):
	MainWindow.close()
	homeAdm.startHomeAdm(id)

def adicionarCargos():

	# SELECT AQUI PARA ME RETORNAR A LISTA DE TODOS OS CARGOS
    cargos = ["professor", "adm", "secretário"]

    for cargo in cargos:
        tela.model.appendRow(QStandardItem(cargo))

def startCargos(id):

    # Configurar tabela
    tela.model = QStandardItemModel()  
    tela.tableCargos.setModel(tela.model)
    tela.model.setHorizontalHeaderLabels(['Cargos'])
    #tela.tableCargos.setSelectionBehavior(QAbstractItemView.SelectRows)
    tela.tableCargos.setColumnWidth(0, 350)
    adicionarCargos()

    # Cadastrar Cargo
    tela.btnCargo.clicked.connect(partial(cadastrarCargos, id))

    # Voltar
    tela.btnVoltar.clicked.connect(partial(voltarHome, id))


    # run
    MainWindow.show()
