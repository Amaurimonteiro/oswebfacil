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
    pdf = canvas.Canvas("os_23424.pdf",pagesize=A4)

    pdf.setLineWidth(0.5)
    pdf.setFont("Times-Bold", 14)

    #pdf.circle(mm2p(100),mm2p(150),mm2p(100))
    #pdf.line(mm2p(100),mm2p(150),mm2p(100),mm2p(150))


    # Ultima linha
    pdf.setFont("Times-Bold", 12)
    pdf.rect(mm2p(5),mm2p(5),mm2p(66),mm2p(15))
    pdf.rect(mm2p(71),mm2p(5),mm2p(67),mm2p(15))
    pdf.rect(mm2p(138),mm2p(5),mm2p(67),mm2p(15))
    pdf.drawString(mm2p(11),mm2p(15), "Informações para Nota Fiscal")
    pdf.drawString(mm2p(75),mm2p(15), "Nota Fiscal - Data de Emissão")
    pdf.drawString(mm2p(140),mm2p(15), "TOTAL GERAL")
    
    # Declaro estar Ciente
    pdf.setFont("Times-Bold", 13)
    pdf.drawString(mm2p(13),mm2p(44), "Declaro estar ciente de que todas as informações contidas nesta Ordem de Serviço são verídicas.")

    pdf.setFont("Times-Bold", 14)
    pdf.drawString(mm2p(7),mm2p(23), "Nome do Cliente:")
    pdf.drawString(mm2p(100),mm2p(23), "Data:")

    pdf.rect(mm2p(5),mm2p(20),mm2p(200),mm2p(30))

    #pdf.drawImage("cadeado.png",200,250,width=100,height=150)

    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "PRODUTO")
    pdf.drawString(310,750, "valor")
    pdf.drawString(410,750, "CATEGORIA")
    pdf.save()

'''
    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!")
'''

def digita_valor():
    v_txt = tela_abrir_os.le_texto_buscar_cliente_2.text()
    v_txt = v_txt.replace(",", ".", len(v_txt))
    v_teste = v_txt.find(".")

    if(v_txt.isnumeric()):
        tela_abrir_os.le_texto_buscar_cliente_2.setText(v_txt)
        tela_abrir_os.la_Oficina.setText(v_txt)
    else:
        if(v_teste>0 and len(v_txt) <= v_teste + 3):
            tela_abrir_os.le_texto_buscar_cliente_2.setText(v_txt)
            tela_abrir_os.la_Oficina.setText(v_txt)
        else:
            v_txt = v_txt[0:len(v_txt)-1]
            tela_abrir_os.le_texto_buscar_cliente_2.setText(v_txt)
            tela_abrir_os.la_Oficina.setText(v_txt)



def buscar_cliente():

    v_texto = tela_abrir_os.le_texto_buscar_cliente.text()

    cursor = banco.cursor()
    #SELECT * FROM Customers WHERE CustomerName LIKE '%or%';
    v_texto_cnpj = "SELECT cnpj_cpf_cliente FROM cad_cliente WHERE cnpj_cpf_cliente LIKE '%{}%' and cnpj_cpf_oficina='{}'".format(v_texto,v_login)
    cursor.execute(v_texto_cnpj)
    dados_lidos = cursor.fetchall()
    #print(len(dados_lidos))
    if (len(dados_lidos) > 0):
        tela_abrir_os.le_texto_buscar_cliente.setText(str(dados_lidos[0][0]))
    else:
        cursor = banco.cursor()
        #SELECT * FROM Customers WHERE CustomerName LIKE '%or%';
        v_texto_nome = "SELECT nome_loja FROM cad_cliente WHERE nome_loja LIKE '%{}%' and cnpj_cpf_oficina='{}'".format(v_texto,v_login)
        cursor.execute(v_texto_nome)
        dados_lidos = cursor.fetchall()
        if (len(dados_lidos) == 0):
            mensagem('Aviso: ','Cliente Não Encontrado!')
        else:    
            #print(dados_lidos)
            tela_abrir_os.le_texto_buscar_cliente.setText(str(dados_lidos[0][0]))

    


def abrir_os():
    global numero_id
    global v_cnpj_cpf_cli

    tela_abrir_os.show()

    '''
    #tela_abrir_os.cb_cliente.addItem("Amauri")
    #tela_abrir_os.cb_cliente_cnpj.clear()
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

    tela_abrir_os.le_texto_buscar_cliente.setFocus()
    


def consulta_cnpj_oficinas():
    global resp
    #47.309.174/0002-85 micheletti
    #frase.replace(quero_trocar, trocar_por, len(frase))

    cnpj = Tela_Cadastro_oficinas_os.lineEdit_2.text()

    cnpj = cnpj.replace("-", "", len(cnpj))
    cnpj = cnpj.replace("/", "", len(cnpj))
    cnpj = cnpj.replace(".", "", len(cnpj))

    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":cnpj,"plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)
    Tela_Cadastro_oficinas_os.lineEdit.setText(resp['nome'])
    #print(resp['nome'])
    #print(['logradouro'])
    Tela_Cadastro_oficinas_os.lineEdit_1.setFocus()
    #print(resp)
    return resp['nome'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'], resp['uf'], resp['cep'], resp['telefone'], resp['email']


def consulta_cnpj_cliente():
    global resp
    #47.309.174/0002-85 micheletti
    #frase.replace(quero_trocar, trocar_por, len(frase))

    cnpj = tela_cad_cliente.lineEdit_2.text()

    cnpj = cnpj.replace("-", "", len(cnpj))
    cnpj = cnpj.replace("/", "", len(cnpj))
    cnpj = cnpj.replace(".", "", len(cnpj))

    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":cnpj,"plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)

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
    cursor.execute("UPDATE cad_cliente SET nome_loja = '{}', nome_responsavel = '{}', endereco = '{}', cidade = '{}', estado = '{}', cep ='{}', fone_loja ='{}', whatsapp_loja ='{}', email_loja ='{}' WHERE id = '{}'".format(v_nome_loja_cli,v_resp_loja_cli,v_endereco_cli,v_cid_cli,v_est_cli,v_cep_cli,v_fone_cli,v_whatsapp_cli,v_email_cli,val_id))
    banco.commit()
    #banco.close()

    tela_altera_cliente.label.setText("Cliente Alterado com sucesso")
    tela_altera_cliente.label_2.setText("")
    mensagem('Aviso: ','Cliente Alterado com sucesso! ')
    #print("gravar Alteração")    


def editar_dados_cliente():
    global numero_id

    linha = tela_listar_cliente.tableWidget.currentRow()
    
    if (linha < 0):
        #QMessageBox.about(tela_listar_cliente,"Aviso:","Selecione Uma Linha na Tabela")
        mensagem('Aviso: ','Selecione uma Linha da Tabela! ')
    else:
        tela_altera_cliente.show()
        tela_altera_cliente.lineEdit_2.setText("")  # cnpj_cli
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
        print(dados_lidos)
        valor_id = dados_lidos[linha][0]
        cursor.execute("select * FROM cad_cliente WHERE id = '{}'".format(valor_id))
        dados_lidos = cursor.fetchall()
        print(dados_lidos)

        if (testa_cnpj_cpf(dados_lidos[0][1]) =="cnpj"):
            tela_altera_cliente.lineEdit_2.setInputMask("99.999.999/9999-99")
            tela_altera_cliente.rb_cnpj.setChecked(True)
            tela_altera_cliente.lineEdit_2.setFocus()
        else:
            tela_altera_cliente.lineEdit_2.setInputMask("999.999.999-99")
            tela_altera_cliente.rb_cpf.setChecked(True)
            tela_altera_cliente.lineEdit_2.setFocus()


        tela_altera_cliente.lineEdit_2.setText(str(dados_lidos[0][1]))  # cnpj_cli
        tela_altera_cliente.lineEdit.setText(str(dados_lidos[0][3]))    # Nome Loja
        tela_altera_cliente.lineEdit_1.setText(str(dados_lidos[0][4]))  # Responsavel
        tela_altera_cliente.lineEdit_3.setText(str(dados_lidos[0][5]))  # ende
        tela_altera_cliente.lineEdit_10.setText(str(dados_lidos[0][6]))  # Bairro
        tela_altera_cliente.lineEdit_4.setText(str(dados_lidos[0][7]))  # cidade
        tela_altera_cliente.lineEdit_5.setText(str(dados_lidos[0][8]))  # estado
        tela_altera_cliente.lineEdit_6.setText(str(dados_lidos[0][9]))  # cep
        tela_altera_cliente.lineEdit_8.setText(str(dados_lidos[0][10]))  # fone
        tela_altera_cliente.lineEdit_7.setText(str(dados_lidos[0][11]))  # whats
        tela_altera_cliente.lineEdit_9.setText(str(dados_lidos[0][12]))  # email
        #numero_id = valor_id

        v_cod_cli = dados_lidos[0][13]

        tela_altera_cliente.label_3.setText("Oficina: "+bd_nome_oficina)
        tela_altera_cliente.label_4.setText("Codigo Cliente: "+v_cod_cli)            

        tela_listar_cliente.close()


def excluir_dados_cliente():
    linha = tela_listar_cliente.tableWidget.currentRow()
    tela_listar_cliente.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cad_cliente WHERE cnpj_cpf_oficina='{}'".format(v_login))
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cad_cliente WHERE id = '{}'".format(valor_id))
    banco.commit()
    mensagem('Aviso: ','Cliente Excluido com Sucesso! ')


def listar_clientes():
    global numero_id
    global v_cnpj_cpf_cli

    menu_principal.close()
    tela_altera_cliente.close()
    tela_listar_cliente.show()

    #linha = segunda_tela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    #cursor.execute("SELECT id FROM produtos")
    #dados_lidos = cursor.fetchall()
    #valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cad_cliente WHERE cnpj_cpf_oficina='{}'".format(v_login))
    dados_lidos = cursor.fetchall()

    tela_listar_cliente.tableWidget.setRowCount(len(dados_lidos))
    tela_listar_cliente.tableWidget.setColumnCount(4)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
           tela_listar_cliente.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 



def cadastrar_cliente():
    global v_cod_cli
    menu_principal.close()
    tela_cad_cliente.show()
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
            comando_SQL = "INSERT INTO cad_cliente (cnpj_cpf_cliente,cnpj_cpf_oficina,nome_loja,nome_responsavel,endereco,bairro,cidade,estado,cep,fone_loja,whatsapp_loja,email_loja,codigo_cliente) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            dados = (str(v_cnpj_cpf_cli),str(v_login),str(v_nome_loja_cli),str(v_resp_loja_cli),str(v_endereco_cli),str(v_bairro_cli),str(v_cid_cli),str(v_est_cli),str(v_cep_cli),str(v_fone_cli),str(v_whatsapp_cli),str(v_email_cli),str(v_cod_cli))
            
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
    cursor.execute("UPDATE cad_oficina SET responsavel = '{}', endereco = '{}', bairro = '{}', cidade = '{}', estado = '{}', cep ='{}', fone_oficina ='{}', whatsapp_oficina ='{}', email_oficina ='{}', ativo_s_n_susp ='{}' WHERE id = '{}'".format(v_responsavel,v_endereco,v_bairro,v_cidade,v_estado,v_cep,v_fone_oficina,v_whatsapp_oficina,v_email_oficina,'Ativo',numero_id))
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
        Tela_Altera_cad_oficina.lineEdit_1.setText(dados_lidos[0][4]) # responsavel
        Tela_Altera_cad_oficina.lineEdit.setText(dados_lidos[0][5])   # endereco
        Tela_Altera_cad_oficina.lineEdit_5.setText(dados_lidos[0][6]) # bairro
        Tela_Altera_cad_oficina.lineEdit_3.setText(dados_lidos[0][7]) # cidade
        Tela_Altera_cad_oficina.lineEdit_2.setText(dados_lidos[0][8]) # estado
        Tela_Altera_cad_oficina.lineEdit_4.setText(dados_lidos[0][9]) # cep
        Tela_Altera_cad_oficina.lineEdit_8.setText(dados_lidos[0][10]) # fone
        Tela_Altera_cad_oficina.lineEdit_7.setText(dados_lidos[0][11]) # whatsapp
        Tela_Altera_cad_oficina.lineEdit_9.setText(dados_lidos[0][12]) # email

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
    Tela_Altera_cad_oficina.close()
    tela_listar_cliente.close()
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
    cursor.execute("UPDATE cad_oficina SET endereco = '{}',bairro = '{}', cidade = '{}', estado = '{}', cep ='{}', fone_oficina ='{}', whatsapp_oficina ='{}', email_oficina ='{}', ativo_s_n_susp ='{}' WHERE id = '{}'".format(v_endereco,v_bairro,v_cidade,v_estado,v_cep,v_fone,v_whatsapp,v_email,'Ativo',numero_id))
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
        print(dados_lidos)
        #banco.close()
        valor_id=0
        if (len(dados_lidos) > 0):
            bd_login = dados_lidos[0][1]
            bd_senha = dados_lidos[0][3]
            bd_nome_oficina=dados_lidos[0][2]

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
    #banco.close()
    valor_id=0
    if (len(dados_lidos) > 0):
        valor_id = dados_lidos[0][2]
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
            comando_SQL = "INSERT INTO cad_oficina (cnpj_cpf,nome_oficina,senha,responsavel,endereco,cidade,estado,cep,fone_oficina,whatsapp_oficina,email_oficina,ativo_s_n_susp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            dados = (str(v_login),str(v_nome_oficina),str(v_senha),str(v_responsavel),str(v_endereco),str(v_cidade),str(v_estado),str(v_cep),str(v_fone_oficina),str(v_whatsapp_oficina),str(v_email_oficina),str(v_ativo))
            
            cursor.execute(comando_SQL,dados)
            banco.commit()
            #cursor.close()

            Tela_Cadastro_oficinas_os.label.setText("Oficina Cadastrada com Sucesso")
            Tela_Cadastro_oficinas_os.label_2.setText("")
            mensagem('Aviso: ','Oficina Cadastrada com Sucesso! ')

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



    #if (valor_id>0):
    #    valor_id = dados_lidos[linha][0]
    #    tela_editar.show()

     #   tela_editar.lineEdit.setText(str(produto[0][0]))
     #   tela_editar.lineEdit_2.setText(str(produto[0][1]))
     #   tela_editar.lineEdit_3.setText(str(produto[0][2]))
     #   tela_editar.lineEdit_4.setText(str(produto[0][3]))
     #   tela_editar.lineEdit_5.setText(str(produto[0][4]))
     #   numero_id = valor_id



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