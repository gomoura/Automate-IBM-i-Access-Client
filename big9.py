import sheets as planilha
import screens as tela
import pandas as pd


planilha_aba1 = pd.read_excel(r"POC.xlsm",sheet_name=0,dtype=str)
planilha_aba2 = pd.read_excel(r"POC.xlsm",sheet_name=1,dtype=str)


nr_tela = 1
cod_acao = []
xml_ = []
validador = 0

controlador_1=0 
controlador_2 =0
controlador_3 = 0
controlador_4 = 0
controlador_5 = 0
controlador_6 = 0
controlador_7 = 0

qtd_registros_hist = 0
qtd_registros_tela1 = 0
qtd_registros_tela2 = 0
qtd_registros_tela3 = 0
qtd_registros_tela4 = 0
qtd_registros_tela5 = 0
qtd_registros_tela6 = 0
qtd_registros_tela7 = 0


#Carregando os valores dos módulos
sheet1_xml_telas_ = planilha.sheet1_xml_telas(planilha_aba1)
sheet2_xml_campos_ = planilha.sheet2_xml_campos(planilha_aba2)
sheet2_valor_telas_ = planilha.sheet2_valor_telas(planilha_aba2)
unindo_tela_valor_ = planilha.unindo_tela_valor(sheet1_xml_telas_,sheet2_xml_campos_,sheet2_valor_telas_)
telas_a_criar_ = planilha.telas_a_criar(unindo_tela_valor_,sheet1_xml_telas_,sheet2_xml_campos_,sheet2_valor_telas_)
frase_historico_ = planilha.frase_historico(planilha_aba1,sheet2_valor_telas_)

for index0, valor0  in enumerate(unindo_tela_valor_): # Fazendo o script percorrer todas as colunas da SHEET2 (Ele olha quantas linhas foram preenchidas.)
    controlador_1 = 0
    controlador_2 = 0
    controlador_3 = 0
    controlador_4 = 0
    controlador_5 = 0
    controlador_6 = 0
    controlador_7 = 0

    cod_acao.clear() #Limpando a lista com o código de ação e o address
    for index1, valor1  in enumerate(unindo_tela_valor_[index0]): # Fazendo o script percorrer todas as colunas da SHEET2 (Ele olha quantas linhas foram preenchidas.)
        #só irá criar a linha se o valor for diferente de null
        #Preenchendo o cabeçalho Hash 
        if index0 == 0 and index1 == 0:
            xml_.append(tela.cabecalhoHash())

      #------------------------------[[[   1    ]]]----------------------------
                
        if  't_1051' == telas_a_criar_[index0][index1]:
            if controlador_1 == 0:
                qtd_registros_tela1 = telas_a_criar_[index0].count('t_1051')
                xml_.append(tela.cabecalhoScreen01(nr_tela,"true","false"))

                if validador == 0:
                    xml_.append(tela.validador_tela())
                    validador +=1

                controlador_1 += 1
            
            for i, valor in enumerate(unindo_tela_valor_[index0][index1]):
                xml_.append(f'\n{valor}')

                #coletando o código de ação, se o indice for menor ou igual a 1 (Ele irá coletar o address e o codigo de ação)
                if controlador_1 < 2:
                    if index1 <= 1:
                        cod_acao.append(valor)
                        controlador_1 =+ 1

                #Adicionando o enter na tela
                if index1 == 1 and i == 1:
                    xml_.append(tela.enter_tela())
                #Adicionando a linha de deletar
                if i % 2 == 0:
                    xml_.append(tela.deletar_valor())
            
            #Adicionando o final da tela
            #Se não houver alterações na tela
            if qtd_registros_tela1 == 2:
                if index1 == (qtd_registros_tela1 - 1):
                    nr_tela +=1
                    xml_.append(tela.rodape(nr_tela))
            #Se houver alterações na tela
            if index1 > 1:
                if index1 == (qtd_registros_tela1 - 1):
                    xml_.append(tela.final_tela_1051())
                    nr_tela +=1
                    xml_.append(tela.rodape(nr_tela))


#------------------------------[[[   2    ]]]----------------------------
        elif 't_10512_1'  == telas_a_criar_[index0][index1]:
            if controlador_2 == 0:
                qtd_registros_tela2 = telas_a_criar_[index0].count('t_10512_1')
                xml_.append(tela.cabecalhoScreen01(nr_tela,"true","false"))
                controlador_2 += 1

                #Se houver alterações na tela **1** (>2)ele precisa pesquisar o item novamente
                if qtd_registros_tela1 > 2:
                    for index, valorIndex in enumerate(cod_acao):
                        xml_.append(f'\n{valorIndex}')
                    if index == 3:
                        xml_.append(tela.enter_tela()) 

            #Está adicionando o shift + f2 para entrar na tela **2**
            if controlador_2 == 1:
                xml_.append(tela.acessando_t_10512_1())
                controlador_2 += 1 


            #Adicionando os dados da serem alterarados
            for i, valor in enumerate(unindo_tela_valor_[index0][index1]):
                xml_.append(f'\n{valor}')
                #Adicionando a linha de deletar
                if i % 2 == 0:
                    xml_.append(tela.deletar_valor())   

            #Adicionando o final da tela
            #Irá criar a tela de finalização da tela 2 apenas se não existir alterações na 3 
            if telas_a_criar_[index0].count('t_10512_2') == 0:
                if planilha.list_rindex(telas_a_criar_[0],'t_10512_1') == index1:
                    xml_.append(tela.finalizando_t_10512_1ou2())
                    nr_tela +=1
                    xml_.append(tela.rodape(nr_tela))  


     #------------------------------[[[   3    ]]]----------------------------
        elif  't_10512_2' == telas_a_criar_[index0][index1]:
            if controlador_3 == 0:
                if qtd_registros_tela2 == 0: # Se houver alteração na tela t_10512_1 não irei criar a chamada ta tela
                    xml_.append(tela.cabecalhoScreen01(nr_tela,"true","false"))
                    qtd_registros_tela3 = telas_a_criar_[index0].count('t_10512_2')
                    controlador_3 += 1
                else:
                    qtd_registros_tela3 = telas_a_criar_[index0].count('t_10512_2')
                    controlador_3 += 1

                #Carregando o código de açãodo e o Address
                if controlador_3 == 1:
                    if qtd_registros_tela1 > 2: #Validando que HOUVE alteração na tela 1
                        if qtd_registros_tela2 == 0: #Validando que Ñ HOUVE alteração tela 2
                            for index, valorIndex in enumerate(cod_acao):
                                xml_.append(f'\n{valorIndex}')
                            if index == 3:
                                xml_.append(f'{tela.enter_tela()}\n') 
                            controlador_3 +=1

            #Adicionando entradas nas telas a serem alteradas
            if controlador_3 == 1 or controlador_3 == 2:
                #Adicionando entradas na tela **1** e **2**           
                if qtd_registros_tela2 == 0: #Validando que Ñ HOUVE alteração tela 2
                    xml_.append(tela.acessando_t_10512_1())
                    xml_.append(tela.acessando_t_10512_2())
                    controlador_3 +=2
                #Adicionando entradas na tela **2**
                else:#Validando que HOUVE alteração na tela 1
                    xml_.append(tela.acessando_t_10512_2())
                    controlador_3 +=2

            #Adicionando os dados da serem alterarados
            for i, valor in enumerate(unindo_tela_valor_[index0][index1]):
                xml_.append(f'\n{valor}')
                #Adicionando a linha de deletar
                if i % 2 == 0:
                    xml_.append(tela.deletar_valor())                   

            #Adicionando o final da tela
            if planilha.list_rindex(telas_a_criar_[0],'t_10512_2') == index1:
                xml_.append(tela.finalizando_t_10512_1ou2())
                nr_tela +=1
                xml_.append(tela.rodape(nr_tela))

     #------------------------------[[[   4    ]]]----------------------------
        elif 't_1054'  == telas_a_criar_[index0][index1]:
            if controlador_4 == 0:
                qtd_registros_tela4 = telas_a_criar_[index0].count('t_1054')
                xml_.append(tela.cabecalhoScreen01(nr_tela,"false","false"))
                controlador_4 += 1

            #Carregando o código de açãodo e o Address quando houver alterações apenas na tela 1
            if controlador_4 == 1:
                if qtd_registros_tela1 > 2: #Validando que HOUVE alteração na tela 1
                    if qtd_registros_tela2 == 0: #Validando que Ñ HOUVE alteração tela 2
                        if qtd_registros_tela3 == 0: #Validando que Ñ HOUVE alteração tela 3
                            for index, valorIndex in enumerate(cod_acao):
                                xml_.append(f'\n{valorIndex}')
                            if index == 3:
                                xml_.append(f'{tela.enter_tela()}\n') 
                controlador_4 += 1

            #Está adicionando o shift + f2 para entrar na tela **2**
            if controlador_4 <= 2:
                xml_.append(tela.acessando_t_1054())
                controlador_4 += 2
            
                        #Adicionando os dados da serem alterarados
            for i, valor in enumerate(unindo_tela_valor_[index0][index1]):
                xml_.append(f'\n{valor}')
                #Adicionando a linha de deletar
                if i % 2 == 0:
                    xml_.append(tela.deletar_valor())

            #Adicionando o final da tela
            if planilha.list_rindex(telas_a_criar_[0],'t_1054') == index1:
                xml_.append(tela.finalizando_t_1054())
                nr_tela +=1
                xml_.append(tela.rodape(nr_tela))

     #------------------------------[[[   5    ]]]----------------------------
        elif 't_1053'  == telas_a_criar_[index0][index1]:
            if controlador_5 == 0:
                qtd_registros_tela5 = telas_a_criar_[index0].count('t_1053')
                xml_.append(tela.cabecalhoScreen01(nr_tela,"false","false"))
                controlador_5 += 1

            #Carregando o código de açãodo e o Address quando houver alterações apenas na tela 1
            if controlador_5 == 1:
                if qtd_registros_tela1 > 2: #Validando que HOUVE alteração na tela 1
                    if qtd_registros_tela2 == 0: #Validando que Ñ HOUVE alteração tela 2
                        if qtd_registros_tela3 == 0: #Validando que Ñ HOUVE alteração tela 3
                            if qtd_registros_tela4 == 0: #Validando que Ñ HOUVE alteração tela 4
                                for index, valorIndex in enumerate(cod_acao):
                                    xml_.append(f'\n{valorIndex}')
                                if index == 3:
                                    xml_.append(f'{tela.enter_tela()}\n') 
                controlador_5 += 1

            #Está adicionando o shift + f2 para entrar na tela **2**
            if controlador_5 <= 2:
                xml_.append(tela.acessando_t_1053())
                controlador_5 += 2 
            
            #Adicionando os dados da serem alterarados
            for i, valor in enumerate(unindo_tela_valor_[index0][index1]):
                xml_.append(f'\n{valor}')
                #Adicionando a linha de deletar
                if i % 2 == 0:
                    xml_.append(tela.deletar_valor())

            #Irá criar a tela de finalização da tela 5 apenas se não existir alterações na 6
            if telas_a_criar_[index0].count('t_1056') == 0:
                if planilha.list_rindex(telas_a_criar_[0],'t_1053') == index1:
                    xml_.append(tela.finalizando_t_1053())
                    nr_tela +=1
                    xml_.append(tela.rodape(nr_tela)) 
            else:
                if planilha.list_rindex(telas_a_criar_[0],'t_1053') == index1:
                    xml_.append(tela.finalizando_t_1053_2())


#------------------------------[[[   6    ]]]----------------------------
        elif  't_1056' == telas_a_criar_[index0][index1]:
            if controlador_6 == 0:
                if qtd_registros_tela5 == 0: # Se houver alteração na tela t_10512_1 não irei criar a chamada ta tela
                    xml_.append(tela.cabecalhoScreen01(nr_tela,"true","false"))
                    qtd_registros_tela6 = telas_a_criar_[index0].count('t_1056')
                    controlador_6 += 1
                else:
                    qtd_registros_tela6 = telas_a_criar_[index0].count('t_1056')
                    controlador_6 += 1

            #Carregando o código de açãodo e o Address quando houver alterações apenas na tela 1
            if controlador_6 == 1:
                if qtd_registros_tela1 > 2: #Validando que HOUVE alteração na tela 1
                    if qtd_registros_tela2 == 0: #Validando que Ñ HOUVE alteração tela 2
                        if qtd_registros_tela3 == 0: #Validando que Ñ HOUVE alteração tela 3
                            if qtd_registros_tela4 == 0: #Validando que Ñ HOUVE alteração tela 4
                                if qtd_registros_tela5 == 0: #Validando que Ñ HOUVE alteração tela 5
                                    for index, valorIndex in enumerate(cod_acao):
                                        xml_.append(f'\n{valorIndex}')
                                    if index == 3:
                                        xml_.append(f'{tela.enter_tela()}\n') 
                controlador_6 +=1

          

            #Adicionando entradas nas telas a serem alteradas
            if controlador_6 <= 2:
                #Adicionando entradas na tela **1** e **2**           
                if qtd_registros_tela5 == 0: #Validando que Ñ HOUVE alteração tela 2
                    xml_.append(tela.acessando_t_1053())
                    xml_.append(tela.acessando_t_1056())
                    controlador_6 +=2
                #Adicionando entradas na tela **2**
                else:#Validando que HOUVE alteração na tela 1
                    xml_.append(tela.acessando_t_1056())
                    controlador_6 +=2


            #Adicionando os dados da serem alterarados
            for i, valor in enumerate(unindo_tela_valor_[index0][index1]):
                xml_.append(f'\n{valor}')
                #Adicionando a linha de deletar
                if i % 2 == 0:
                    xml_.append(tela.deletar_valor())


            #Adicionando o final da tela
            if planilha.list_rindex(telas_a_criar_[0],'t_1056') == index1:
                xml_.append(tela.finalizando_t_1056())
                nr_tela +=1
                xml_.append(tela.rodape(nr_tela))

#------------------------------[[[   7    ]]]----------------------------
        elif 't_4206'  == telas_a_criar_[index0][index1]:
            if controlador_7 == 0:
                qtd_registros_tela5 = telas_a_criar_[index0].count('t_4206')
                xml_.append(tela.cabecalhoScreen01(nr_tela,"false","false"))
                controlador_7 += 1

            #Carregando o código de açãodo e o Address quando houver alterações apenas na tela 1
            if controlador_7 == 1:
                if qtd_registros_tela1 > 2: #Validando que HOUVE alteração na tela 1
                    if qtd_registros_tela2 == 0: #Validando que Ñ HOUVE alteração tela 2
                        if qtd_registros_tela3 == 0: #Validando que Ñ HOUVE alteração tela 3
                            if qtd_registros_tela4 == 0: #Validando que Ñ HOUVE alteração tela 4
                                if qtd_registros_tela5 == 0: #Validando que Ñ HOUVE alteração tela 5
                                    if qtd_registros_tela6 == 0: #Validando que Ñ HOUVE alteração tela 5                                    
                                        for index, valorIndex in enumerate(cod_acao):
                                            xml_.append(f'\n{valorIndex}')
                                        if index == 3:
                                            xml_.append(f'{tela.enter_tela()}\n') 
                controlador_7 +=1


            #Está adicionando o shift + f2 para entrar na tela **2**
            if controlador_7 <= 2:
                xml_.append(tela.acessando_t_4206())
                controlador_7 += 2 


            #Adicionando os dados da serem alterarados
            for i, valor in enumerate(unindo_tela_valor_[index0][index1]):
                xml_.append(f'\n{valor}')
                #Adicionando a linha de deletar
                if i % 2 == 0:
                    xml_.append(tela.deletar_valor())


            #Adicionando o final da tela
            if planilha.list_rindex(telas_a_criar_[0],'t_4206') == index1:
                xml_.append(tela.finalizando_t_4206())
                nr_tela +=1
                xml_.append(tela.rodape(nr_tela))




#------------------------------[[[   Historico    ]]]-------------------------
        if index1 == len(unindo_tela_valor_[index0])-1: # Colunas

            if index0 == len(unindo_tela_valor_)-1: # Linhas
                #Se entrar nesse laço significa que estou encerrando o código após finalizar
                xml_.append(tela.cabecalhoScreen01(nr_tela,'false','true'))
            else:
                xml_.append(tela.cabecalhoScreen01(nr_tela,'false','false'))

            #Carregando o código de açãodo e o Address quando houver alterações apenas na tela 1
            if qtd_registros_hist == 0:
                if qtd_registros_tela1 > 2: #Validando que HOUVE alteração na tela 1
                    if qtd_registros_tela2 == 0: #Validando que Ñ HOUVE alteração tela 2
                        if qtd_registros_tela3 == 0: #Validando que Ñ HOUVE alteração tela 3
                            if qtd_registros_tela4 == 0: #Validando que Ñ HOUVE alteração tela 4
                                if qtd_registros_tela5 == 0: #Validando que Ñ HOUVE alteração tela 5
                                    if qtd_registros_tela6 == 0: #Validando que Ñ HOUVE alteração tela 6
                                       if qtd_registros_tela7 == 0: #Validando que Ñ HOUVE alteração tela 6                                        
                                            for index, valorIndex in enumerate(cod_acao):
                                                xml_.append(f'\n{valorIndex}')
                                            if index == 3:
                                                xml_.append(f'{tela.enter_tela()}\n') 
                qtd_registros_hist +=1
      
                    
            xml_.append(tela.tela_historico(len(frase_historico_[index0]),frase_historico_[index0]))

            if index0 == len(unindo_tela_valor_)-1: # Linhas
                #Se entrar nesse laço significa que estou encerrando o código após finalizar
                xml_.append(tela.rodapeHash())
            else:
                nr_tela +=1
                xml_.append(tela.rodape(nr_tela))



#Salvando os dados em arquivo .mac
file2write=open('big9.mac','w')
c = 0
while c < len(xml_):
    #Ignorando as linhas em branco na hora de carregar no arquivo.
    file2write.write(xml_[c])
    c += 1

print('\n'+'=-'*20)
print('    Código executado com sucesso!')
print('=-'*20)