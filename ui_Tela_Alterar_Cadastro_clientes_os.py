# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\os_system\Tela_Alterar_Cadastro_clientes_os.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Altera_Cadastro_cliente_os(object):
    def setupUi(self, Tela_Altera_Cadastro_cliente_os):
        Tela_Altera_Cadastro_cliente_os.setObjectName("Tela_Altera_Cadastro_cliente_os")
        Tela_Altera_Cadastro_cliente_os.resize(965, 926)
        Tela_Altera_Cadastro_cliente_os.setMouseTracking(True)
        Tela_Altera_Cadastro_cliente_os.setTabletTracking(True)
        Tela_Altera_Cadastro_cliente_os.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Tela_Altera_Cadastro_cliente_os.setStyleSheet("background-color: rgb(0, 85, 255);")
        Tela_Altera_Cadastro_cliente_os.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        Tela_Altera_Cadastro_cliente_os.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(Tela_Altera_Cadastro_cliente_os)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(224, 260, 571, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(224, 210, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pb_grava_alt_cli = QtWidgets.QPushButton(self.centralwidget)
        self.pb_grava_alt_cli.setGeometry(QtCore.QRect(700, 798, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pb_grava_alt_cli.setFont(font)
        self.pb_grava_alt_cli.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pb_grava_alt_cli.setObjectName("pb_grava_alt_cli")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(224, 310, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_1.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_1.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_1.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_1.setText("")
        self.lineEdit_1.setClearButtonEnabled(False)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.pb_cadastrar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cadastrar_2.setGeometry(QtCore.QRect(120, 800, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pb_cadastrar_2.setFont(font)
        self.pb_cadastrar_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pb_cadastrar_2.setObjectName("pb_cadastrar_2")
        self.rb_cnpj = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_cnpj.setGeometry(QtCore.QRect(420, 180, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb_cnpj.setFont(font)
        self.rb_cnpj.setStyleSheet("color: rgb(255, 255, 255);")
        self.rb_cnpj.setChecked(True)
        self.rb_cnpj.setObjectName("rb_cnpj")
        self.rb_cpf = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_cpf.setGeometry(QtCore.QRect(537, 182, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rb_cpf.setFont(font)
        self.rb_cpf.setStyleSheet("color: rgb(255, 255, 255);")
        self.rb_cpf.setObjectName("rb_cpf")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 871, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(225, 360, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_3.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_3.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(226, 460, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_4.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_4.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(225, 511, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_5.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_5.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(224, 562, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_6.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_6.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 901, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 901, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(18, 265, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(19, 315, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(16, 216, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(21, 366, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 465, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 517, 190, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(17, 567, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(225, 668, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_7.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_7.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_7.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_7.setClearButtonEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 620, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(226, 615, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_8.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_8.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_8.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_8.setClearButtonEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(17, 724, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 674, 190, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(225, 721, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_9.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_9.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_9.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_9.setInputMask("")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setClearButtonEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pb_consulta = QtWidgets.QPushButton(self.centralwidget)
        self.pb_consulta.setGeometry(QtCore.QRect(820, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pb_consulta.setFont(font)
        self.pb_consulta.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pb_consulta.setObjectName("pb_consulta")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(224, 410, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_10.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_10.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_10.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lineEdit_10.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_10.setText("")
        self.lineEdit_10.setClearButtonEnabled(False)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 416, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        Tela_Altera_Cadastro_cliente_os.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Altera_Cadastro_cliente_os)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 26))
        self.menubar.setObjectName("menubar")
        Tela_Altera_Cadastro_cliente_os.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(Tela_Altera_Cadastro_cliente_os)
        self.statusBar.setObjectName("statusBar")
        Tela_Altera_Cadastro_cliente_os.setStatusBar(self.statusBar)

        self.retranslateUi(Tela_Altera_Cadastro_cliente_os)
        QtCore.QMetaObject.connectSlotsByName(Tela_Altera_Cadastro_cliente_os)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_2, self.lineEdit)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit, self.lineEdit_1)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_1, self.lineEdit_3)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_3, self.lineEdit_10)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_10, self.lineEdit_4)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_6, self.lineEdit_8)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_8, self.lineEdit_7)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_7, self.lineEdit_9)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.lineEdit_9, self.pb_cadastrar_2)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.pb_cadastrar_2, self.rb_cpf)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.rb_cpf, self.pb_consulta)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.pb_consulta, self.rb_cnpj)
        Tela_Altera_Cadastro_cliente_os.setTabOrder(self.rb_cnpj, self.pb_grava_alt_cli)

    def retranslateUi(self, Tela_Altera_Cadastro_cliente_os):
        _translate = QtCore.QCoreApplication.translate
        Tela_Altera_Cadastro_cliente_os.setWindowTitle(_translate("Tela_Altera_Cadastro_cliente_os", "Tela de Alteração de Cadastro de Clientes"))
        self.label.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Preencha os campos abaixo para"))
        self.lineEdit.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o nome do Cliente - Loja"))
        self.lineEdit_2.setInputMask(_translate("Tela_Altera_Cadastro_cliente_os", "NN.NNN.NNN/NNNN-NN"))
        self.lineEdit_2.setText(_translate("Tela_Altera_Cadastro_cliente_os", "../-"))
        self.lineEdit_2.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o Número do Documento"))
        self.pb_grava_alt_cli.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Gravar"))
        self.lineEdit_1.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite nome do Responsável da Loja"))
        self.pb_cadastrar_2.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Voltar Para Lista de Clientes"))
        self.rb_cnpj.setText(_translate("Tela_Altera_Cadastro_cliente_os", "CNPJ"))
        self.rb_cpf.setText(_translate("Tela_Altera_Cadastro_cliente_os", "CPF"))
        self.label_2.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Alterar do Cliente"))
        self.lineEdit_3.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o Endereço do Cliente"))
        self.lineEdit_4.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite a Cidade do Cliente"))
        self.lineEdit_5.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o Estado do Cliente"))
        self.lineEdit_6.setInputMask(_translate("Tela_Altera_Cadastro_cliente_os", "NNNNN-NNN"))
        self.lineEdit_6.setText(_translate("Tela_Altera_Cadastro_cliente_os", "-"))
        self.lineEdit_6.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o Cep do Cliente"))
        self.label_5.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Nome da Loja:"))
        self.label_6.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Responsável da Loja:"))
        self.label_7.setText(_translate("Tela_Altera_Cadastro_cliente_os", "CNPJ ou CPF:"))
        self.label_8.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Endereço\':"))
        self.label_9.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Cidade:"))
        self.label_10.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Estado:"))
        self.label_11.setText(_translate("Tela_Altera_Cadastro_cliente_os", "CEP:"))
        self.lineEdit_7.setInputMask(_translate("Tela_Altera_Cadastro_cliente_os", "\\(NN\\)NNNNN-NNNN"))
        self.lineEdit_7.setText(_translate("Tela_Altera_Cadastro_cliente_os", "()-"))
        self.lineEdit_7.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o Email do Cliente"))
        self.label_12.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Telefone Loja:"))
        self.lineEdit_8.setInputMask(_translate("Tela_Altera_Cadastro_cliente_os", "\\(NN\\)NNNNN-NNNN"))
        self.lineEdit_8.setText(_translate("Tela_Altera_Cadastro_cliente_os", "()-"))
        self.lineEdit_8.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o Email do Cliente"))
        self.label_13.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Email Loja:"))
        self.label_14.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Whatsapp Loja:"))
        self.lineEdit_9.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o Email do Cliente"))
        self.pb_consulta.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Consulta"))
        self.lineEdit_10.setPlaceholderText(_translate("Tela_Altera_Cadastro_cliente_os", "Digite o Bairro do Cliente"))
        self.label_15.setText(_translate("Tela_Altera_Cadastro_cliente_os", "Bairro:"))
