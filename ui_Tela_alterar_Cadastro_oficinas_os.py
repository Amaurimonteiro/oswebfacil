# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\os_system\Tela_alterar_Cadastro_oficinas_os.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_altera_Cadastro_oficinas_os(object):
    def setupUi(self, Tela_altera_Cadastro_oficinas_os):
        Tela_altera_Cadastro_oficinas_os.setObjectName("Tela_altera_Cadastro_oficinas_os")
        Tela_altera_Cadastro_oficinas_os.resize(786, 733)
        Tela_altera_Cadastro_oficinas_os.setLayoutDirection(QtCore.Qt.LeftToRight)
        Tela_altera_Cadastro_oficinas_os.setStyleSheet("background-color: rgb(0, 85, 255);")
        Tela_altera_Cadastro_oficinas_os.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        Tela_altera_Cadastro_oficinas_os.setDocumentMode(False)
        Tela_altera_Cadastro_oficinas_os.setDockNestingEnabled(True)
        Tela_altera_Cadastro_oficinas_os.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.ForceTabbedDocks)
        self.centralwidget = QtWidgets.QWidget(Tela_altera_Cadastro_oficinas_os)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 811, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pb_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cadastrar.setGeometry(QtCore.QRect(467, 598, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pb_cadastrar.setFont(font)
        self.pb_cadastrar.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pb_cadastrar.setObjectName("pb_cadastrar")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(214, 120, 421, 41))
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
        self.pb_cadastrar_2.setGeometry(QtCore.QRect(58, 598, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pb_cadastrar_2.setFont(font)
        self.pb_cadastrar_2.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pb_cadastrar_2.setObjectName("pb_cadastrar_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(214, 315, 421, 41))
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
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(214, 265, 421, 41))
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(214, 167, 421, 40))
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
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(214, 363, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_4.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(24, 124, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(34, 171, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(32, 269, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(34, 320, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(37, 368, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 419, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(7, 523, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setEnabled(True)
        self.lineEdit_9.setGeometry(QtCore.QRect(215, 520, 421, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
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
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_9.setClearButtonEnabled(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(215, 467, 421, 41))
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
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setClearButtonEnabled(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(216, 414, 421, 41))
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
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setClearButtonEnabled(False)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 473, 190, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(215, 215, 421, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_5.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;")
        self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(35, 219, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        Tela_altera_Cadastro_oficinas_os.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_altera_Cadastro_oficinas_os)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 26))
        self.menubar.setObjectName("menubar")
        Tela_altera_Cadastro_oficinas_os.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(Tela_altera_Cadastro_oficinas_os)
        self.statusBar.setObjectName("statusBar")
        Tela_altera_Cadastro_oficinas_os.setStatusBar(self.statusBar)

        self.retranslateUi(Tela_altera_Cadastro_oficinas_os)
        QtCore.QMetaObject.connectSlotsByName(Tela_altera_Cadastro_oficinas_os)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.lineEdit_1, self.lineEdit)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.lineEdit, self.lineEdit_3)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.lineEdit_3, self.lineEdit_2)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.lineEdit_2, self.lineEdit_4)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.lineEdit_4, self.lineEdit_8)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.lineEdit_8, self.lineEdit_7)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.lineEdit_7, self.lineEdit_9)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.lineEdit_9, self.pb_cadastrar)
        Tela_altera_Cadastro_oficinas_os.setTabOrder(self.pb_cadastrar, self.pb_cadastrar_2)

    def retranslateUi(self, Tela_altera_Cadastro_oficinas_os):
        _translate = QtCore.QCoreApplication.translate
        Tela_altera_Cadastro_oficinas_os.setWindowTitle(_translate("Tela_altera_Cadastro_oficinas_os", "Tela de Alteração de Cadastro de Oficinas"))
        self.label.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Altere os campos abaixo para"))
        self.pb_cadastrar.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Gravar Alteração"))
        self.lineEdit_1.setPlaceholderText(_translate("Tela_altera_Cadastro_oficinas_os", "Digite nome do Responsável"))
        self.pb_cadastrar_2.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Voltar Para Menu Principal"))
        self.label_2.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Alterar Cadastro da Oficina"))
        self.lineEdit_2.setPlaceholderText(_translate("Tela_altera_Cadastro_oficinas_os", "Digite o Estado da Oficina"))
        self.lineEdit_3.setPlaceholderText(_translate("Tela_altera_Cadastro_oficinas_os", "Digite a Cidade da Oficina"))
        self.lineEdit.setPlaceholderText(_translate("Tela_altera_Cadastro_oficinas_os", "Digite o Endereço da Oficina"))
        self.lineEdit_4.setInputMask(_translate("Tela_altera_Cadastro_oficinas_os", "NNNNN-NNN"))
        self.lineEdit_4.setText(_translate("Tela_altera_Cadastro_oficinas_os", "-"))
        self.lineEdit_4.setPlaceholderText(_translate("Tela_altera_Cadastro_oficinas_os", "Digite o cep da oficina"))
        self.label_3.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Responsavel Oficina:"))
        self.label_4.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Endereço:"))
        self.label_5.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Cidade:"))
        self.label_6.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Estado:"))
        self.label_7.setText(_translate("Tela_altera_Cadastro_oficinas_os", "CEP:"))
        self.label_12.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Telefone Oficina:"))
        self.label_13.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Email Oficina:"))
        self.lineEdit_7.setInputMask(_translate("Tela_altera_Cadastro_oficinas_os", "\\(NN\\)NNNNN-NNNN"))
        self.lineEdit_7.setText(_translate("Tela_altera_Cadastro_oficinas_os", "()-"))
        self.lineEdit_8.setInputMask(_translate("Tela_altera_Cadastro_oficinas_os", "\\(NN\\)NNNNN-NNNN"))
        self.lineEdit_8.setText(_translate("Tela_altera_Cadastro_oficinas_os", "()-"))
        self.label_14.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Whatsapp Oficina:"))
        self.lineEdit_5.setPlaceholderText(_translate("Tela_altera_Cadastro_oficinas_os", "Digite o Bairro da Oficina"))
        self.label_8.setText(_translate("Tela_altera_Cadastro_oficinas_os", "Bairro:"))
