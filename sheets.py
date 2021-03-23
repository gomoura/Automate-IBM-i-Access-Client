#----------------------------------------------------
def sheet1_xml_telas(planilha_aba1):


    sht1_mouse_click_a9_temp = []
    sht1_mouse_click_a9 = [] #--> Possui o valor de cada linha da primeira plahilha ***já com a estrutura do JDE a9***

    for contador, coluna in planilha_aba1.iterrows():
        #Criando uma coluna com o nome das telas
        sht1_mouse_click_a9_temp.append(coluna["Telas"])
        #Criando uma coluna com o XML dos cliques
        sht1_mouse_click_a9_temp.append(f'<mouseclick row = "{coluna["Linha"]}" col = "{coluna["Coluna"]}"/>')   
        #Passando da lista temporária para a principal
        sht1_mouse_click_a9.append(sht1_mouse_click_a9_temp[:])
        #Limpando a lista temporária para a próxima iteração
        sht1_mouse_click_a9_temp.clear()
    return sht1_mouse_click_a9

#----------------------------------------------------

def sheet2_xml_campos(planilha_aba2):

    #Gerando a linha de valor da da Sheet_2  - XML
    sht2_val_campo_temp = []
    sht2_val_campo = [] #variavel final

    for index, row in planilha_aba2.iterrows():
        c = 0
        while c < len(planilha_aba2.columns):
            sht2_val_campo_temp.append(f'<input value="&apos;{str(row[c])}&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false"/>')
            c +=1
        
        sht2_val_campo.append(sht2_val_campo_temp[:])
        sht2_val_campo_temp.clear()

    return sht2_val_campo

#----------------------------------------------------

def sheet2_valor_telas(planilha_aba2): #Devolve o valor de cada campo da sheet 2 destacando os campos em branco

    #Preenchendo os campos vazios da segunda Sheet com null(Segunda aba)
    planilha_aba2.fillna(value="null", inplace=True)

    sht2_val_celula_temp = []
    sht2_val_celula = [] #variavel final

    for index, row in planilha_aba2.iterrows():
        c = 0

        while c < len(planilha_aba2.columns):
            #Coletando o valor se o XML
            sht2_val_celula_temp.append(row[c])
            c +=1

        sht2_val_celula.append(sht2_val_celula_temp[:])
        sht2_val_celula_temp.clear()
    
    return sht2_val_celula

#----------------------------------------------------

def sheet2_valor_s_null(sheet1_xml_telas_,sheet2_xml_campos_,sheet2_valor_telas_): #Devolve o valor de cada campo da sheet 2 destacando os campos em branco

  
    sht2_val_celula_temp = []
    sht2_val_celula = [] #variavel final

    for index1, valor1  in enumerate(sheet2_xml_campos_): # Fazendo o script percorrer todas as colunas da SHEET2 
        for index2, valor2 in enumerate(sheet1_xml_telas_): # Fazendo o script percorrer todas as colunas da SHEET2
            #if sheet2_valor[index1][index2] != "null":
            if sheet2_valor_telas_[index1][index2] != 'null':
                
                sht2_val_celula_temp.append(valor2)

        sht2_val_celula.append(sht2_val_celula_temp[:])
        sht2_val_celula_temp.clear()
    
    return sht2_val_celula

#----------------------------------------------------


def unindo_tela_valor(planilha_aba1,planilha_aba2,sheet2_valor_telas_):

    addressTemp = []
    address = []
    addressTemp1 = []


    for index1, valor1 in enumerate(planilha_aba2): # Fazendo o script percorrer todas as colunas da SHEET2     
        for index2, valor2 in enumerate(planilha_aba1): # Fazendo o script percorrer todas as colunas da SHEET2 
            if sheet2_valor_telas_[index1][index2] != 'null':
                addressTemp.append(valor2[1])
                addressTemp.append(valor1[index2])

                addressTemp1.append(addressTemp[:])
                addressTemp.clear()
                
        address.append(addressTemp1[:])
        addressTemp1.clear()
 
    return(address)

#----------------------------------------------------

def telas_a_criar(unindo_tela_valor_,sheet1_xml_telas_,sheet2_xml_campos_,sheet2_valor_telas_):
    telas = []
    telasTemp = []

    sheet2_valor_s_null_ = sheet2_valor_s_null(sheet1_xml_telas_,sheet2_xml_campos_,sheet2_valor_telas_)

    for indice0,valor0 in enumerate(unindo_tela_valor_):
        for indice1, valor1 in enumerate(sheet2_valor_s_null_[indice0]):
            telasTemp.append(valor1[0])
        telas.append(telasTemp[:])
        telasTemp.clear()
    return telas

#----------------------------------------------------

def list_rindex(li, x):
    for i in range(len(li)):
        if li[i] == x:
            reserva = i
    return reserva
import sheets as planilha
import screens as tela

telasTemp = []
telas = []

#----------------------------------------------------
#Histórico
def frase_historico(planilha_aba1,sheet2_valor_telas_):
    from datetime import datetime

    requisitante = planilha_aba1['Requisitante'][0]
    data_e_hora = str(datetime.now())[:19]
    campos = []
    historico = []
    historicoTemp = []
    
    #Obtendo o nome dos campos da Sheet1
    for i in planilha_aba1['Campos']:
        campos.append(i)

    for j in range(len(sheet2_valor_telas_)): # Fazendo o script percorrer todas as colunas da SHEET2
        for i, valor in enumerate(sheet2_valor_telas_[j]): # Fazendo o script percorrer todas as linhas da SHEET2
            
            if valor != "null":
                if i > 1:
                    historicoTemp.append(campos[i])

            if i == len(campos)-1:
                historicoTemp.append(f'Requestor {requisitante}')
                historicoTemp.append(data_e_hora)            

        historico.append(', '.join(historicoTemp[:]))#Estou removendo os brackts para transformar em uma lista única
        historicoTemp.clear()
   

    return historico