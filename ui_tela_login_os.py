# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\os_system\tela_login_os.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Login_OS(object):
    def setupUi(self, Tela_Login_OS):
        Tela_Login_OS.setObjectName("Tela_Login_OS")
        Tela_Login_OS.setWindowModality(QtCore.Qt.NonModal)
        Tela_Login_OS.setEnabled(True)
        Tela_Login_OS.resize(602, 551)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Tela_Login_OS.sizePolicy().hasHeightForWidth())
        Tela_Login_OS.setSizePolicy(sizePolicy)
        Tela_Login_OS.setToolTipDuration(0)
        Tela_Login_OS.setAutoFillBackground(False)
        Tela_Login_OS.setStyleSheet("background-color: rgb(0, 170, 255);")
        Tela_Login_OS.setWindowFilePath("")
        Tela_Login_OS.setAnimated(True)
        Tela_Login_OS.setTabShape(QtWidgets.QTabWidget.Rounded)
        Tela_Login_OS.setDockNestingEnabled(True)
        Tela_Login_OS.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        Tela_Login_OS.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Tela_Login_OS)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_login = QtWidgets.QPushButton(self.centralwidget)
        self.pb_login.setGeometry(QtCore.QRect(140, 314, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pb_login.setFont(font)
        self.pb_login.setStyleSheet("background-color: rgb(46, 255, 242);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pb_login.setObjectName("pb_login")
        self.le_login = QtWidgets.QLineEdit(self.centralwidget)
        self.le_login.setGeometry(QtCore.QRect(170, 99, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.le_login.setFont(font)
        self.le_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.le_login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.le_login.setObjectName("le_login")
        self.le_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.le_senha.setGeometry(QtCore.QRect(170, 185, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.le_senha.setFont(font)
        self.le_senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.le_senha.setObjectName("le_senha")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 460, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pb_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cadastrar.setGeometry(QtCore.QRect(294, 450, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pb_cadastrar.setFont(font)
        self.pb_cadastrar.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pb_cadastrar.setObjectName("pb_cadastrar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 99, 41, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\os_system\\usuario.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 185, 51, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\os_system\\cadeado.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 127);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pb_sair = QtWidgets.QPushButton(self.centralwidget)
        self.pb_sair.setGeometry(QtCore.QRect(350, 314, 121, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_sair.sizePolicy().hasHeightForWidth())
        self.pb_sair.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pb_sair.setFont(font)
        self.pb_sair.setStyleSheet("background-color: rgb(46, 255, 242);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pb_sair.setObjectName("pb_sair")
        self.rb_cnpj = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_cnpj.setGeometry(QtCore.QRect(220, 20, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb_cnpj.setFont(font)
        self.rb_cnpj.setStyleSheet("color: rgb(255, 255, 255);")
        self.rb_cnpj.setChecked(True)
        self.rb_cnpj.setObjectName("rb_cnpj")
        self.rb_cpf = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_cpf.setGeometry(QtCore.QRect(340, 20, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb_cpf.setFont(font)
        self.rb_cpf.setStyleSheet("color: rgb(255, 255, 255);")
        self.rb_cpf.setObjectName("rb_cpf")
        self.label_3.raise_()
        self.label_2.raise_()
        self.pb_login.raise_()
        self.le_login.raise_()
        self.le_senha.raise_()
        self.label.raise_()
        self.pb_cadastrar.raise_()
        self.label_4.raise_()
        self.pb_sair.raise_()
        self.rb_cnpj.raise_()
        self.rb_cpf.raise_()
        Tela_Login_OS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Login_OS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        Tela_Login_OS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Login_OS)
        self.statusbar.setObjectName("statusbar")
        Tela_Login_OS.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Login_OS)
        QtCore.QMetaObject.connectSlotsByName(Tela_Login_OS)
        Tela_Login_OS.setTabOrder(self.le_login, self.le_senha)
        Tela_Login_OS.setTabOrder(self.le_senha, self.pb_login)
        Tela_Login_OS.setTabOrder(self.pb_login, self.pb_cadastrar)
        Tela_Login_OS.setTabOrder(self.pb_cadastrar, self.pb_sair)
        Tela_Login_OS.setTabOrder(self.pb_sair, self.rb_cnpj)
        Tela_Login_OS.setTabOrder(self.rb_cnpj, self.rb_cpf)

    def retranslateUi(self, Tela_Login_OS):
        _translate = QtCore.QCoreApplication.translate
        Tela_Login_OS.setWindowTitle(_translate("Tela_Login_OS", "Tela de Login Sistema de Os"))
        self.pb_login.setText(_translate("Tela_Login_OS", "LOGIN"))
        self.le_login.setToolTip(_translate("Tela_Login_OS", "<html><head/><body><p><br/></p></body></html>"))
        self.le_login.setPlaceholderText(_translate("Tela_Login_OS", "Login "))
        self.le_senha.setPlaceholderText(_translate("Tela_Login_OS", "Senha"))
        self.label.setText(_translate("Tela_Login_OS", "Não é cadastrado?"))
        self.pb_cadastrar.setText(_translate("Tela_Login_OS", "Cadastrar Oficina"))
        self.pb_sair.setText(_translate("Tela_Login_OS", "Sair"))
        self.rb_cnpj.setText(_translate("Tela_Login_OS", "CNPJ"))
        self.rb_cpf.setText(_translate("Tela_Login_OS", "CPF"))
