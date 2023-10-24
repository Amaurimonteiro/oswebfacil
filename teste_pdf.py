from calendar import day_name, month
from datetime import datetime
from email.mime import message
import logging
from tkinter import messagebox
from urllib import response
#from typing_extensions import Self
from PyQt5.QtWidgets import QMessageBox,QApplication,QLineEdit,QWidget
from PyQt5.QtCore import Qt
from PyQt5 import  uic,QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import sys

import requests
import json


def mm2p(milimetros):
    return milimetros / 0.352777


def gerar_pdf_os():
    '''
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cad_cliente"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    '''

    y = 0
    pdf = canvas.Canvas("os_nova.pdf",pagesize=A4)

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

    pdf.save()


    #pdf.drawImage("cadeado.png",80,250,width=200,height=350)

app=QtWidgets.QApplication([])

tela_abrir_os = uic.loadUi("Tela_Abrir_Ordem_de_Servico.ui")
tela_abrir_os.pb_gera_pdf_os.clicked.connect(gerar_pdf_os)

tela_abrir_os.show()
app.exec()
