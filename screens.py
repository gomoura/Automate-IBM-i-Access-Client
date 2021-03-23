def cabecalhoHash():
    return '''<HAScript name="ENTER" description="" timeout="60000" pausetime="300" promptall="true" blockinput="false" author="d510098" creationdate="Jan 7, 2021 5:06:57 PM" supressclearevents="false" usevars="true" ignorepauseforenhancedtn="true" delayifnotenhancedtn="0" ignorepausetimeforenhancedtn="true" continueontimeout="false">

<vars>
    <create name="$a1$" type="string" value="&apos; &apos;" />
</vars>\n'''

def validador_tela():
    return '<prompt name="&apos;Ok or Cancel&apos;" description="" row="0" col="0" len="150" default="" clearfield="false" encrypted="false" movecursor="true" xlatehostkeys="true" assigntovar="" varupdateonly="false" required="false" title="&apos;Tela 01051?&apos;" />'

def cabecalhoScreen01(nrTela = 0,entradaTela="true",saidaTela="false"):
    return f'''\n
<screen name="Screen{nrTela}" entryscreen="{entradaTela}" exitscreen="{saidaTela}" transient="false">
<description >
    <oia status="NOTINHIBITED" optional="false" invertmatch="false" />
</description>

<actions>\n'''


def deletar_valor():
    return '\n<input value="&apos;[deleteword][deleteword][deleteword][deleteword][deleteword][deleteword][deleteword][deleteword][deleteword][deleteword]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />'

def enter_tela():
    return '''\n<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="250"/>'''

#----------------------t__1051
def final_tela_1051():
    return '''\n<!--Alterando dados na tela 1051-->
<pause value="100"/>
<mouseclick row = "4" col = "19"/>
<input value="&apos;c[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<!--Alterando dados na tela 1051-->\n'''
#----------------------------------------------------

#----------------------t_10512_1
def acessando_t_10512_1():
    return f'''\n<!--Acessando a tela t_10512_1-->
<pause value="250"/>
<input value="&apos;[pf14]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="1000"/>
<!--Acessando a tela t_10512_1-->'''

def acessando_t_10512_2():
    return f'''\n<!--Acessando a tela t_10512_2-->
<input value="&apos;[pagedn]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="150"/>
<!--Acessando a tela t_10512_2-->'''

def finalizando_t_10512_1ou2():
    return f''' \n<!--Finalizando a tela t_10512_1-->
<pause value="150"/>
<mouseclick row="3" col="19" />
<pause value="150"/>
<input value="&apos;C&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="100"/>
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="250"/>
<input value="&apos;[pf3]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<!--Finalizando a tela t_10512_1-->'''

#----------------------------------------------------

#----------------------t_1054
def acessando_t_1054():
    return f'''\n<!--Acessando a tela t_1054-->
<pause value="250"/>
<input value="&apos;[pf16]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="1000"/>
<!--Acessando a tela t_1054-->'''


def finalizando_t_1054():
    return f''' \n<!--Finalizando a tela t_1054-->
<pause value="150"/>
<mouseclick row="3" col="19" />
<pause value="150"/>
<input value="&apos;C&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="100"/>
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="250"/>
<input value="&apos;[pf3]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<!--Finalizando a tela t_1054-->'''
#----------------------t_1054


#----------------------t_1053
def acessando_t_1053():
    return f'''\n<!--Acessando a tela t_1053-->
<pause value="250"/>
<input value="&apos;[pf15]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="1250"/>
<!--Acessando a tela t_1053-->'''


def finalizando_t_1053():
    return f''' \n<!--Finalizando a tela t_1053-->
<pause value="150"/>
<mouseclick row="2" col="19" />
<pause value="150"/>
<input value="&apos;C&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="100"/>
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="250"/>
<input value="&apos;[pf3]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<!--Finalizando a tela t_1053-->'''

def finalizando_t_1053_2():
    return f''' \n<!--Finalizando a tela t_1053-->
<pause value="150"/>
<mouseclick row="2" col="19" />
<pause value="150"/>
<input value="&apos;C&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="100"/>
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="250"/>
<!--Finalizando a tela t_1053-->'''
#----------------------t_1053


#----------------------t_1056
def acessando_t_1056():
    return f'''\n<!--Acessando a tela t_1056-->
<pause value="250"/>
<input value="&apos;[pf17]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="1250"/>
<!--Acessando a tela t_1056-->'''


def finalizando_t_1056():
    return f''' \n<!--Finalizando a tela t_1056-->
<pause value="150"/>
<mouseclick row="3" col="19" />
<pause value="150"/>
<input value="&apos;C&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="100"/>
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="250"/>
<input value="&apos;[pf3]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="550"/>
<input value="&apos;[pf3]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="550"/>
<input value="&apos;[pf3]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="550"/>
<!--Finalizando a tela t_1056-->'''
#----------------------t_1056

#----------------------t_4206
def acessando_t_4206():
    return f'''\n<!--Acessando a tela t_4206-->
<pause value="250"/>
<input value="&apos;[pf23]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="1000"/>
<!--Acessando a tela t_4206-->'''

def finalizando_t_4206():
    return f''' \n<!--Finalizando a tela t_4206-->
<pause value="150"/>
<mouseclick row="3" col="28" />
<pause value="150"/>
<input value="&apos;C&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="100"/>
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="250"/>
<input value="&apos;[pf3]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="550"/>
<!--Finalizando a tela t_4206-->'''
#----------------------t_4206


def rodape(proximaTela=0):
    return f'''<!--Rodapé p/ próxima tela-->
</actions>
<nextscreens timeout="0" >
    <nextscreen name="Screen{proximaTela}" />
</nextscreens>
</screen>\n'''


def rodapeHash():
    return f'''
</actions>
<nextscreens timeout="0" >
</nextscreens>
</screen>
</HAScript>\n'''

#------------------------------------------------
def tela_historico(hist,frase_historico_):
    
    if hist <= 80:
        espaco = " " * 80
        srow = 22

    elif hist > 80 and hist <= 160 :
        espaco = " " * (80*2)
        srow = 21

    elif hist > 160 and hist <= 240:
        espaco = " " * (80*3)
        srow = 20

    elif hist > 240 and hist <= 320:
        espaco = " " * (80*4)
        srow = 19

    elif hist > 320 and hist <= 400:
        espaco = " " * (80*5)
        srow = 18

    elif hist > 400 and hist <= 480:
        espaco = " " * (80*6)
        srow = 17

    elif hist > 480 and hist <= 560:
        espaco = " " * (80*7)
        srow = 16

    elif hist > 560 and hist <= 640:
        espaco = " " * (80*8)
        srow = 15

    elif hist > 640 and hist <= 720:
        espaco = " " * (80*9)
        srow = 14

    elif hist > 720 and hist <= 800:
        espaco = " " * (80*10)
        srow = 13

    elif hist > 800 and hist <= 880:
        espaco = " " * (80*11)
        srow = 12

    elif hist > 880 and hist <= 960:
        espaco = " " * (80*12)
        srow = 11

    trecho1 = 5 *f'''\n<extract name="&apos;vazio&apos;" planetype="TEXT_PLANE" srow="{srow}" scol="1" erow="22" ecol="80" unwrap="false" continuous="false" assigntovar="$a1$" />
<if condition="$a1$ != &apos;{espaco}&apos;" >
<pause value="350" />
<input value="&apos;[pagedn]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="550" />
</if>\n'''


    trecho2 = f'''\n<input value="&apos;[pf6]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="800" />\n {trecho1}\n    

<extract name="&apos;vazio&apos;" planetype="TEXT_PLANE" srow="7" scol="1" erow="7" ecol="80" unwrap="false" continuous="false" assigntovar="$a1$" />
<if condition="$a1$ == &apos;                                                                                &apos;" >  
<input value="&apos;[eof]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="750"/>
</if>
<else>
<input value="&apos;[eof][newline]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="750"/>
</else>
<input value="&apos;{frase_historico_}&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<pause value="250" />
<input value="&apos;[enter]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
<input value="&apos;[pf3]&apos;" row="0" col="0" movecursor="true" xlatehostkeys="true" encrypted="false" />
\n'''

    return trecho2

