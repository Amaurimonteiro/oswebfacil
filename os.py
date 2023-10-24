# pip install mysql
# python.exe -m pip install --upgrade pip
# pip install mysql.connector
# pip install requests
# pip install json
# pip install pyqt5

# pip install typing_extensions
# pip install reportlab

# pip install pyinstaller
# pyinstaller --onefile -w oswebfacil.py
# pyinstaller os.py
# cp.bat
# virtualenv oswebfacil
# oswebfacil/Scripts/Activate


from datetime import datetime
import mysql.connector
import requests
import json
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from typing_extensions import Self
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


numero_id = 0

'''
banco_hostnet = mysql.connector.connect(
    host='web149.f1.k8.com.br',  # '187.73.33.17',
    user="fremondata",
    passwd="Am1324br",
    database="fremondata"
)
'''

banco = mysql.connector.connect(
    host='br942.hostgator.com.br',  
    user="oswebf62_amaurism",
    passwd="Am1324br10",
    database="oswebf62_os"
)


'''
numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="curso_python"
)
'''

# 47.309.174/0002-85 micheletti
# 43.776.517/0001-80 sabesp
# 61.695.227/0001-93 Eletropaulo
# 08.726.829/0001-88 Padaria

def mm2p(milimetros):
    return milimetros / 0.352777


def gerar_pdf_os():

    global v_num_os

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cad_os WHERE num_os = '{}'".format(v_num_os)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)


    y = 0
    pdf = canvas.Canvas("pdf_os_nova.pdf",pagesize=A4)

    pdf.setLineWidth(0.5)
    pdf.setFont("Times-Bold", 14)

    #pdf.circle(mm2p(100),mm2p(150),mm2p(100))
    #pdf.line(mm2p(100),mm2p(150),mm2p(100),mm2p(150))
    
    # Ultima linha
    pdf.setFont("Times-Bold", 10)
    pdf.rect(mm2p(5),mm2p(5),mm2p(66),mm2p(13))
    pdf.rect(mm2p(71),mm2p(5),mm2p(67),mm2p(13))
    pdf.rect(mm2p(138),mm2p(5),mm2p(67),mm2p(13))
    pdf.drawString(mm2p(13),mm2p(14), "Informações para Nota Fiscal")
    pdf.drawString(mm2p(81),mm2p(14), "Nota Fiscal - Data de Emissão")
    pdf.drawString(mm2p(139),mm2p(14), "TOTAL GERAL")
    
    # Declaro estar Ciente
    pdf.setFont("Times-Bold", 12)
    pdf.drawString(mm2p(19),mm2p(30), "Declaro estar ciente de que todas as informações contidas nesta Ordem de Serviço são verídicas.")
    pdf.rect(mm2p(5),mm2p(18),mm2p(200),mm2p(16))
    
    pdf.drawString(mm2p(7),mm2p(19), "Nome do Cliente:")
    pdf.drawString(mm2p(135),mm2p(19), "Data:")

    pdf.drawString(mm2p(7),mm2p(36), "Local/Data:")
    pdf.drawString(mm2p(120),mm2p(36), "TOTAL MÃO DE OBRA:")

    pdf.drawString(mm2p(7),mm2p(44), "Técnico:")
    pdf.drawString(mm2p(90),mm2p(44), "RG:")
    pdf.drawString(mm2p(138),mm2p(44), "TOTAL PEÇAS:")
    pdf.line(mm2p(5),mm2p(43),mm2p(205),mm2p(43))

    pdf.setFont("Times-Bold", 14)
    pdf.drawString(mm2p(97),mm2p(87), "Lista de Peças")
    pdf.setFont("Times-Bold", 12)
    pdf.drawString(mm2p(7),mm2p(82), "Código           Quant.          Descrição                                                                                R$ Unitário       R$ Total")
    pdf.rect(mm2p(5),mm2p(50),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(56),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(62),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(68),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(74),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(80),mm2p(200),mm2p(6))

    pdf.rect(mm2p(30),mm2p(50),mm2p(24),mm2p(36))
    pdf.rect(mm2p(154),mm2p(50),mm2p(29),mm2p(36))

    #pdf.rect(mm2p(5),mm2p(94),mm2p(200),mm2p(7))

    pdf.setFont("Times-Bold", 11)
    pdf.rect(mm2p(5),mm2p(93),mm2p(200),mm2p(6))
    pdf.drawString(mm2p(12),mm2p(95), "*** Cuidado ao transportar o Equipamento para não desregular, pois não cobrimos GARANTIA nesse caso. ***")
    
    pdf.rect(mm2p(5),mm2p(99),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(105),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(111),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(117),mm2p(200),mm2p(6))
    pdf.setFont("Times-Bold", 13)
    pdf.drawString(mm2p(8),mm2p(118), "Observações:")

    pdf.rect(mm2p(5),mm2p(124),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(130),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(136),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(142),mm2p(200),mm2p(6))
    pdf.setFont("Times-Bold", 13)
    pdf.drawString(mm2p(8),mm2p(143), "Medidas Corretivas:")

    pdf.rect(mm2p(5),mm2p(149),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(155),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(161),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(167),mm2p(200),mm2p(6))
    pdf.drawString(mm2p(8),mm2p(168), "Defeito Constatado:")

    pdf.rect(mm2p(5),mm2p(174),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(180),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(186),mm2p(200),mm2p(6))
    pdf.rect(mm2p(5),mm2p(192),mm2p(200),mm2p(6))
    pdf.drawString(mm2p(8),mm2p(193), "Defeito Informado:")


    pdf.setFont("Times-Bold", 10)
    pdf.rect(mm2p(5),mm2p(199),mm2p(200),mm2p(11))
    pdf.rect(mm2p(30),mm2p(199),mm2p(24),mm2p(11))
    pdf.rect(mm2p(86),mm2p(199),mm2p(32),mm2p(11))
    pdf.rect(mm2p(160),mm2p(199),mm2p(45),mm2p(11))

    pdf.drawString(mm2p(6),mm2p(206), "H. Entrada")
    pdf.drawString(mm2p(31),mm2p(206), "H. Saída")
    pdf.drawString(mm2p(55),mm2p(206), "Nº Lacre Antigo")
    pdf.drawString(mm2p(87),mm2p(206), "Nº Lacre Atual")
    pdf.drawString(mm2p(119),mm2p(206), "Selo Reparado Antigo")
    pdf.drawString(mm2p(161),mm2p(206), "Selo Reparado Atual")
    
    pdf.setFont("Times-Bold", 10)
    pdf.rect(mm2p(5),mm2p(211),mm2p(200),mm2p(13))
    pdf.drawString(mm2p(6),mm2p(220), "Equip. Fabricante:")
    pdf.drawString(mm2p(84),mm2p(220), "Modelo:")
    pdf.drawString(mm2p(149),mm2p(220), "Portaria:")
    pdf.line(mm2p(5),mm2p(217),mm2p(205),mm2p(217))

    pdf.drawString(mm2p(6),mm2p(213), "Nº de Série:")
    pdf.drawString(mm2p(84),mm2p(213), "Carga Max.:")
    pdf.drawString(mm2p(149),mm2p(213), "Divisão:")
    pdf.rect(mm2p(83),mm2p(211),mm2p(65),mm2p(13))

    pdf.drawString(mm2p(6),mm2p(227), "Hora Técnica:")
    pdf.drawString(mm2p(84),mm2p(227), "Tempo Gasto:")
    pdf.drawString(mm2p(149),mm2p(227), "Inventário:")
    pdf.rect(mm2p(5),mm2p(225),mm2p(200),mm2p(6))


    pdf.setFont("Times-Bold", 12)
    pdf.rect(mm2p(5),mm2p(232),mm2p(200),mm2p(34))

    pdf.drawString(mm2p(6),mm2p(260), "Razão Social:")
    pdf.drawString(mm2p(120),mm2p(260), "CNPJ/CPF:")
    pdf.line(mm2p(5),mm2p(259),mm2p(205),mm2p(259))

    pdf.drawString(mm2p(6),mm2p(253), "Endereço:")
    pdf.drawString(mm2p(120),mm2p(253), "Cidade:")
    pdf.drawString(mm2p(170),mm2p(253), "UF:")
    pdf.line(mm2p(5),mm2p(252),mm2p(205),mm2p(252))

    pdf.drawString(mm2p(6),mm2p(246), "Bairro:")
    pdf.drawString(mm2p(100),mm2p(246), "I.E./R.G.:")
    pdf.drawString(mm2p(170),mm2p(246), "CEP:")
    pdf.line(mm2p(5),mm2p(245),mm2p(205),mm2p(245))

    pdf.drawString(mm2p(6),mm2p(239), "Fone:")
    pdf.drawString(mm2p(100),mm2p(239), "Email:")
    pdf.line(mm2p(5),mm2p(238),mm2p(205),mm2p(238))

    pdf.drawString(mm2p(6),mm2p(233), "Contato:")

    pdf.drawImage("os_logo_sistema.png",mm2p(5),mm2p(267),width=100,height=79)

    pdf.save()

    mensagem('Aviso:','Pdf Criado com Sucesso')

def digita_quant_1():
    v_txt = tela_abrir_os.le_quant_1.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_abrir_os.le_quant_1.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_abrir_os.le_quant_1.setText(v_txt)

def digita_quant_1_alt():
    v_txt = tela_altera_os.le_quant_1.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_altera_os.le_quant_1.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_altera_os.le_quant_1.setText(v_txt)

def digita_quant_2():
    v_txt = tela_abrir_os.le_quant_2.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_abrir_os.le_quant_2.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_abrir_os.le_quant_2.setText(v_txt)

def digita_quant_2_alt():
    v_txt = tela_altera_os.le_quant_2.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_altera_os.le_quant_2.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_altera_os.le_quant_2.setText(v_txt)

def digita_quant_3():
    v_txt = tela_abrir_os.le_quant_3.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_abrir_os.le_quant_3.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_abrir_os.le_quant_3.setText(v_txt)

def digita_quant_3_alt():
    v_txt = tela_altera_os.le_quant_3.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_altera_os.le_quant_3.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_altera_os.le_quant_3.setText(v_txt)

def digita_quant_4():
    v_txt = tela_abrir_os.le_quant_4.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_abrir_os.le_quant_4.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_abrir_os.le_quant_4.setText(v_txt)

def digita_quant_4_alt():
    v_txt = tela_altera_os.le_quant_4.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_altera_os.le_quant_4.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_altera_os.le_quant_4.setText(v_txt)

def digita_quant_5():
    v_txt = tela_abrir_os.le_quant_5.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_abrir_os.le_quant_5.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_abrir_os.le_quant_5.setText(v_txt)

def digita_quant_5_alt():
    v_txt = tela_altera_os.le_quant_5.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
 
    if(v_txt.isnumeric()):
        tela_altera_os.le_quant_5.setText(v_txt)
    else:
        v_txt = v_txt[0:len(v_txt)-1]
        tela_altera_os.le_quant_5.setText(v_txt)

def digita_valor_1():
    global v_tot_1
    global v_tot_2
    global v_tot_3
    global v_tot_4
    global v_tot_5


    v_txt = tela_abrir_os.le_val_unit_1.text()
    if(v_txt==''):
        tela_abrir_os.le_val_unit_1.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_abrir_os.le_val_unit_1.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_abrir_os.le_quant_1.text()

    if (v_txt.isnumeric()):
        tela_abrir_os.le_val_unit_1.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_abrir_os.le_val_unit_1.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_abrir_os.le_val_unit_1.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_1 = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1+v_tot_2+v_tot_3+v_tot_4+v_tot_5
    tela_abrir_os.le_val_tot_1.setText(format(v_tot_1, ".2f"))
    tela_abrir_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))
    #format(3, ".2f")

def digita_valor_1_alt():
    global v_tot_1_alt
    global v_tot_2_alt
    global v_tot_3_alt
    global v_tot_4_alt
    global v_tot_5_alt

    v_txt = tela_altera_os.le_val_unit_1.text()
    if(v_txt==''):
        tela_altera_os.le_val_unit_1.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_altera_os.le_val_unit_1.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_altera_os.le_quant_1.text()

    if (v_txt.isnumeric()):
        tela_altera_os.le_val_unit_1.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_altera_os.le_val_unit_1.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_altera_os.le_val_unit_1.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_1_alt = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1_alt + v_tot_2_alt + v_tot_3_alt + v_tot_4_alt + v_tot_5_alt
    tela_altera_os.le_val_tot_1.setText(format(v_tot_1_alt, ".2f"))
    tela_altera_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))
    #format(3, ".2f")

def digita_valor_2():
    global v_tot_1
    global v_tot_2
    global v_tot_3
    global v_tot_4
    global v_tot_5
    v_txt = tela_abrir_os.le_val_unit_2.text()
    if(v_txt==''):
        tela_abrir_os.le_val_unit_2.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_abrir_os.le_val_unit_2.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_abrir_os.le_quant_2.text()

    if (v_txt.isnumeric()):
        tela_abrir_os.le_val_unit_2.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_abrir_os.le_val_unit_2.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_abrir_os.le_val_unit_2.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_2 = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1+v_tot_2+v_tot_3+v_tot_4+v_tot_5
    tela_abrir_os.le_val_tot_2.setText(format(v_tot_2, ".2f"))
    tela_abrir_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))

def digita_valor_2_alt():
    global v_tot_1_alt
    global v_tot_2_alt
    global v_tot_3_alt
    global v_tot_4_alt
    global v_tot_5_alt
    v_txt = tela_altera_os.le_val_unit_2.text()
    if(v_txt==''):
        tela_altera_os.le_val_unit_2.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_altera_os.le_val_unit_2.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_altera_os.le_quant_2.text()

    if (v_txt.isnumeric()):
        tela_altera_os.le_val_unit_2.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_altera_os.le_val_unit_2.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_altera_os.le_val_unit_2.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_2_alt = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1_alt+v_tot_2_alt+v_tot_3_alt+v_tot_4_alt+v_tot_5_alt
    tela_altera_os.le_val_tot_2.setText(format(v_tot_2_alt, ".2f"))
    tela_altera_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))

def digita_valor_3():
    global v_tot_1
    global v_tot_2
    global v_tot_3
    global v_tot_4
    global v_tot_5
    v_txt = tela_abrir_os.le_val_unit_3.text()
    if(v_txt==''):
        tela_abrir_os.le_val_unit_3.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_abrir_os.le_val_unit_3.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_abrir_os.le_quant_3.text()

    if (v_txt.isnumeric()):
        tela_abrir_os.le_val_unit_3.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_abrir_os.le_val_unit_3.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_abrir_os.le_val_unit_3.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_3 = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1+v_tot_2+v_tot_3+v_tot_4+v_tot_5
    tela_abrir_os.le_val_tot_3.setText(format(v_tot_3, ".2f"))
    tela_abrir_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))

def digita_valor_3_alt():
    global v_tot_1_alt
    global v_tot_2_alt
    global v_tot_3_alt
    global v_tot_4_alt
    global v_tot_5_alt
    v_txt = tela_altera_os.le_val_unit_3.text()
    if(v_txt==''):
        tela_altera_os.le_val_unit_3.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_altera_os.le_val_unit_3.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_altera_os.le_quant_3.text()

    if (v_txt.isnumeric()):
        tela_altera_os.le_val_unit_3.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_altera_os.le_val_unit_3.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_altera_os.le_val_unit_3.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_3_alt = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1_alt+v_tot_2_alt+v_tot_3_alt+v_tot_4_alt+v_tot_5_alt
    tela_altera_os.le_val_tot_3.setText(format(v_tot_3_alt, ".2f"))
    tela_altera_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))

def digita_valor_4():
    global v_tot_1
    global v_tot_2
    global v_tot_3
    global v_tot_4
    global v_tot_5
    v_txt = tela_abrir_os.le_val_unit_4.text()
    if(v_txt==''):
        tela_abrir_os.le_val_unit_4.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_abrir_os.le_val_unit_4.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_abrir_os.le_quant_4.text()

    if (v_txt.isnumeric()):
        tela_abrir_os.le_val_unit_4.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_abrir_os.le_val_unit_4.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_abrir_os.le_val_unit_4.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_4 = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1+v_tot_2+v_tot_3+v_tot_4+v_tot_5
    tela_abrir_os.le_val_tot_4.setText(format(v_tot_4, ".2f"))
    tela_abrir_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))

def digita_valor_4_alt():
    global v_tot_1_alt
    global v_tot_2_alt
    global v_tot_3_alt
    global v_tot_4_alt
    global v_tot_5_alt
    v_txt = tela_altera_os.le_val_unit_4.text()
    if(v_txt==''):
        tela_altera_os.le_val_unit_4.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_altera_os.le_val_unit_4.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_altera_os.le_quant_4.text()

    if (v_txt.isnumeric()):
        tela_altera_os.le_val_unit_4.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_altera_os.le_val_unit_4.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_altera_os.le_val_unit_4.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_4_alt = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1_alt+v_tot_2_alt+v_tot_3_alt+v_tot_4_alt+v_tot_5_alt
    tela_altera_os.le_val_tot_4.setText(format(v_tot_4_alt, ".2f"))
    tela_altera_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))

def digita_valor_5():
    global v_tot_1
    global v_tot_2
    global v_tot_3
    global v_tot_4
    global v_tot_5
    v_txt = tela_abrir_os.le_val_unit_5.text()
    if(v_txt==''):
        tela_abrir_os.le_val_unit_5.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_abrir_os.le_val_unit_5.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_abrir_os.le_quant_5.text()

    if (v_txt.isnumeric()):
        tela_abrir_os.le_val_unit_5.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_abrir_os.le_val_unit_5.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_abrir_os.le_val_unit_5.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_5 = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1+v_tot_2+v_tot_3+v_tot_4+v_tot_5
    tela_abrir_os.le_val_tot_5.setText(format(v_tot_5, ".2f"))
    tela_abrir_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))

def digita_valor_5_alt():
    global v_tot_1_alt
    global v_tot_2_alt
    global v_tot_3_alt
    global v_tot_4_alt
    global v_tot_5_alt
    v_txt = tela_altera_os.le_val_unit_5.text()
    if(v_txt==''):
        tela_altera_os.le_val_unit_5.setText('')
        v_txt='0'
        return

    if(v_txt=='.'):
        tela_altera_os.le_val_unit_5.setText('0.')
        v_txt='0.'
        return

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")
    v_quant = tela_altera_os.le_quant_5.text()

    if (v_txt.isnumeric()):
        tela_altera_os.le_val_unit_5.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_altera_os.le_val_unit_5.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_altera_os.le_val_unit_5.setText(v_txt)
    
    #if(v_quant.isnumeric() and v_txt.isfloat()):
    v_tot_5_alt = int(v_quant) * float(v_txt)
    v_tot_pecas = v_tot_1_alt+v_tot_2_alt+v_tot_3_alt+v_tot_4_alt+v_tot_5_alt
    tela_altera_os.le_val_tot_5.setText(format(v_tot_5_alt, ".2f"))
    tela_altera_os.le_val_tot_pecas.setText(format(v_tot_pecas,".2f"))

def digita_hora_tec():
    v_txt = tela_abrir_os.le_val_hora_tec.text()
    if(v_txt==''):
        tela_abrir_os.le_val_hora_tec.setText('0')
        v_txt='0'

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")

    if(v_txt.isnumeric()):
        tela_abrir_os.le_val_hora_tec.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_abrir_os.le_val_hora_tec.setText(v_txt)            
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_abrir_os.le_val_hora_tec.setText(v_txt)

def digita_hora_tec_alt():
    v_txt = tela_altera_os.le_val_hora_tec.text()
    if(v_txt==''):
        tela_altera_os.le_val_hora_tec.setText('0')
        v_txt='0'

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")

    if(v_txt.isnumeric()):
        tela_altera_os.le_val_hora_tec.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_altera_os.le_val_hora_tec.setText(v_txt)            
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_altera_os.le_val_hora_tec.setText(v_txt)

def digita_val_mao_de_obra():
    v_txt = tela_abrir_os.le_val_mao_de_obra.text()
    if(v_txt==''):
        tela_abrir_os.le_val_mao_de_obra.setText('0')
        v_txt='0'

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")

    if(v_txt.isnumeric()):
        tela_abrir_os.le_val_mao_de_obra.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_abrir_os.le_val_mao_de_obra.setText(v_txt)            
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_abrir_os.le_val_mao_de_obra.setText(v_txt)

def digita_val_mao_de_obra_alt():
    v_txt = tela_altera_os.le_val_mao_de_obra.text()
    if(v_txt==''):
        tela_altera_os.le_val_mao_de_obra.setText('0')
        v_txt='0'

    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")

    if(v_txt.isnumeric()):
        tela_altera_os.le_val_mao_de_obra.setText(v_txt)
    else:
        if(v_teste > 0 and len(v_txt) <= v_teste + 3):
            tela_altera_os.le_val_mao_de_obra.setText(v_txt)            
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_altera_os.le_val_mao_de_obra.setText(v_txt)

def buscar_cliente():
    global v_cnpj_cpf_cli
    global v_nome_cli

    v_texto = tela_abrir_os.le_buscar_cliente.text()

    cursor = banco.cursor()
    #SELECT * FROM Customers WHERE CustomerName LIKE '%or%';
    v_texto_cnpj = "SELECT cnpj_cpf_cliente,nome_loja FROM cad_cliente WHERE cnpj_cpf_cliente LIKE '%{}%' and cnpj_cpf_oficina = '{}'".format(v_texto,v_login)
    cursor.execute(v_texto_cnpj)
    dados_lidos = cursor.fetchall()
    #print(len(dados_lidos))
    
    if (len(dados_lidos) > 0):
        tela_abrir_os.label_8.setText("Digite todo ou parte do CNPJ ou CPF Cliente Total = '{}'".format(str(len(dados_lidos))))
        tela_abrir_os.cb_texto_buscar_cliente.clear()

        for i in range(0, len(dados_lidos)):            
            tela_abrir_os.cb_texto_buscar_cliente.addItem(dados_lidos[i][0])

        tela_abrir_os.label_8.setText("Digite todo ou parte do CNPJ ou CPF Cliente Total = '{}'".format(str(len(dados_lidos))))
        #tela_abrir_os.cb_texto_buscar_cliente.showPopup()
        #tela_abrir_os.le_texto_buscar_cliente.setText(str(dados_lidos[0][0]))

        #if (len(dados_lidos)==1):
        v_cnpj_cpf_cli = dados_lidos[0][0]
        v_nome_cli = dados_lidos[0][1]

        if (len(dados_lidos) == 1):
            tela_abrir_os.cb_texto_buscar_cliente.clear()
            tela_abrir_os.cb_texto_buscar_cliente.addItem(v_nome_cli)
            tela_abrir_os.le_nome_tecnico.setFocus()
            

    else:
        cursor = banco.cursor()
        #SELECT * FROM Customers WHERE CustomerName LIKE '%or%';
        v_texto_nome = "SELECT nome_loja,cnpj_cpf_cliente FROM cad_cliente WHERE nome_loja LIKE '%{}%' and cnpj_cpf_oficina='{}'".format(v_texto,v_login)
        cursor.execute(v_texto_nome)
        dados_lidos = cursor.fetchall()
        if (len(dados_lidos) == 0):
            tela_abrir_os.cb_texto_buscar_cliente.clear()
            tela_abrir_os.label_8.setText("Digite todo ou parte do CNPJ ou CPF Cliente / Total = '{}' '{}'".format(str(len(dados_lidos)),'Cliente Não Encontrado!'))
            #mensagem('Aviso: ','Cliente Não Encontrado!')
            #print(dados_lidos)
        else:
            tela_abrir_os.label_8.setText("Digite todo ou parte doo CNPJ ou CPF Cliente / Total = '{}'".format(str(len(dados_lidos))))

            tela_abrir_os.cb_texto_buscar_cliente.clear()
            for i in range(0, len(dados_lidos)):            
                tela_abrir_os.cb_texto_buscar_cliente.addItem(dados_lidos[i][0])

            #tela_abrir_os.cb_texto_buscar_cliente.showPopup()    
                

            #tela_abrir_os.label_8.setText("Digite todo ou parte do CNPJ ou CPF Cliente / Total='{}' ".format(str(len(dados_lidos))))
            #print(dados_lidos)
            #tela_abrir_os.le_texto_buscar_cliente.setText(str(dados_lidos[0][0]))

        #if (len(dados_lidos)==1):
        v_cnpj_cpf_cli = dados_lidos[0][1]
        v_nome_cli = dados_lidos[0][0]
        tela_abrir_os.le_nome_tecnico.setFocus()

def converte_data_do_banco(vdata):
    #if (vdata == '0000/00/00'):
    if (vdata == 'None'):
        vdata = '  /  /    '
        return vdata
    else:
        v_ano = vdata[:4]
        v_mes = vdata[5:7]
        v_dia = vdata[8:]
        return v_dia + '/' + v_mes + '/' + v_ano

def converte_data_para_banco(vdata):
    if (vdata == '//'):
        vdata = '00/00/0000'
        return vdata
    else:
        v_ano = vdata[6:]
        v_mes = vdata[3:5]
        v_dia = vdata[:2]
        return v_ano + '/' + v_mes + '/' + v_dia

def gravar_os():
    global v_nome_cli
    global v_cnpj_cpf_cli

    if (v_cnpj_cpf_cli == ''):
        mensagem('Aviso:','Existem Campos Obrigatorios em Branco')
        tela_abrir_os.le_buscar_cliente.setFocus()
        return


    v_data_abertura = converte_data_para_banco(tela_abrir_os.le_data_abertura.text())    
    v_data_fechamento = converte_data_para_banco(tela_abrir_os.le_data_fechamento.text())

    v_nome_cli = tela_abrir_os.cb_texto_buscar_cliente.currentText()
    v_nome_tecnico = tela_abrir_os.le_nome_tecnico.text()
    v_rg_tecnico = tela_abrir_os.le_rg_tecnico.text()
    v_defeito_info = tela_abrir_os.defeito_info.toPlainText()
    v_defeito_const = tela_abrir_os.defeito_const.toPlainText()
    v_medidas_corre = tela_abrir_os.medidas_corre.toPlainText()
    v_obs = tela_abrir_os.observacoes.toPlainText()

    if (tela_abrir_os.le_val_hora_tec.text().strip()==""):
        v_val_hora_tec = "0.00"
        tela_abrir_os.le_val_hora_tec.setText(v_val_hora_tec)
    else:
        v_val_hora_tec = tela_abrir_os.le_val_hora_tec.text()
        

    v_tempo_gasto = tela_abrir_os.le_tempo_gasto.text()
    #v_valor_mao_de_obra = tela_abrir_os.le_val_mao_de_obra.text()

    if (tela_abrir_os.le_val_mao_de_obra.text().strip()==""):
        v_valor_mao_de_obra = "0.00"
        tela_abrir_os.le_val_mao_de_obra.setText(v_valor_mao_de_obra)
    else:
        v_valor_mao_de_obra = tela_abrir_os.le_val_mao_de_obra.text()


    v_inventario = tela_abrir_os.le_inventario.text()
    v_equip_fabri = tela_abrir_os.le_equipa_fabri.text()
    v_modelo = tela_abrir_os.le_modelo.text()
    v_num_serie = tela_abrir_os.le_num_serie.text()
    v_portaria = tela_abrir_os.le_portaria.text()
    v_carga_max = tela_abrir_os.le_carga_max.text()
    v_divisao = tela_abrir_os.le_divisao.text()

    v_h_entrada = tela_abrir_os.le_h_entrada.text()
    v_h_saida = tela_abrir_os.le_h_saida.text()
    v_n_lacre_ant = tela_abrir_os.le_n_lacre_ant.text()
    v_n_lacre_atual = tela_abrir_os.le_n_lacre_atual.text()
    v_selo_rep_ant = tela_abrir_os.le_selo_rep_antigo.text()
    v_selo_rep_atual = tela_abrir_os.le_selo_rep_atual.text()

    v_cod_Peca_1 = tela_abrir_os.le_cod_peca_1.text()
    if (int(tela_abrir_os.le_quant_1.text())==0 or tela_abrir_os.le_quant_1.text().strip()==''):
        v_quant_1 = "0"
        tela_abrir_os.le_quant_1.setText(v_quant_1)
    else:
        v_quant_1 = tela_abrir_os.le_quant_1.text()

    v_descr_1 = tela_abrir_os.le_descri_1.text()
    v_val_unit_1 = tela_abrir_os.le_val_unit_1.text()
    v_val_tot_1 = tela_abrir_os.le_val_tot_1.text()

    if (float(tela_abrir_os.le_val_unit_1.text())==0.0 or tela_abrir_os.le_val_unit_1.text().strip()==''):
        v_val_unit_1 = "0.00"
        tela_abrir_os.le_val_unit_1.setText(v_val_unit_1)
    else:
        v_val_unit_1 = tela_abrir_os.le_val_unit_1.text()


    v_cod_Peca_2 = tela_abrir_os.le_cod_peca_2.text()
    if (int(tela_abrir_os.le_quant_2.text())==0 or tela_abrir_os.le_quant_2.text().strip()==''):
        v_quant_2 = "0"
        tela_abrir_os.le_quant_2.setText(v_quant_2)
    else:
        v_quant_2 = tela_abrir_os.le_quant_2.text()

    v_descr_2 = tela_abrir_os.le_descri_2.text()
    v_val_unit_2 = tela_abrir_os.le_val_unit_2.text()
    v_val_tot_2 = tela_abrir_os.le_val_tot_2.text()

    if (float(tela_abrir_os.le_val_unit_2.text())==0.0 or tela_abrir_os.le_val_unit_2.text().strip()==''):
        v_val_unit_2 = "0.00"
        tela_abrir_os.le_val_unit_2.setText(v_val_unit_2)
    else:
        v_val_unit_2 = tela_abrir_os.le_val_unit_2.text()



    v_cod_Peca_3 = tela_abrir_os.le_cod_peca_3.text()
    if (int(tela_abrir_os.le_quant_3.text())==0 or tela_abrir_os.le_quant_3.text().strip()==''):
        v_quant_3 = "0"
        tela_abrir_os.le_quant_3.setText(v_quant_3)
    else:
        v_quant_3 = tela_abrir_os.le_quant_3.text()

    v_descr_3 = tela_abrir_os.le_descri_3.text()
    v_val_unit_3 = tela_abrir_os.le_val_unit_3.text()
    v_val_tot_3 = tela_abrir_os.le_val_tot_3.text()

    if (float(tela_abrir_os.le_val_unit_3.text())==0.0 or tela_abrir_os.le_val_unit_3.text().strip()==''):
        v_val_unit_3 = "0.00"
        tela_abrir_os.le_val_unit_3.setText(v_val_unit_3)
    else:
        v_val_unit_3 = tela_abrir_os.le_val_unit_3.text()



    v_cod_Peca_4 = tela_abrir_os.le_cod_peca_4.text()
    if (int(tela_abrir_os.le_quant_4.text())==0 or tela_abrir_os.le_quant_4.text().strip()==''):
        v_quant_4 = "0"
        tela_abrir_os.le_quant_4.setText(v_quant_4)
    else:
        v_quant_4 = tela_abrir_os.le_quant_4.text()

    v_descr_4 = tela_abrir_os.le_descri_4.text()
    v_val_unit_4 = tela_abrir_os.le_val_unit_4.text()
    v_val_tot_4 = tela_abrir_os.le_val_tot_4.text()

    if (float(tela_abrir_os.le_val_unit_4.text())==0.0 or tela_abrir_os.le_val_unit_4.text().strip()==''):
        v_val_unit_4 = "0.00"
        tela_abrir_os.le_val_unit_4.setText(v_val_unit_4)
    else:
        v_val_unit_4 = tela_abrir_os.le_val_unit_4.text()



    v_cod_Peca_5 = tela_abrir_os.le_cod_peca_5.text()
    if (int(tela_abrir_os.le_quant_5.text())==0 or tela_abrir_os.le_quant_5.text().strip()==''):
        v_quant_5 = "0"
        tela_abrir_os.le_quant_5.setText(v_quant_5)
    else:
        v_quant_5 = tela_abrir_os.le_quant_5.text()

    v_descr_5 = tela_abrir_os.le_descri_5.text()
    v_val_unit_5 = tela_abrir_os.le_val_unit_5.text()
    v_val_tot_5 = tela_abrir_os.le_val_tot_5.text()

    if (float(tela_abrir_os.le_val_unit_5.text())==0.0 or tela_abrir_os.le_val_unit_5.text().strip()==''):
        v_val_unit_5 = "0.00"
        tela_abrir_os.le_val_unit_5.setText(v_val_unit_5)
    else:
        v_val_unit_5 = tela_abrir_os.le_val_unit_5.text()

    
    cursor=banco.cursor()
    comando_SQL="SELECT num_os FROM cad_os WHERE num_os='{}'".format(v_num_os)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    valor_id=0
    if (len(dados_lidos) > 0):
        #valor_id = dados_lidos[0][2]
        #print(dados_lidos)
        #tela_cad_cliente.label.setText("Cliente já Cadastrado")
        #tela_cad_cliente.label_2.setText("")
        mensagem('Aviso: ','Ordem de Serviço já Cadastrada! ')
        #cursor.close()
    else:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO cad_os (num_os,cnpj_cpf_oficina,cnpj_cpf_cliente,nome_cliente,nome_tecnico,rg_tecnico,val_mao_de_obra,defeitos_Informados,defeitos_constatados,medidas_corretivas,observacoes,valor_hora_tecnica,tempo_gasto,inventario,equip_fabricante,modelo,n_serie,portaria,carga_maxima,divisao,h_entrada,h_saida,n_lacre_antigo,n_lacre_atual,selo_reparado_antigo,selo_reparado_atual,cod_peca_1,quant_1,Descri_1,valor_unit_1,valor_tot_1,cod_peca_2,quant_2,Descri_2,valor_unit_2,valor_tot_2,cod_peca_3,quant_3,Descri_3,valor_unit_3,valor_tot_3,cod_peca_4,quant_4,Descri_4,valor_unit_4,valor_tot_4,cod_peca_5,quant_5,Descri_5,valor_unit_5,valor_tot_5,data_abertura,data_fechamento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(v_num_os),str(v_login),str(v_cnpj_cpf_cli),str(v_nome_cli),str(v_nome_tecnico),str(v_rg_tecnico),str(v_valor_mao_de_obra),str(v_defeito_info),str(v_defeito_const),str(v_medidas_corre),str(v_obs),str(v_val_hora_tec),str(v_tempo_gasto),str(v_inventario),str(v_equip_fabri),str(v_modelo),str(v_num_serie),str(v_portaria),str(v_carga_max),str(v_divisao),str(v_h_entrada),str(v_h_saida),str(v_n_lacre_ant),str(v_n_lacre_atual),str(v_selo_rep_ant),str(v_selo_rep_atual),str(v_cod_Peca_1),str(v_quant_1),str(v_descr_1),str(v_val_unit_1),str(v_val_tot_1),str(v_cod_Peca_2),str(v_quant_2),str(v_descr_2),str(v_val_unit_2),str(v_val_tot_2),str(v_cod_Peca_3),str(v_quant_3),str(v_descr_3),str(v_val_unit_3),str(v_val_tot_3),str(v_cod_Peca_4),str(v_quant_4),str(v_descr_4),str(v_val_unit_4),str(v_val_tot_4),str(v_cod_Peca_5),str(v_quant_5),str(v_descr_5),str(v_val_unit_5),str(v_val_tot_5),str(v_data_abertura),str(v_data_fechamento))
            
        cursor.execute(comando_SQL,dados)
        banco.commit()

        tela_cad_cliente.label.setText("Ordem de Serviço Cadastrada com Sucesso!")
        tela_cad_cliente.label_2.setText("")
        mensagem('Aviso: ','Ordem de Serviço Cadastrada com Sucesso!')

def abrir_os():
    global numero_id
    global v_cnpj_cpf_cli
    global v_num_os
 
    v_nome_cli = ""
    v_cnpj_cpf_cli = ""

    global v_tot_1
    global v_tot_2
    global v_tot_3
    global v_tot_4
    global v_tot_5

    v_tot_1 = 0.00
    v_tot_2 = 0.00
    v_tot_3 = 0.00
    v_tot_4 = 0.00
    v_tot_5 = 0.00

    #print(datetime.today().strftime('%Y%m%d%H'))co
    v_data_abertura = datetime.today().strftime('%d/%m/%Y')
    v_ano= datetime.today().strftime('%Y')
    v_ano=v_ano[2:]
    v_num_os= datetime.today().strftime(v_ano+'%m%d%H%M')
    tela_abrir_os.show()

    tela_abrir_os.le_data_abertura.setText(v_data_abertura)
    #tela_abrir_os.le_data_fechamento.setText('00/00/0000')

    tela_abrir_os.la_titulo.setText("Ordem de Serviço Num. : "+v_num_os)
    tela_abrir_os.la_oficina.setText("Oficina: '{}': ".format(bd_nome_oficina))


    '''
    #tela_abrir_os.le_texto_buscar_cliente.addItem("Amauri")
    #tela_abrir_os.le_texto_buscar_cliente.clear()
    #tela_abrir_os.cb_cliente_nome.clear()
    '''

    menu_principal.close()

    cursor = banco.cursor()
    cursor.execute("SELECT cnpj_cpf_cliente,nome_loja FROM cad_cliente WHERE cnpj_cpf_oficina='{}'".format(v_login))
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    '''
    for i in range(0, len(dados_lidos)):
        tela_abrir_os.cb_cliente_cnpj.addItem(dados_lidos[i][0])
        #tela_listar_cliente.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 


    for i in range(0, len(dados_lidos)):
        #for j in range(0, 1):
        tela_abrir_os.cb_cliente_nome.addItem(str(dados_lidos[i][1]))
    '''

    tela_abrir_os.le_buscar_cliente.setFocus()

def consulta_cnpj_oficinas():
    global resp
    #47.309.174/0002-85 micheletti
    #frase.replace(quero_trocar, trocar_por, len(frase))
    if Tela_Cadastro_oficinas_os.rb_cpf.isChecked():
        Tela_Cadastro_oficinas_os.lineEdit.setFocus()
        return


    cnpj = Tela_Cadastro_oficinas_os.lineEdit_2.text()

    cnpj = cnpj.replace("-", "", len(cnpj))
    cnpj = cnpj.replace("/", "", len(cnpj))
    cnpj = cnpj.replace(".", "", len(cnpj))

    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":cnpj,"plugin":"RF"}
    response = requests.request("GET", url, params=querystring)
    
    resp = json.loads(response.text)
    

    print(resp)
    if (len(resp) < 6):
        mensagem('Aviso:','CNPJ inválido')
        tela_cad_cliente.lineEdit_2.setFocus()
    else:    
        resp = json.loads(response.text)
        Tela_Cadastro_oficinas_os.lineEdit.setText(resp['nome'])
        #print(resp['nome'])
        #print(['logradouro'])
        Tela_Cadastro_oficinas_os.lineEdit_1.setFocus()
        #print(resp)
        return resp['nome'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'], resp['uf'], resp['cep'], resp['telefone'], resp['email']

def consulta_cnpj_cliente():
    global resp
    # 47.309.174/0002-85 micheletti
    #frase.replace(quero_trocar, trocar_por, len(frase))

    if tela_cad_cliente.rb_cpf.isChecked():
        tela_cad_cliente.lineEdit_11.setText("Isento")
        tela_cad_cliente.lineEdit.setFocus()
        return

    cnpj = tela_cad_cliente.lineEdit_2.text()

    cnpj = cnpj.replace("-", "", len(cnpj))
    cnpj = cnpj.replace("/", "", len(cnpj))
    cnpj = cnpj.replace(".", "", len(cnpj))

    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":cnpj,"plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)

    #print(resp)
    if (len(resp) < 6):
        mensagem('Aviso:','CNPJ inválido')
        tela_cad_cliente.lineEdit_2.setFocus()
    else:    
        v_endereco = resp['logradouro']+', '+resp['numero'] + ' ' + resp['complemento']
        tela_cad_cliente.show()
        tela_cad_cliente.lineEdit.setText(resp['nome'])
        tela_cad_cliente.lineEdit_3.setText(v_endereco)
        tela_cad_cliente.lineEdit_10.setText(resp['bairro'])
        tela_cad_cliente.lineEdit_4.setText(resp['municipio'])
        tela_cad_cliente.lineEdit_5.setText(resp['uf'])
        tela_cad_cliente.lineEdit_6.setText(resp['cep'])
        tela_cad_cliente.lineEdit_8.setText(resp['telefone'])
        tela_cad_cliente.lineEdit_9.setText(resp['email'])
        #print(resp['nome'])
        #print(['logradouro'])
        tela_cad_cliente.lineEdit_1.setFocus()
        #print(resp)
        return resp['nome'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'], resp['uf'], resp['cep'], resp['telefone'], resp['email']


'''  Sintegra

    meu_token = "01A6C3C6-7887-41E2-9EA1-4B022C402F5B"

    url = "https://www.sintegraws.com.br/api/v1/execute-api.php"

    querystring = {"token":meu_token,"cnpj":cnpj,"plugin":"ST"}

    response = requests.request("GET",url,params=querystring)

    print(response.text)

    a=a
'''

def mensagem(titulo,texto):
    #QMessageBox.about(listar_clientes,"Aviso:","Selecione Uma Linha na Tabela")
    
    msg = QMessageBox()
    msg.setWindowTitle(titulo)
    msg.setText(texto)
    msg.setIcon(QMessageBox.Information)
    #msg.setIcon(QMessageBox.Warning)
    #msg.setIcon(QMessageBox.Critical)
    msg.exec()    

def gravar_alteracao_cliente():
    global valor_id
    v_nome_loja_cli = tela_altera_cliente.lineEdit.text()
    v_resp_loja_cli = tela_altera_cliente.lineEdit_1.text()
    v_cnpj_cpf_cli = tela_altera_cliente.lineEdit_2.text()
    v_inscricao = tela_altera_cliente.lineEdit_11.text()
    v_endereco_cli = tela_altera_cliente.lineEdit_3.text()
    v_cid_cli = tela_altera_cliente.lineEdit_4.text()
    v_est_cli = tela_altera_cliente.lineEdit_4.text()
    v_cep_cli = tela_altera_cliente.lineEdit_6.text()
    v_fone_cli = tela_altera_cliente.lineEdit_8.text()
    v_whatsapp_cli = tela_altera_cliente.lineEdit_7.text()
    v_email_cli = tela_altera_cliente.lineEdit_9.text()
    
    #print(bd_nome_oficina)
    #print(v_login)
 
    cursor=banco.cursor()
    comando_SQL="SELECT * FROM cad_cliente WHERE cnpj_cpf_cliente='{}'".format(v_cnpj_cpf_cli)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    #print(dados_lidos)
    val_id = dados_lidos[0][0]

    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cad_cliente SET nome_loja = '{}', i_estadual ='{}',nome_responsavel = '{}', endereco = '{}', cidade = '{}', estado = '{}', cep ='{}', fone_loja ='{}', whatsapp_loja ='{}', email_loja ='{}' WHERE id = '{}'".format(v_nome_loja_cli,v_inscricao,v_resp_loja_cli,v_endereco_cli,v_cid_cli,v_est_cli,v_cep_cli,v_fone_cli,v_whatsapp_cli,v_email_cli,val_id))
    banco.commit()
    #banco.close()

    tela_altera_cliente.label.setText("Cliente Alterado com sucesso")
    tela_altera_cliente.label_2.setText("")
    mensagem('Aviso: ','Cliente Alterado com sucesso! ')
    #print("gravar Alteração")    

def gravar_alteracao_os():
    global valor_id
    global v_vum_os
    
    v_data_abertura = converte_data_para_banco(tela_altera_os.le_data_abertura.text())    
    v_data_fechamento = converte_data_para_banco(tela_altera_os.le_data_fechamento.text())

    v_nome_cli = tela_altera_os.cb_texto_buscar_cliente.currentText()
    v_nome_tecnico = tela_altera_os.le_nome_tecnico.text()
    v_rg_tecnico = tela_altera_os.le_rg_tecnico.text()
    v_defeito_info = tela_altera_os.defeito_info.toPlainText()
    v_defeito_const = tela_altera_os.defeito_const.toPlainText()
    v_medidas_corre = tela_altera_os.medidas_corre.toPlainText()
    v_obs = tela_altera_os.observacoes.toPlainText()

    if (tela_altera_os.le_val_hora_tec.text().strip()==""):
        v_val_hora_tec = "0.00"
        tela_altera_os.le_val_hora_tec.setText(v_val_hora_tec)
    else:
        v_val_hora_tec = tela_altera_os.le_val_hora_tec.text()
        

    v_tempo_gasto = tela_altera_os.le_tempo_gasto.text()
    #v_valor_mao_de_obra = tela_altera_os.le_val_mao_de_obra.text()

    if (tela_altera_os.le_val_mao_de_obra.text().strip()==""):
        v_valor_mao_de_obra = "0.00"
        tela_altera_os.le_val_mao_de_obra.setText(v_valor_mao_de_obra)
    else:
        v_valor_mao_de_obra = tela_altera_os.le_val_mao_de_obra.text()


    v_inventario = tela_altera_os.le_inventario.text()
    v_equip_fabri = tela_altera_os.le_equipa_fabri.text()
    v_modelo = tela_altera_os.le_modelo.text()
    v_num_serie = tela_altera_os.le_num_serie.text()
    v_portaria = tela_altera_os.le_portaria.text()
    v_carga_max = tela_altera_os.le_carga_max.text()
    v_divisao = tela_altera_os.le_divisao.text()

    v_h_entrada = tela_altera_os.le_h_entrada.text()
    v_h_saida = tela_altera_os.le_h_saida.text()
    v_n_lacre_ant = tela_altera_os.le_n_lacre_ant.text()
    v_n_lacre_atual = tela_altera_os.le_n_lacre_atual.text()
    v_selo_rep_ant = tela_altera_os.le_selo_rep_antigo.text()
    v_selo_rep_atual = tela_altera_os.le_selo_rep_atual.text()

    v_cod_Peca_1 = tela_altera_os.le_cod_peca_1.text()
    if (int(tela_altera_os.le_quant_1.text())==0 or tela_altera_os.le_quant_1.text().strip()==''):
        v_quant_1 = "0"
        tela_altera_os.le_quant_1.setText(v_quant_1)
    else:
        v_quant_1 = tela_altera_os.le_quant_1.text()

    v_descr_1 = tela_altera_os.le_descri_1.text()
    v_val_unit_1 = tela_altera_os.le_val_unit_1.text()
    v_val_tot_1 = tela_altera_os.le_val_tot_1.text()

    if (float(tela_altera_os.le_val_unit_1.text())==0.0 or tela_altera_os.le_val_unit_1.text().strip()==''):
        v_val_unit_1 = "0.00"
        tela_altera_os.le_val_unit_1.setText(v_val_unit_1)
    else:
        v_val_unit_1 = tela_altera_os.le_val_unit_1.text()


    v_cod_Peca_2 = tela_altera_os.le_cod_peca_2.text()
    if (int(tela_altera_os.le_quant_2.text())==0 or tela_altera_os.le_quant_2.text().strip()==''):
        v_quant_2 = "0"
        tela_altera_os.le_quant_2.setText(v_quant_2)
    else:
        v_quant_2 = tela_altera_os.le_quant_2.text()

    v_descr_2 = tela_altera_os.le_descri_2.text()
    v_val_unit_2 = tela_altera_os.le_val_unit_2.text()
    v_val_tot_2 = tela_altera_os.le_val_tot_2.text()

    if (float(tela_altera_os.le_val_unit_2.text())==0.0 or tela_altera_os.le_val_unit_2.text().strip()==''):
        v_val_unit_2 = "0.00"
        tela_altera_os.le_val_unit_2.setText(v_val_unit_2)
    else:
        v_val_unit_2 = tela_altera_os.le_val_unit_2.text()



    v_cod_Peca_3 = tela_altera_os.le_cod_peca_3.text()
    if (int(tela_altera_os.le_quant_3.text())==0 or tela_altera_os.le_quant_3.text().strip()==''):
        v_quant_3 = "0"
        tela_altera_os.le_quant_3.setText(v_quant_3)
    else:
        v_quant_3 = tela_altera_os.le_quant_3.text()

    v_descr_3 = tela_altera_os.le_descri_3.text()
    v_val_unit_3 = tela_altera_os.le_val_unit_3.text()
    v_val_tot_3 = tela_altera_os.le_val_tot_3.text()

    if (float(tela_altera_os.le_val_unit_3.text())==0.0 or tela_altera_os.le_val_unit_3.text().strip()==''):
        v_val_unit_3 = "0.00"
        tela_altera_os.le_val_unit_3.setText(v_val_unit_3)
    else:
        v_val_unit_3 = tela_altera_os.le_val_unit_3.text()



    v_cod_Peca_4 = tela_altera_os.le_cod_peca_4.text()
    if (int(tela_altera_os.le_quant_4.text())==0 or tela_altera_os.le_quant_4.text().strip()==''):
        v_quant_4 = "0"
        tela_altera_os.le_quant_4.setText(v_quant_4)
    else:
        v_quant_4 = tela_altera_os.le_quant_4.text()

    v_descr_4 = tela_altera_os.le_descri_4.text()
    v_val_unit_4 = tela_altera_os.le_val_unit_4.text()
    v_val_tot_4 = tela_altera_os.le_val_tot_4.text()

    if (float(tela_altera_os.le_val_unit_4.text())==0.0 or tela_altera_os.le_val_unit_4.text().strip()==''):
        v_val_unit_4 = "0.00"
        tela_altera_os.le_val_unit_4.setText(v_val_unit_4)
    else:
        v_val_unit_4 = tela_altera_os.le_val_unit_4.text()


    v_cod_Peca_5 = tela_altera_os.le_cod_peca_5.text()
    if (int(tela_altera_os.le_quant_5.text())==0 or tela_altera_os.le_quant_5.text().strip()==''):
        v_quant_5 = "0"
        tela_altera_os.le_quant_5.setText(v_quant_5)
    else:
        v_quant_5 = tela_altera_os.le_quant_5.text()

    v_descr_5 = tela_altera_os.le_descri_5.text()
    v_val_unit_5 = tela_altera_os.le_val_unit_5.text()
    v_val_tot_5 = tela_altera_os.le_val_tot_5.text()

    if (float(tela_altera_os.le_val_unit_5.text())==0.0 or tela_altera_os.le_val_unit_5.text().strip()==''):
        v_val_unit_5 = "0.00"
        tela_altera_os.le_val_unit_5.setText(v_val_unit_5)
    else:
        v_val_unit_5 = tela_altera_os.le_val_unit_5.text()



    #print(bd_nome_oficina)
    #print(v_login)
 
    cursor=banco.cursor()
    comando_SQL="SELECT id,num_os FROM cad_os WHERE num_os='{}'".format(v_num_os)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    val_id = dados_lidos[0][0]

    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cad_os SET nome_tecnico='{}', rg_tecnico='{}',val_mao_de_obra='{}',defeitos_Informados='{}',defeitos_constatados='{}',medidas_corretivas='{}',observacoes='{}',valor_hora_tecnica='{}',tempo_gasto='{}',inventario='{}',equip_fabricante='{}',modelo='{}',n_serie='{}',portaria='{}',carga_maxima='{}',divisao='{}',h_entrada='{}',h_saida='{}',n_lacre_antigo='{}',n_lacre_atual='{}',selo_reparado_antigo='{}',selo_reparado_atual='{}',cod_peca_5 ='{}', quant_5 ='{}', Descri_5 ='{}', valor_unit_5 ='{}', valor_tot_5 ='{}', cod_peca_4 ='{}', quant_4 ='{}', Descri_4 ='{}', valor_unit_4 ='{}', valor_tot_4 ='{}', cod_peca_3 ='{}', quant_3 ='{}', Descri_3 ='{}', valor_unit_3 ='{}', valor_tot_3 ='{}', cod_peca_2 ='{}', quant_2 ='{}', Descri_2 ='{}', valor_unit_2 ='{}', valor_tot_2 ='{}', cod_peca_1 ='{}', quant_1 ='{}', Descri_1 ='{}', valor_unit_1 ='{}', valor_tot_1 ='{}',data_fechamento='{}' WHERE id = '{}'".format(v_nome_tecnico,v_rg_tecnico,v_valor_mao_de_obra,v_defeito_info,v_defeito_const,v_medidas_corre,v_obs,v_val_hora_tec,v_tempo_gasto,v_inventario,v_equip_fabri,v_modelo,v_num_serie,v_portaria,v_carga_max,v_divisao,v_h_entrada,v_h_saida,v_n_lacre_ant,v_n_lacre_atual,v_selo_rep_ant,v_selo_rep_atual,v_cod_Peca_5,v_quant_5,v_descr_5,v_val_unit_5,v_val_tot_5,v_cod_Peca_4,v_quant_4,v_descr_4,v_val_unit_4,v_val_tot_4,v_cod_Peca_3,v_quant_3,v_descr_3,v_val_unit_3,v_val_tot_3,v_cod_Peca_2,v_quant_2,v_descr_2,v_val_unit_2,v_val_tot_2,v_cod_Peca_1,v_quant_1,v_descr_1,v_val_unit_1,v_val_tot_1,v_data_fechamento,val_id))
    banco.commit()
    #banco.close()

    tela_altera_cliente.label.setText("Ordem de Serviço Alterada com sucesso!")
    tela_altera_cliente.label_2.setText("")
    mensagem('Aviso: ','Ordem de Serviço Alterada com sucesso! ')
    #print("gravar Alteração")

def editar_os():
    global numero_id
    global v_num_os

    global v_tot_1_alt
    global v_tot_2_alt
    global v_tot_3_alt
    global v_tot_4_alt
    global v_tot_5_alt

    v_tot_1_alt = 0.00
    v_tot_2_alt = 0.00
    v_tot_3_alt = 0.00
    v_tot_4_alt = 0.00
    v_tot_5_alt = 0.00


    linha = tela_listar_os.tableWidget.currentRow()
    
    if (linha < 0):
        #QMessageBox.about(tela_listar_cliente,"Aviso:","Selecione Uma Linha na Tabela")
        mensagem('Aviso: ','Selecione uma Linha da Tabela! ')
    else:
        tela_altera_os.show()
        
        tela_altera_os.le_buscar_cliente.setText("")
        tela_altera_os.cb_texto_buscar_cliente.clear()
        tela_altera_os.le_nome_tecnico.setText("")
        tela_altera_os.le_rg_tecnico.setText("")
        tela_altera_os.defeito_info.setPlainText("")
        tela_altera_os.defeito_const.setPlainText("")
        tela_altera_os.medidas_corre.setPlainText("")
        tela_altera_os.observacoes.setPlainText("")

        tela_altera_os.le_val_hora_tec.setText("")
        tela_altera_os.le_tempo_gasto.setText("") 
        tela_altera_os.le_val_mao_de_obra.setText("")
        tela_altera_os.le_inventario.setText("")
        tela_altera_os.le_equipa_fabri.setText("")

        tela_altera_os.le_modelo.setText("")
        tela_altera_os.le_num_serie.setText("")
        tela_altera_os.le_portaria.setText("")
        tela_altera_os.le_carga_max.setText("")
        tela_altera_os.le_divisao.setText("")
        tela_altera_os.le_h_entrada.setText("")
        tela_altera_os.le_h_saida.setText("")
        tela_altera_os.le_n_lacre_ant.setText("")

        tela_altera_os.le_n_lacre_atual.setText("")
        tela_altera_os.le_selo_rep_antigo.setText("")
        tela_altera_os.le_selo_rep_atual.setText("")

        tela_altera_os.le_cod_peca_1.setText("")
        tela_altera_os.le_quant_1.setText("")
        tela_altera_os.le_descri_1.setText("")
        tela_altera_os.le_val_unit_1.setText("")
        tela_altera_os.le_val_tot_1.setText("")

        tela_altera_os.le_cod_peca_2.setText("")
        tela_altera_os.le_quant_2.setText("")
        tela_altera_os.le_descri_2.setText("")
        tela_altera_os.le_val_unit_2.setText("")
        tela_altera_os.le_val_tot_2.setText("")

        tela_altera_os.le_cod_peca_3.setText("")
        tela_altera_os.le_quant_3.setText("")
        tela_altera_os.le_descri_3.setText("")
        tela_altera_os.le_val_unit_3.setText("")
        tela_altera_os.le_val_tot_3.setText("")

        tela_altera_os.le_cod_peca_4.setText("")
        tela_altera_os.le_quant_4.setText("")
        tela_altera_os.le_descri_4.setText("")
        tela_altera_os.le_val_unit_4.setText("")
        tela_altera_os.le_val_tot_4.setText("")

        tela_altera_os.le_cod_peca_5.setText("")
        tela_altera_os.le_quant_5.setText("")
        tela_altera_os.le_descri_5.setText("")
        tela_altera_os.le_val_unit_5.setText("")
        tela_altera_os.le_val_tot_5.setText("")

        tela_altera_os.le_data_abertura.setText("")
        tela_altera_os.le_data_fechamento.setText("")

        cursor = banco.cursor()
        cursor.execute("SELECT id FROM cad_os WHERE cnpj_cpf_oficina='{}'".format(v_login))
        dados_lidos = cursor.fetchall()
        #print(dados_lidos)
        valor_id = dados_lidos[linha][0]
        cursor.execute("select * FROM cad_os WHERE id = '{}'".format(valor_id))
        dados_lidos = cursor.fetchall()
        print(dados_lidos)

        #tela_altera_os.lineEdit_2.setText(str(dados_lidos[0][1]))
        #tela_altera_os.lineEdit_11.setText(str(dados_lidos[0][3]))

        v_num_os = str(dados_lidos[0][1])

        tela_altera_os.num_os.setText("Número da Os: '{}'".format(str(dados_lidos[0][1])))

        tela_altera_os.le_buscar_cliente.setText("")
        tela_altera_os.cb_texto_buscar_cliente.addItem(str(dados_lidos[0][4]))
        tela_altera_os.le_nome_tecnico.setText(str(dados_lidos[0][5]))
        tela_altera_os.le_rg_tecnico.setText(str(dados_lidos[0][6]))
        tela_altera_os.le_val_mao_de_obra.setText(str(dados_lidos[0][7]))
        
        tela_altera_os.defeito_info.setPlainText(str(dados_lidos[0][8]))
        tela_altera_os.defeito_const.setPlainText(str(dados_lidos[0][9]))
        tela_altera_os.medidas_corre.setPlainText(str(dados_lidos[0][10]))
        tela_altera_os.observacoes.setPlainText(str(dados_lidos[0][11]))
        
        tela_altera_os.le_val_hora_tec.setText(str(dados_lidos[0][12]))
        tela_altera_os.le_tempo_gasto.setText(str(dados_lidos[0][13])) 
        #tela_altera_os.le_val_mao_de_obra.setText(str(dados_lidos[0][13]))
        tela_altera_os.le_inventario.setText(str(dados_lidos[0][14]))
        tela_altera_os.le_equipa_fabri.setText(str(dados_lidos[0][15]))

        tela_altera_os.le_modelo.setText(str(dados_lidos[0][16]))
        tela_altera_os.le_num_serie.setText(str(dados_lidos[0][17]))
        tela_altera_os.le_portaria.setText(str(dados_lidos[0][18]))
        tela_altera_os.le_carga_max.setText(str(dados_lidos[0][19]))
        tela_altera_os.le_divisao.setText(str(dados_lidos[0][20]))
        tela_altera_os.le_h_entrada.setText(str(dados_lidos[0][21]))
        tela_altera_os.le_h_saida.setText(str(dados_lidos[0][22]))
        tela_altera_os.le_n_lacre_ant.setText(str(dados_lidos[0][23]))

        tela_altera_os.le_n_lacre_atual.setText(str(dados_lidos[0][24]))
        tela_altera_os.le_selo_rep_antigo.setText(str(dados_lidos[0][25]))
        tela_altera_os.le_selo_rep_atual.setText(str(dados_lidos[0][26]))

        tela_altera_os.le_cod_peca_5.setText(str(dados_lidos[0][27]))
        tela_altera_os.le_quant_5.setText(str(dados_lidos[0][28]))
        tela_altera_os.le_descri_5.setText(str(dados_lidos[0][29]))
        tela_altera_os.le_val_unit_5.setText(str(dados_lidos[0][30]))
        tela_altera_os.le_val_tot_5.setText(str(dados_lidos[0][31]))

        tela_altera_os.le_cod_peca_4.setText(str(dados_lidos[0][32]))
        tela_altera_os.le_quant_4.setText(str(dados_lidos[0][33]))
        tela_altera_os.le_descri_4.setText(str(dados_lidos[0][34]))
        tela_altera_os.le_val_unit_4.setText(str(dados_lidos[0][35]))
        tela_altera_os.le_val_tot_4.setText(str(dados_lidos[0][36]))

        tela_altera_os.le_cod_peca_3.setText(str(dados_lidos[0][37]))
        tela_altera_os.le_quant_3.setText(str(dados_lidos[0][38]))
        tela_altera_os.le_descri_3.setText(str(dados_lidos[0][39]))
        tela_altera_os.le_val_unit_3.setText(str(dados_lidos[0][40]))
        tela_altera_os.le_val_tot_3.setText(str(dados_lidos[0][41]))

        tela_altera_os.le_cod_peca_2.setText(str(dados_lidos[0][42]))
        tela_altera_os.le_quant_2.setText(str(dados_lidos[0][43]))
        tela_altera_os.le_descri_2.setText(str(dados_lidos[0][44]))
        tela_altera_os.le_val_unit_2.setText(str(dados_lidos[0][45]))
        tela_altera_os.le_val_tot_2.setText(str(dados_lidos[0][46]))

        tela_altera_os.le_cod_peca_1.setText(str(dados_lidos[0][47]))
        tela_altera_os.le_quant_1.setText(str(dados_lidos[0][48]))
        tela_altera_os.le_descri_1.setText(str(dados_lidos[0][49]))
        tela_altera_os.le_val_unit_1.setText(str(dados_lidos[0][50]))
        tela_altera_os.le_val_tot_1.setText(str(dados_lidos[0][51]))

        vdata_abertura = converte_data_do_banco(str(dados_lidos[0][52]))
        vdata_fechamento = converte_data_do_banco(str(dados_lidos[0][53]))

        tela_altera_os.le_data_abertura.setText(vdata_abertura)
        tela_altera_os.le_data_fechamento.setText(vdata_fechamento)

        #numero_id = valor_id

        #v_cod_cli = dados_lidos[0][14]

        tela_altera_os.la_titulo.setText("Editar Ordem de Serviço")
        tela_altera_os.la_oficina.setText("Oficina: "+bd_nome_oficina)
        #tela_altera_os.label_4.setText("Codigo Cliente: "+v_cod_cli)            

        tela_listar_os.close()

def editar_dados_cliente():
    global numero_id

    linha = tela_listar_cliente.tableWidget.currentRow()
    
    if (linha < 0):
        #QMessageBox.about(tela_listar_cliente,"Aviso:","Selecione Uma Linha na Tabela")
        mensagem('Aviso: ','Selecione uma Linha da Tabela! ')
    else:
        tela_altera_cliente.show()
        tela_altera_cliente.lineEdit_2.setText("")  # cnpj_cli
        tela_altera_cliente.lineEdit_11.setText("") # Inscricao Estadual
        tela_altera_cliente.lineEdit.setText("")    # Nome Loja
        tela_altera_cliente.lineEdit_1.setText("")  # Responsavel
        tela_altera_cliente.lineEdit_3.setText("")  # ende
        tela_altera_cliente.lineEdit_10.setText("")  # Bairro
        tela_altera_cliente.lineEdit_4.setText("")  # cidade
        tela_altera_cliente.lineEdit_5.setText("")  # estado
        tela_altera_cliente.lineEdit_6.setText("")  # cep
        tela_altera_cliente.lineEdit_8.setText("")  # fone
        tela_altera_cliente.lineEdit_7.setText("")  # whats
        tela_altera_cliente.lineEdit_9.setText("")  # email

        cursor = banco.cursor()
        cursor.execute("SELECT id FROM cad_cliente WHERE cnpj_cpf_oficina='{}'".format(v_login))
        dados_lidos = cursor.fetchall()
        #print(dados_lidos)
        valor_id = dados_lidos[linha][0]
        cursor.execute("select * FROM cad_cliente WHERE id = '{}'".format(valor_id))
        dados_lidos = cursor.fetchall()
        #print(dados_lidos)

        if (testa_cnpj_cpf(dados_lidos[0][1]) =="cnpj"):
            tela_altera_cliente.lineEdit_2.setInputMask("99.999.999/9999-99")
            tela_altera_cliente.rb_cnpj.setChecked(True)
            tela_altera_cliente.lineEdit_2.setFocus()
        else:
            tela_altera_cliente.lineEdit_2.setInputMask("999.999.999-99")
            tela_altera_cliente.rb_cpf.setChecked(True)
            tela_altera_cliente.lineEdit_2.setFocus()


        tela_altera_cliente.lineEdit_2.setText(str(dados_lidos[0][1]))  # cnpj_cli
        tela_altera_cliente.lineEdit_11.setText(str(dados_lidos[0][3]))  # cnpj_cli
        tela_altera_cliente.lineEdit.setText(str(dados_lidos[0][4]))    # Nome Loja
        tela_altera_cliente.lineEdit_1.setText(str(dados_lidos[0][5]))  # Responsavel
        tela_altera_cliente.lineEdit_3.setText(str(dados_lidos[0][6]))  # ende
        tela_altera_cliente.lineEdit_10.setText(str(dados_lidos[0][7]))  # Bairro
        tela_altera_cliente.lineEdit_4.setText(str(dados_lidos[0][8]))  # cidade
        tela_altera_cliente.lineEdit_5.setText(str(dados_lidos[0][9]))  # estado
        tela_altera_cliente.lineEdit_6.setText(str(dados_lidos[0][10]))  # cep
        tela_altera_cliente.lineEdit_8.setText(str(dados_lidos[0][11]))  # fone
        tela_altera_cliente.lineEdit_7.setText(str(dados_lidos[0][12]))  # whats
        tela_altera_cliente.lineEdit_9.setText(str(dados_lidos[0][13]))  # email
        #numero_id = valor_id

        v_cod_cli = dados_lidos[0][14]

        tela_altera_cliente.label_3.setText("Oficina: "+bd_nome_oficina)
        tela_altera_cliente.label_4.setText("Codigo Cliente: "+v_cod_cli)            

        tela_listar_cliente.close()

def excluir_dados_cliente():
    global v_cnpj_cpf_cli

    linha = tela_listar_cliente.tableWidget.currentRow()

    if (linha < 0):
        mensagem('Aviso:','Escolha uma linha para Exclusão')
        return

    tela_listar_cliente.tableWidget.removeRow(linha)


    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cad_cliente WHERE cnpj_cpf_oficina='{}'".format(v_login))
    dados_lidos = cursor.fetchall()
    #print(dados_lidos)
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cad_cliente WHERE id = '{}'".format(valor_id))
    banco.commit()
    mensagem('Aviso: ','Cliente Excluido com Sucesso! ')

def excluir_os():
    global v_cnpj_cpf_cli

    linha = tela_listar_os.tableWidget.currentRow()

    if (linha < 0):
        mensagem('Aviso:','Escolha uma linha para Exclusão')
        return

    tela_listar_os.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cad_os WHERE cnpj_cpf_oficina='{}' and v_cnpj_cpf_cli='{}'".format(v_login,v_cnpj_cpf_cli))
    dados_lidos = cursor.fetchall()
    #print(dados_lidos)
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cad_os WHERE id = '{}'".format(valor_id))
    banco.commit()
    mensagem('Aviso: ','Ordem de Serviço Excluida com Sucesso! ')

def listar_os():
    global numero_id
    global v_cnpj_cpf_cli

    menu_principal.close()
    tela_listar_os.show()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id,num_os,nome_cliente,data_abertura,data_fechamento FROM cad_os WHERE cnpj_cpf_oficina='{}'".format(v_login))
    dados_lidos = cursor.fetchall()

    tela_listar_os.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_os.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
           tela_listar_os.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    #tela_listar_os.tableWidget.setCurrentRow(-1)           

def listar_clientes():
    global numero_id
    global v_cnpj_cpf_cli


    menu_principal.close()
    tela_altera_cliente.close()
    tela_listar_cliente.show()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id,cnpj_cpf_cliente,cnpj_cpf_oficina,i_estadual,nome_loja FROM cad_cliente WHERE cnpj_cpf_oficina='{}'".format(v_login))
    dados_lidos = cursor.fetchall()

    tela_listar_cliente.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_cliente.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
           tela_listar_cliente.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 
    #tela_listar_cliente.tableWidget.setCurrentItem(-1)           

def cadastrar_cliente():
    global v_cod_cli
    menu_principal.close()
    tela_cad_cliente.show()

    tela_altera_cliente.lineEdit_2.setText("")  # cnpj_cli
    tela_altera_cliente.lineEdit_11.setText("")  # cnpj_cli
    tela_altera_cliente.lineEdit.setText("")    # Nome Loja
    tela_altera_cliente.lineEdit_1.setText("")  # Responsavel
    tela_altera_cliente.lineEdit_3.setText("")  # ende
    tela_altera_cliente.lineEdit_10.setText("")  # Bairro
    tela_altera_cliente.lineEdit_4.setText("")  # cidade
    tela_altera_cliente.lineEdit_5.setText("")  # estado
    tela_altera_cliente.lineEdit_6.setText("")  # cep
    tela_altera_cliente.lineEdit_8.setText("")  # fone
    tela_altera_cliente.lineEdit_7.setText("")  # whats
    tela_altera_cliente.lineEdit_9.setText("")  # email

    #print(datetime.today().strftime('%Y%m%d%H'))
    v_ano= datetime.today().strftime('%Y')
    v_ano=v_ano[2:]
    v_cod_cli= datetime.today().strftime(v_ano+'%m%d%H%M')
    tela_cad_cliente.label_3.setText("Oficina: "+bd_nome_oficina)
    tela_cad_cliente.label_4.setText("Codigo Cliente: "+v_cod_cli)
    if tela_cad_cliente.rb_cnpj.isChecked():
        seleciona_cnpj_cliente()

def gravar_cliente():
    global v_cod_cli

    v_nome_loja_cli = tela_cad_cliente.lineEdit.text()
    v_resp_loja_cli = tela_cad_cliente.lineEdit_1.text()
    v_cnpj_cpf_cli = tela_cad_cliente.lineEdit_2.text()
    v_incricao = tela_cad_cliente.lineEdit_11.text()
    v_endereco_cli = tela_cad_cliente.lineEdit_3.text()
    v_bairro_cli = tela_cad_cliente.lineEdit_10.text()
    v_cid_cli = tela_cad_cliente.lineEdit_4.text()
    v_est_cli = tela_cad_cliente.lineEdit_4.text()
    v_cep_cli = tela_cad_cliente.lineEdit_6.text()
    v_fone_cli = tela_cad_cliente.lineEdit_8.text()
    v_whatsapp_cli = tela_cad_cliente.lineEdit_7.text()
    v_email_cli = tela_cad_cliente.lineEdit_9.text()
    
    print(bd_nome_oficina)
    print(v_login) 

    cursor=banco.cursor()
    comando_SQL="SELECT * FROM cad_cliente WHERE cnpj_cpf_cliente='{}'".format(v_cnpj_cpf_cli)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    valor_id=0
    if (len(dados_lidos) > 0):
        valor_id = dados_lidos[0][2]
        print(dados_lidos)
        tela_cad_cliente.label.setText("Cliente já Cadastrado")
        tela_cad_cliente.label_2.setText("")
        mensagem('Aviso: ','Cliente já Cadastrado! ')
        #cursor.close()

    if (valor_id == 0):
            cursor = banco.cursor()
            comando_SQL = "INSERT INTO cad_cliente (cnpj_cpf_cliente,cnpj_cpf_oficina,i_estadual,nome_loja,nome_responsavel,endereco,bairro,cidade,estado,cep,fone_loja,whatsapp_loja,email_loja,codigo_cliente) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            dados = (str(v_cnpj_cpf_cli),str(v_login),str(v_incricao),str(v_nome_loja_cli),str(v_resp_loja_cli),str(v_endereco_cli),str(v_bairro_cli),str(v_cid_cli),str(v_est_cli),str(v_cep_cli),str(v_fone_cli),str(v_whatsapp_cli),str(v_email_cli),str(v_cod_cli))
            
            cursor.execute(comando_SQL,dados)
            banco.commit()

            tela_cad_cliente.label.setText("Cliente Cadastrado com Sucesso")
            tela_cad_cliente.label_2.setText("")
            mensagem('Aviso: ','Cliente Cadastrado com Sucesso! ')

def gravar_alteracao_oficina():
    #global v_login
    cursor=banco.cursor()
    comando_SQL="SELECT * FROM cad_oficina WHERE cnpj_cpf='{}'".format(v_login)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    #print(dados_lidos)
    valor_id=0
    if (len(dados_lidos) > 0):
        numero_id = dados_lidos[0][0]

    # ler dados do lineEdit
    v_inscricao = Tela_Altera_cad_oficina.lineEdit_6.text()
    v_responsavel = Tela_Altera_cad_oficina.lineEdit_1.text()
    v_endereco = Tela_Altera_cad_oficina.lineEdit.text()
    v_bairro = Tela_Altera_cad_oficina.lineEdit_5.text()
    v_cidade = Tela_Altera_cad_oficina.lineEdit_3.text()
    v_estado = Tela_Altera_cad_oficina.lineEdit_2.text()
    v_cep = Tela_Altera_cad_oficina.lineEdit_4.text()
    v_fone_oficina=Tela_Altera_cad_oficina.lineEdit_8.text()
    v_whatsapp_oficina=Tela_Altera_cad_oficina.lineEdit_7.text()
    v_email_oficina=Tela_Altera_cad_oficina.lineEdit_9.text()

    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cad_oficina SET responsavel = '{}',i_estadual = '{}', endereco = '{}', bairro = '{}', cidade = '{}', estado = '{}', cep ='{}', fone_oficina ='{}', whatsapp_oficina ='{}', email_oficina ='{}', ativo_s_n_susp ='{}' WHERE id = '{}'".format(v_responsavel,v_inscricao,v_endereco,v_bairro,v_cidade,v_estado,v_cep,v_fone_oficina,v_whatsapp_oficina,v_email_oficina,'Ativo',numero_id))
    banco.commit()
    #banco.close()
    Tela_Altera_cad_oficina.label.setText("Oficina Alterada com Sucesso")
    Tela_Altera_cad_oficina.label_2.setText("")
    mensagem('Aviso: ','Oficina Alterada com Sucesso! ')
    #print("gravar Alteração")    

def altera_oficina():
    menu_principal.close()
    v_login = tela_login_os.le_login.text()
    cursor = banco.cursor()
    comando_SQL="SELECT * FROM cad_oficina WHERE cnpj_cpf='{}'".format(v_login)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    #banco.close()
    #print(dados_lidos)
    valor_id=0
    if (len(dados_lidos) > 0):
        numero_id = dados_lidos[0][0]
        Tela_Altera_cad_oficina.lineEdit_1.setText(dados_lidos[0][5]) # responsavel
        Tela_Altera_cad_oficina.lineEdit_6.setText(dados_lidos[0][2]) # inscrição estadual
        Tela_Altera_cad_oficina.lineEdit.setText(dados_lidos[0][6])   # endereco
        Tela_Altera_cad_oficina.lineEdit_5.setText(dados_lidos[0][7]) # bairro
        Tela_Altera_cad_oficina.lineEdit_3.setText(dados_lidos[0][8]) # cidade
        Tela_Altera_cad_oficina.lineEdit_2.setText(dados_lidos[0][9]) # estado
        Tela_Altera_cad_oficina.lineEdit_4.setText(dados_lidos[0][10]) # cep
        Tela_Altera_cad_oficina.lineEdit_8.setText(dados_lidos[0][11]) # fone
        Tela_Altera_cad_oficina.lineEdit_7.setText(dados_lidos[0][12]) # whatsapp
        Tela_Altera_cad_oficina.lineEdit_9.setText(dados_lidos[0][13]) # email

    Tela_Altera_cad_oficina.show()

def testa_cnpj_cpf(doc):
    letra_1 = "-"
    letra_2 = "/"
    if (letra_1 in doc and letra_2 in doc):
        return "cnpj"
    else:
        return "cpf"

def voltar_menu_principal():
    menu_principal.show()
    tela_altera_cliente.close()
    tela_altera_os.close()
    tela_abrir_os.close()
    Tela_Altera_cad_oficina.close()
    tela_listar_cliente.close()
    tela_listar_os.close()
    tela_cad_cliente.close()

def sair_tela_login():
    tela_login_os.close()

def logout():
    segunda_tela_login.close()
    tela_login_os.show()

def voltar_login():
    tela_cad_cliente.close()
    Tela_Cadastro_oficinas_os.close()
    Tela_Complemento_cad_oficina.close()
    menu_principal.close()
    tela_login_os.show()

def gravar_complemento():
    v_login = Tela_Cadastro_oficinas_os.lineEdit_2.text()
    cursor = banco.cursor()
    comando_SQL="SELECT * FROM cad_oficina WHERE cnpj_cpf='{}'".format(v_login)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    #banco.close()
    #print(dados_lidos)
    valor_id=0
    if (len(dados_lidos) > 0):
        numero_id = dados_lidos[0][0]    

    
    # ler dados do lineEdit
    v_inscricao = Tela_Complemento_cad_oficina.lineEdit_5.text()
    v_endereco = Tela_Complemento_cad_oficina.lineEdit.text()
    v_bairro = Tela_Complemento_cad_oficina.lineEdit_4.text()
    v_cidade = Tela_Complemento_cad_oficina.lineEdit_1.text()
    v_estado = Tela_Complemento_cad_oficina.lineEdit_2.text()
    v_cep = Tela_Complemento_cad_oficina.lineEdit_3.text()
    v_fone = Tela_Complemento_cad_oficina.lineEdit_8.text()
    v_whatsapp = Tela_Complemento_cad_oficina.lineEdit_7.text()
    v_email = Tela_Complemento_cad_oficina.lineEdit_9.text()
    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cad_oficina SET endereco = '{}',i_estadual = '{}',bairro = '{}', cidade = '{}', estado = '{}', cep ='{}', fone_oficina ='{}', whatsapp_oficina ='{}', email_oficina ='{}', ativo_s_n_susp ='{}' WHERE id = '{}'".format(v_endereco,v_inscricao,v_bairro,v_cidade,v_estado,v_cep,v_fone,v_whatsapp,v_email,'Ativo',numero_id))
    banco.commit()

    Tela_Complemento_cad_oficina.label.setText("Oficina Complementada com Sucesso")
    Tela_Complemento_cad_oficina.label_2.setText("")
    mensagem('Aviso: ','Oficina Complementada com Sucesso! ')
    #banco.close()

def chama_segunda_tela_login():
    global bd_nome_oficina
    global v_login

    tela_login_os.label_4.setText("")
    v_login = tela_login_os.le_login.text()
    v_senha = tela_login_os.le_senha.text()

    if (v_login=="" or v_senha==""):
        tela_login_os.label_4.setText("Dados não Digitados!")
        mensagem('Aviso: ','Dados Não Digitados! ')
    else:
        cursor = banco.cursor()
        comando_SQL="SELECT * FROM cad_oficina WHERE cnpj_cpf='{}'".format(v_login)
        cursor.execute(comando_SQL)
        dados_lidos = cursor.fetchall()
        #print(dados_lidos)
        #banco.close()
        valor_id=0
        if (len(dados_lidos) > 0):
            bd_login = dados_lidos[0][1]
            bd_senha = dados_lidos[0][4]
            bd_nome_oficina=dados_lidos[0][3]

            #print(dados_lidos)
            if (v_senha == bd_senha and v_login == bd_login) :
                tela_login_os.label_4.setText(bd_nome_oficina)
                
                tela_login_os.close()
                menu_principal.show()
            else :
                #tela_login_os.label_4.setText("Login ou Senha incorretos!") 
                mensagem('Aviso: ','Login ou Senha Incorretos! ')
        else :
            #tela_login_os.label_4.setText("Login não encontrado!")
            mensagem('Aviso: ','Login não Encontrado! ')

def cadastrar():

    v_nome_oficina = Tela_Cadastro_oficinas_os.lineEdit.text()
    v_inscricao = ""   #Tela_Cadastro_oficinas_os.lineEdit_6.text()
    v_responsavel = Tela_Cadastro_oficinas_os.lineEdit_1.text()
    v_login = Tela_Cadastro_oficinas_os.lineEdit_2.text()
    v_senha = Tela_Cadastro_oficinas_os.lineEdit_3.text()
    c_senha = Tela_Cadastro_oficinas_os.lineEdit_4.text()
    v_endereco = ""
    v_cidade=""
    v_estado=""
    v_cep=""
    v_fone_oficina=""
    v_whatsapp_oficina=""
    v_email_oficina=""

    v_ativo=""
    print(v_nome_oficina)
    print(v_responsavel)
 
    cursor = banco.cursor()
    #{}".format(codigo,descricao,preco,categoria,numero_id))
    comando_SQL="SELECT * FROM cad_oficina WHERE cnpj_cpf='{}'".format(v_login)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    #banco.close()
    valor_id=0
    if (len(dados_lidos) > 0):
        valor_id = dados_lidos[0][3]
        print(dados_lidos)
        Tela_Cadastro_oficinas_os.label.setText("Oficina já Cadastrada")
        Tela_Cadastro_oficinas_os.label_2.setText("")
        mensagem('Aviso: ','Oficina Já Cadastrada! ')
    elif (v_login=="" or v_senha==""):
            tela_login_os.label_4.setText("Dados não Digitados!")
            mensagem('Aviso: ','Dados Não Digitados! ')
    elif (valor_id == 0):
        if (v_senha == c_senha):

            cursor = banco.cursor()
            comando_SQL = "INSERT INTO cad_oficina (cnpj_cpf,i_estadual,nome_oficina,senha,responsavel,endereco,cidade,estado,cep,fone_oficina,whatsapp_oficina,email_oficina,ativo_s_n_susp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            dados = (str(v_login),str(v_inscricao),str(v_nome_oficina),str(v_senha),str(v_responsavel),str(v_endereco),str(v_cidade),str(v_estado),str(v_cep),str(v_fone_oficina),str(v_whatsapp_oficina),str(v_email_oficina),str(v_ativo))
            
            cursor.execute(comando_SQL,dados)
            banco.commit()
            #cursor.close()

            Tela_Cadastro_oficinas_os.label.setText("Oficina Cadastrada com Sucesso")
            Tela_Cadastro_oficinas_os.label_2.setText("")
            #mensagem('Aviso: ','Oficina Cadastrada com Sucesso! ')

            #Tela_Cadastro_oficinas_os.close()

#resp['nome'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'], resp['uf'], resp['cep'], resp['telefone'], resp['email']

            v_endereco = resp['logradouro']+', '+resp['numero'] + ' ' + resp['complemento']
            Tela_Complemento_cad_oficina.show()
            Tela_Complemento_cad_oficina.lineEdit.setText(v_endereco)
            Tela_Complemento_cad_oficina.lineEdit_1.setText(resp['municipio'])
            Tela_Complemento_cad_oficina.lineEdit_2.setText(resp['uf'])
            Tela_Complemento_cad_oficina.lineEdit_3.setText(resp['cep'])
            Tela_Complemento_cad_oficina.lineEdit_8.setText(resp['telefone'])
            Tela_Complemento_cad_oficina.lineEdit_9.setText(resp['email'])

        else:
            Tela_Cadastro_oficinas_os.label.setText("Senhas Digitadas São diferentes")
            mensagem('Aviso: ','Senhas Digitadas São Diferentes! ')

def abre_Tela_Cadastro_oficinas_os():
    tela_login_os.close()        
    Tela_Cadastro_oficinas_os.show()
    if Tela_Cadastro_oficinas_os.rb_cnpj.isChecked():
        seleciona_cnpj_oficina()

def seleciona_cnpj_login():
    if tela_login_os.rb_cnpj.isChecked():
        tela_login_os.le_login.setInputMask("99.999.999/9999-99")
        tela_login_os.le_login.setFocus()


def seleciona_cpf_login():
    if tela_login_os.rb_cpf.isChecked():
        tela_login_os.le_login.setInputMask("999.999.999-99")
        tela_login_os.le_login.setFocus()


def seleciona_cnpj_oficina():
    if Tela_Cadastro_oficinas_os.rb_cnpj.isChecked():
        Tela_Cadastro_oficinas_os.lineEdit_2.setInputMask("99.999.999/9999-99")
        Tela_Cadastro_oficinas_os.lineEdit_2.setFocus()


def seleciona_cpf_oficina():
    if Tela_Cadastro_oficinas_os.rb_cpf.isChecked():
        Tela_Cadastro_oficinas_os.lineEdit_2.setInputMask("999.999.999-99")
        Tela_Cadastro_oficinas_os.lineEdit_2.setFocus()


def seleciona_cnpj_cliente():
    if tela_cad_cliente.rb_cnpj.isChecked():
        tela_cad_cliente.lineEdit_2.setInputMask("99.999.999/9999-99")
        tela_cad_cliente.lineEdit_2.setFocus()


def seleciona_cpf_cliente():
    if tela_cad_cliente.rb_cpf.isChecked():
        tela_cad_cliente.lineEdit_2.setInputMask("999.999.999-99")
        tela_cad_cliente.lineEdit_2.setFocus()


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def salvar_valor_editado():
    global numero_id

    # ler dados do lineEdit
    codigo = tela_editar.lineEdit_2.text()
    descricao = tela_editar.lineEdit_3.text()
    preco = tela_editar.lineEdit_4.text()
    categoria = tela_editar.lineEdit_5.text()
    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE produtos SET codigo = '{}', descricao = '{}', valor = '{}', categoria ='{}' WHERE id = {}".format(codigo,descricao,preco,categoria,numero_id))
    banco.commit()
    #atualizar as janelas
    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()

app=QtWidgets.QApplication([])

tela_login_os=uic.loadUi("tela_login_os.ui")
tela_login_os.pb_login.clicked.connect(chama_segunda_tela_login)  #chama_segunda_tela_login
tela_login_os.pb_sair.clicked.connect(sair_tela_login)
tela_login_os.le_senha.setEchoMode(QtWidgets.QLineEdit.Password)
tela_login_os.pb_cadastrar.clicked.connect(abre_Tela_Cadastro_oficinas_os)
tela_login_os.rb_cnpj.clicked.connect(seleciona_cnpj_login)
tela_login_os.rb_cpf.clicked.connect(seleciona_cpf_login)

segunda_tela = uic.loadUi("segunda_tela.ui")
segunda_tela_login = uic.loadUi("segunda_tela_login.ui")
segunda_tela_login.pushButton.clicked.connect(logout)

Tela_Cadastro_oficinas_os = uic.loadUi("Tela_Cadastro_oficinas_os.ui")
Tela_Cadastro_oficinas_os.pb_cadastrar.clicked.connect(cadastrar)
Tela_Cadastro_oficinas_os.pb_consulta.clicked.connect(consulta_cnpj_oficinas)
Tela_Cadastro_oficinas_os.pb_cadastrar_2.clicked.connect(voltar_login)
Tela_Cadastro_oficinas_os.rb_cnpj.clicked.connect(seleciona_cnpj_oficina)
Tela_Cadastro_oficinas_os.rb_cpf.clicked.connect(seleciona_cpf_oficina)

Tela_Complemento_cad_oficina = uic.loadUi("Tela_complemento_oficinas_os.ui")
Tela_Complemento_cad_oficina.pb_cadastrar.clicked.connect(gravar_complemento)
Tela_Complemento_cad_oficina.pb_cadastrar_2.clicked.connect(voltar_login)

menu_principal = uic.loadUi("menu_os.ui")
menu_principal.pb_login_5.clicked.connect(altera_oficina)
menu_principal.pb_login_4.clicked.connect(voltar_login)
menu_principal.pb_login.clicked.connect(cadastrar_cliente)
menu_principal.pb_login_7.clicked.connect(listar_clientes)
menu_principal.pb_abrir_os.clicked.connect(abrir_os)
menu_principal.pb_fecha_os.clicked.connect(listar_os)

Tela_Altera_cad_oficina = uic.loadUi("Tela_alterar_Cadastro_oficinas_os.ui")
Tela_Altera_cad_oficina.pb_cadastrar.clicked.connect(gravar_alteracao_oficina)
Tela_Altera_cad_oficina.pb_cadastrar_2.clicked.connect(voltar_menu_principal)

tela_cad_cliente = uic.loadUi("Tela_Cadastro_clientes_os.ui")
tela_cad_cliente.pb_cadastrar_2.clicked.connect(voltar_menu_principal)
tela_cad_cliente.pb_consulta.clicked.connect(consulta_cnpj_cliente)
tela_cad_cliente.pb_cadastrar.clicked.connect(gravar_cliente)
tela_cad_cliente.rb_cnpj.clicked.connect(seleciona_cnpj_cliente)
tela_cad_cliente.rb_cpf.clicked.connect(seleciona_cpf_cliente)

tela_altera_cliente = uic.loadUi("Tela_Alterar_Cadastro_clientes_os.ui")
tela_altera_cliente.pb_cadastrar_2.clicked.connect(listar_clientes)
tela_altera_cliente.pb_grava_alt_cli.clicked.connect(gravar_alteracao_cliente)
tela_altera_cliente.rb_cnpj.clicked.connect(seleciona_cnpj_cliente)
tela_altera_cliente.rb_cpf.clicked.connect(seleciona_cpf_cliente)

tela_listar_cliente = uic.loadUi("listar_clientes_os.ui")
tela_listar_cliente.pb_excluir.clicked.connect(excluir_dados_cliente)
tela_listar_cliente.pb_voltar_menu.clicked.connect(voltar_menu_principal)
tela_listar_cliente.pb_editar_cliente.clicked.connect(editar_dados_cliente)


tela_listar_os = uic.loadUi("listar_os.ui")
tela_listar_os.pb_excluir.clicked.connect(excluir_os)
tela_listar_os.pb_voltar_menu.clicked.connect(voltar_menu_principal)
tela_listar_os.pb_editar_os.clicked.connect(editar_os)


tela_abrir_os = uic.loadUi("Tela_Abrir_Ordem_de_Servico.ui")
tela_abrir_os.le_val_unit_1.textEdited.connect(digita_valor_1)
tela_abrir_os.le_val_unit_2.textEdited.connect(digita_valor_2)
tela_abrir_os.le_val_unit_3.textEdited.connect(digita_valor_3)
tela_abrir_os.le_val_unit_4.textEdited.connect(digita_valor_4)
tela_abrir_os.le_val_unit_5.textEdited.connect(digita_valor_5)
tela_abrir_os.le_quant_1.textEdited.connect(digita_quant_1)
tela_abrir_os.le_quant_2.textEdited.connect(digita_quant_2)
tela_abrir_os.le_quant_3.textEdited.connect(digita_quant_3)
tela_abrir_os.le_quant_4.textEdited.connect(digita_quant_4)
tela_abrir_os.le_quant_5.textEdited.connect(digita_quant_5)
tela_abrir_os.le_val_hora_tec.textEdited.connect(digita_hora_tec)
tela_abrir_os.le_val_mao_de_obra.textEdited.connect(digita_val_mao_de_obra)
tela_abrir_os.le_buscar_cliente.textEdited.connect(buscar_cliente)
tela_abrir_os.pb_gera_pdf_os.clicked.connect(gerar_pdf_os)
tela_abrir_os.pb_voltar_menu.clicked.connect(voltar_menu_principal)
tela_abrir_os.pb_gravar_os.clicked.connect(gravar_os)


tela_altera_os = uic.loadUi("Tela_Alterar_Ordem_de_Servico.ui")
tela_altera_os.le_val_unit_1.textEdited.connect(digita_valor_1_alt)
tela_altera_os.le_val_unit_2.textEdited.connect(digita_valor_2_alt)
tela_altera_os.le_val_unit_3.textEdited.connect(digita_valor_3_alt)
tela_altera_os.le_val_unit_4.textEdited.connect(digita_valor_4_alt)
tela_altera_os.le_val_unit_5.textEdited.connect(digita_valor_5_alt)
tela_altera_os.le_quant_1.textEdited.connect(digita_quant_1_alt)
tela_altera_os.le_quant_2.textEdited.connect(digita_quant_2_alt)
tela_altera_os.le_quant_3.textEdited.connect(digita_quant_3_alt)
tela_altera_os.le_quant_4.textEdited.connect(digita_quant_4_alt)
tela_altera_os.le_quant_5.textEdited.connect(digita_quant_5_alt)
tela_altera_os.le_val_hora_tec.textEdited.connect(digita_hora_tec_alt)
tela_altera_os.le_val_mao_de_obra.textEdited.connect(digita_val_mao_de_obra_alt)
#tela_altera_os.le_buscar_cliente.textEdited.connect(buscar_cliente)
tela_altera_os.pb_gera_pdf_os.clicked.connect(gerar_pdf_os)
tela_altera_os.pb_voltar_menu.clicked.connect(voltar_menu_principal)
tela_altera_os.pb_gravar_altera_os.clicked.connect(gravar_alteracao_os)



tela_login_os.show()
#tela_login_os.setWindowTitle("no title")
if tela_login_os.rb_cnpj.isChecked():
    seleciona_cnpj_login()
    #consulta_cnpj("47.309.174/0002-85")
    #47.309.174/0002-85

app.exec()
