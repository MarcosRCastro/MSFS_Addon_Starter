import os
from tkinter.ttk import *
from tkinter import *
import webbrowser as wb
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from pathlib import Path
import pyperclip as pc
import win32com.client as win32
import datetime as date


 
# Variáveis
local_programa = Path.home() / 'MSFS_Manager'


caminho_01 = local_programa / 'caminho_01.txt'
caminho_02 = local_programa / 'caminho_02.txt'
caminho_03 = local_programa / 'caminho_03.txt'
caminho_04 = local_programa / 'caminho_04.txt'
caminho_05 = local_programa / 'caminho_05.txt'
caminho_06 = local_programa / 'caminho_06.txt'
idioma_salvo = local_programa / 'idioma.txt'



############## Funçoes ###################

# Verificar se é primeira inicialização
def primeira_inicializacao():
    primeira_ini = local_programa
    if primeira_ini.exists():
        print('Não é a primeira inicialização')
        with open(idioma_salvo, 'r') as arquivo:
            idioma_local = arquivo.readlines()
        global idioma
        idioma = idioma_local
        return

    else:
        os.mkdir(local_programa)
        primeira_escolha_idioma()

# Função para esscolha de idioma do programa
def primeira_escolha_idioma():
    janela_escolha_idioma = Tk()
    janela_escolha_idioma.title('Language')
    janela_escolha_idioma.geometry('300x150+620+335')
    janela_escolha_idioma.resizable(False, False)
    Label(janela_escolha_idioma, text="Choose language:").place(x=50,y=20,width=200,height=30)
    
  
    botao_ingles = Button(janela_escolha_idioma, text='English', command=lambda: [idioma_ingles(), janela_escolha_idioma.destroy()]).place(x=50,y=80,width=80,height=30)
    botao_portugues =  Button(janela_escolha_idioma, text='Português', command=lambda: [idioma_portugues(), janela_escolha_idioma.destroy()]).place(x=170,y=80,width=80,height=30)

    janela_escolha_idioma.mainloop()
    
# Escolha de idioma para portugues
def idioma_portugues():
    global idioma
    idioma = 0
    with open(idioma_salvo, 'w') as arquivo:
        arquivo.write('0')
    mensagem_boas_vindas()
    

# Escolha de idioma para ingles
def idioma_ingles():
    global idioma
    idioma = 1
    with open(idioma_salvo, 'w') as arquivo:
        arquivo.write('1')
    mensagem_boas_vindas()
    

# Mensagem de boas vindas na primeira inicialização
def mensagem_boas_vindas():
  
    if idioma == 0:
        bem_vindo = messagebox.showinfo(
            message='Seja bem vindo ao MSFS Manager!\n\n'
            'Este programa está em desenvolvimento, assim, provavelmente durante sua utilização você encontre alguns erros. Peço que nos informe sempre que encontrar um problema e sempre que tiver uma ideia ou sugestão.\n\n'
            'Bons voos, Comandante!!',
            title='Olá!'
        )
        return
    if idioma == 1:
        bem_vindo = messagebox.showinfo(
            message='Welcome to MSFS Manager!\n\n'
            "This program is in development, so, it's possible to show some error during use. Please, let us know if something wrong happens..\n\n"
            "Have good flights!!",
            title="Hello!"
        )
        return



# Janela configurações
def configuracoes():
    janela_configuracoes = Tk()
    janela_configuracoes.title('Configurações')
    janela_configuracoes.geometry('500x350+520+220')
    janela_configuracoes.resizable(False, False)

    # Idioma
    label_escolha_de_idioma = Label(janela_configuracoes, text='Escolha o idioma:', anchor=W).place(x=10,y=20,width=200,height=30)
    var_idioma = StringVar()
    escolher_idioma = Combobox(janela_configuracoes)
    escolher_idioma.place(x=250,y=20,width=120,height=30)
    escolher_idioma['values'] = ('Inglês','Português')
    escolher_idioma.current(1)

    iniciar_com_windows = Label(janela_configuracoes, text='Iniciar com o Windows:', anchor=W).place(x=10,y=60,width=200,height=30)
    var_iniciar_com_windows = StringVar()
    iniciar_com_windows = Combobox(janela_configuracoes)
    iniciar_com_windows.place(x=250,y=60,width=120,height=30)
    iniciar_com_windows['values'] = ('Sim','Não')
    iniciar_com_windows.current(1)

    iniciar_programas_auto = Label(janela_configuracoes, text='Abrir todos programas ao executar\no MSFS Manager:', anchor=W, justify=LEFT).place(x=10,y=100,width=200,height=30)
    var_iniciar_programas_auto = StringVar()
    iniciar_programas_auto = Combobox(janela_configuracoes)
    iniciar_programas_auto.place(x=250,y=100,width=120,height=30)
    iniciar_programas_auto['values'] = ('Sim','Não')
    iniciar_programas_auto.current(1)
    
    cor_de_fundo = Label(janela_configuracoes, text='Cor de fundo:', anchor=W, justify=LEFT).place(x=10,y=140,width=200,height=30)
    var_iniciar_programas_auto = StringVar()
    iniciar_programas_auto = Combobox(janela_configuracoes)
    iniciar_programas_auto.place(x=250,y=140,width=120,height=30)
    iniciar_programas_auto['values'] = ('Claro','Escuro')
    iniciar_programas_auto.current(1)


    botao_cancelar = Button(janela_configuracoes, text='Cancelar', command= lambda: janela_configuracoes.destroy()).place(x=270,y=300,width=100,height=30)
    #botao_confirmar = Button(janela_configuracoes, text='Confirmar').place(x=380,y=300,width=100,height=30)


# Janela reportar Bug     
def reportar_bug():
    janela_email_bug = Tk()
    janela_email_bug.title('Alerta de Bug')
    janela_email_bug.geometry('500x150+520+220')
    janela_email_bug.resizable(False, False)
    
    # Português
    if idioma == 0:
        Label(janela_email_bug, text="Explique o erro abaixo:").place(x=140,y=20,width=200,height=30)
    
        texto = Entry(janela_email_bug)
        texto.place(x=20,y=60,width=460,height=30)
        

        botao_enviar = Button(janela_email_bug, text='Enviar', command= lambda: enviar_texto_bug(texto)).place(x=420,y=110,width=60,height=30)
        botao_cancelar = Button(janela_email_bug, text='Cancelar', command= lambda: janela_email_bug.destroy()).place(x=350,y=110,width=60,height=30)
    
    # Inglês
    if idioma == 1:
        Label(janela_email_bug, text="Explain the error:").place(x=140,y=20,width=200,height=30)
    
        texto = Entry(janela_email_bug)
        texto.place(x=20,y=60,width=460,height=30)
        

        botao_enviar = Button(janela_email_bug, text='Send', command= lambda: enviar_texto_bug(texto)).place(x=420,y=110,width=60,height=30)
        botao_cancelar = Button(janela_email_bug, text='Cancel', command= lambda: janela_email_bug.destroy()).place(x=350,y=110,width=60,height=30)


# Janela para fazer sugestão
def sugestao():
    janela_sugestao = Tk()
    janela_sugestao.title('Deixe aqui sua sugestão')
    janela_sugestao.geometry('500x350+520+220')
    janela_sugestao.resizable(False, False)

    info = Label(janela_sugestao, text='Deixe sua ideia ou sugestão abaixo:').place(x=20,y=20,width=430,height=30)
    
    texto = Entry(janela_sugestao)
    texto.place(x=20,y=60,width=460,height=30)
    
    
    botao_enviar = Button(janela_sugestao, text='Enviar', command= lambda: enviar_texto_bug(texto)).place(x=420,y=300,width=60,height=30)
    botao_cancelar = Button(janela_sugestao, text='Cancelar', command= lambda: janela_sugestao.destroy()).place(x=350,y=300,width=60,height=30)
    


# Função enviar texto na página de avisar sobre bug

def enviar_texto_bug(texto): ##### Não está funcionando
    # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')
    # criar um email
    email = outlook.CreateItem(0)
    # configurar as informações do seu e-mail
    email.To = 'maarquinhoo@outlook.com.br'
    email.Subject = ('Reporte de erro - MSFS Manager | ' + date.today())
    email.HTMLBody = texto.get()
    email.Send()
    messagebox.showinfo(message='Reporte de erro enviado. Obrigado pela dedicação.')
    print('E-mail enviado!')


# Função enviar sugestão na página sugestão
def enviar_sugestao(texto): ##### Não está funcionando
    # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')
    # criar um email
    email = outlook.CreateItem(0)
    # configurar as informações do seu e-mail
    email.To = 'maarquinhoo@outlook.com.br'
    email.Subject = ('Sugestão para MSFS Manager | ' + date.today())
    email.HTMLBody = '''Teste teste teste'''
    email.Send()
    messagebox.showinfo(message='Sugestão enviada. Obrigado pela dedicação.')



# Janela "Sobre"
def sobre():
    janela_sobre = Tk()
    janela_sobre.title('Sobre o MSFS Manager')
    janela_sobre.geometry('500x350+520+220')
    janela_sobre.resizable(False, False)

    # Inglês
    if idioma == 0:
        janela_sobre.title('About the MSFS Manager')
        info = Label(janela_sobre, text='The "Microsoft Flight Simulator Manager (MSFS Manager)" was created by\n'
                                        'Marcos Castro in order to facilitate the opening of all programs\n'
                                        'used for Flight Simulation. This is the Alpha version of the MSFS Manager\n'
                                        'and soon will receive a lot of new functionalities.\n\n'
                                        'If you have some idea, improovment suggestions for this software, please,\n'
                                        'let us know, because we want it to be the best possible for you.\n\n'
                                        'This software was created to be used with MSFS, but it also can\n'
                                        'be used to open any software you want. So use and abuse.\n\n'
                                        'If you want to help in this software development, besides sending us\n'
                                        'suggestions and bug reports, make us a donation. Any amount will be welcome..').place(x=20,y=5,width=450,height=250)

        botao_voltar = Button(janela_sobre,text='Return',command = lambda: janela_sobre.destroy()).place(x=120,y=250,width=120,height=30)
        botao_reportar_bug = Button(janela_sobre,text='Bug reports',command=lambda:reportar_bug()).place(x=270,y=250,width=120,height=30)
        botao_sugestao = Button(janela_sobre, text='Suggestions', command= lambda: sugestao()).place(x=120,y=290,width=120,height=30)
        botao_doacao = Button(janela_sobre, text='Donations', command=lambda: janela_pix()).place(x=270,y=290,width=120,height=30)

    # Português
    if idioma == 1:
        info = Label(janela_sobre, text='O "Microsoft Flight Simulator Manager (MSFS Manager)" foi criado pelo programador\n'
                                        'Marcos Castro com o intuito de facilitar a abertura de todos os programas\n'
                                        'utilizados para a simulação de voo. A versão Alpha do MSFS Manager\n'
                                        'é a atual versão e ainda contará com muitas melhorias.\n\n'
                                        'Se você tem alguma ideia, sugestão para melhoria do programa não\n'
                                        'deixe de nos enviar, pois queremos que ele seja o melhor possível para\n'
                                        'você.\n\n'
                                        'Lembrando que o MSFS Manager foi criado para o MSFS, porém pode\n'
                                        'ser usado para abrir quaisquer programas que você quiser. Então, use e abuse.\n\n'
                                        'Se você quiser ajudar no desenvolvimento deste programa, além de nos enviar\n'
                                        'sugestões e reporte de bugs, faça-nos uma doação. Qualquer valor será bem vindo.').place(x=20,y=5,width=450,height=250)

        botao_voltar = Button(janela_sobre,text='Voltar',command = lambda: janela_sobre.destroy()).place(x=120,y=250,width=120,height=30)
        botao_reportar_bug = Button(janela_sobre,text='Reportar bug',command=lambda:reportar_bug()).place(x=270,y=250,width=120,height=30)
        botao_sugestao = Button(janela_sobre, text='Enviar sugestão', command= lambda: sugestao()).place(x=120,y=290,width=120,height=30)
        botao_doacao = Button(janela_sobre, text='Fazer doação', command=lambda: janela_pix()).place(x=270,y=290,width=120,height=30)



# Função de doação em formato de PIX
def janela_pix():
    janela_pix = Tk()
    janela_pix.title('Dados do PIX')
    janela_pix.geometry('500x350+520+220')
    janela_pix.resizable(False, False)
    
    # Inglês
    if idioma == 0:
        codigo = '69482510-6503-4a5c-af1a-e4b4c8ee9e4f'
        info = Label(janela_pix, text='Use a chave PIX abaixo para fazer uma doação.\n' 
                                        'Ajude-nos a comprar um café, até porque códigos não\n'
                                        'existem sem boas doses de cafeína.\n\n').place(x=30,y=20,width=430,height=120)
        info02 = Label(janela_pix, text='69482510-6503-4a5c-af1a-e4b4c8ee9e4f').place(x=30,y=100,width=430,height=120)
        botao_copiar = Button(janela_pix, text='Copiar', command= lambda: pc.copy(codigo)).place(x=200,y=290,width=120,height=30)
        botao_voltar = Button(janela_pix, text='Voltar', command= lambda: janela_pix.destroy()).place(x=340,y=290,width=120,height=30)

    # Português
    if idioma == 1:
        codigo = '69482510-6503-4a5c-af1a-e4b4c8ee9e4f'
        info = Label(janela_pix, text='Use a chave PIX abaixo para fazer uma doação.\n' 
                                        'Ajude-nos a comprar um café, até porque códigos não\n'
                                        'existem sem boas doses de cafeína.\n\n').place(x=30,y=20,width=430,height=120)
        info02 = Label(janela_pix, text='69482510-6503-4a5c-af1a-e4b4c8ee9e4f').place(x=30,y=100,width=430,height=120)
        botao_copiar = Button(janela_pix, text='Copiar', command= lambda: pc.copy(codigo)).place(x=200,y=290,width=120,height=30)
        botao_voltar = Button(janela_pix, text='Voltar', command= lambda: janela_pix.destroy()).place(x=340,y=290,width=120,height=30)

# Escolher caminho
# Abrir pastar para escolher o   caminho do programa
def escolher_caminho_01():
    filename = filedialog.askopenfilename()
    print(filename)
    if len(filename) > 3:
        if idioma == 0:
            with open(caminho_01, 'w') as arquivo:
                arquivo.write('%s' % filename)
                arquivo.write('\n')
                texto = filename
                caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
                botao_excluir_programa_01 = Button(root,text='Delete',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
                botao_abrir_programa_01 = Button(root,text='Open',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)
        if idioma == 1:
            with open(caminho_01, 'w') as arquivo:
                arquivo.write('%s' % filename)
                arquivo.write('\n')
                texto = filename
                caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
                botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
                botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)
        
    else:
        return

def escolher_caminho_02():
    filename = filedialog.askopenfilename()
    print(filename)
    if len(filename) > 3:
        with open(caminho_02, 'w') as arquivo:
            arquivo.write('%s' % filename)
            arquivo.write('\n')
            texto = filename
            caminho = Label(root,text=texto).place(x=110,y=120,width=430,height=30)
            botao_excluir_programa_02 = Button(root,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
            botao_abrir_programa_02 = Button(root,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)
    else:
        return
        
def escolher_caminho_03():
    filename = filedialog.askopenfilename()
    print(filename)
    if len(filename) > 3:        
        with open(caminho_03, 'w') as arquivo:
            arquivo.write('%s' % filename)
            arquivo.write('\n')
            texto = filename
            caminho = Label(root,text=texto).place(x=110,y=160,width=430,height=30)
            botao_excluir_programa_03 = Button(root,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
            botao_abrir_programa_03 = Button(root,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)
    else:
        return

def escolher_caminho_04():
    filename = filedialog.askopenfilename()
    print(filename)
    if len(filename) > 3:
        with open(caminho_04, 'w') as arquivo:
            arquivo.write('%s' % filename)
            arquivo.write('\n')
            texto = filename
            caminho = Label(root,text=texto).place(x=110,y=200,width=430,height=30)
            botao_excluir_programa_04 = Button(root,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
            botao_abrir_programa_04 = Button(root,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)
    else:
        return

def escolher_caminho_05():
    filename = filedialog.askopenfilename()
    print(filename)
    if len(filename) > 3:
        with open(caminho_05, 'w') as arquivo:
            arquivo.write('%s' % filename)
            arquivo.write('\n')
            texto = filename
            caminho = Label(root,text=texto).place(x=110,y=240,width=430,height=30)
            botao_excluir_programa_05 = Button(root,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
            botao_abrir_programa_05 = Button(root,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)
    else:
        return

def escolher_caminho_06():
    filename = filedialog.askopenfilename()
    print(filename)
    if len(filename) > 3:
        with open(caminho_06, 'w') as arquivo:
            arquivo.write('%s' % filename)
            arquivo.write('\n')
            texto = filename
            caminho = Label(root,text=texto).place(x=110,y=280,width=430,height=30)
            botao_excluir_programa_06 = Button(root,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
            botao_abrir_programa_06 = Button(root,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)
    else:
        return
    

#Salvar caminho 01
def salvar_caminho_01(caminho):
    
    texto = caminho.get()
    if len(texto) < 3:
        alerta = messagebox.showinfo(
        message='Por favor, insira um caminho válido!',
        title='Atenção!'
        )
    else:
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)
        with open(caminho_01, 'w') as arquivo:
            arquivo.write('%s' % texto)
            

#Salvar caminho 02
def salvar_caminho_02(caminho):

    texto = caminho.get()
    if len(texto) < 3:
        alerta = messagebox.showinfo(
        message='Por favor, insira um caminho válido!',
        title='Atenção!'
        )
    else:
        caminho = Label(root,text=texto).place(x=110,y=120,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)
        with open(caminho_02, 'w') as arquivo:
            arquivo.write('%s' % texto)
            


#Salvar caminho 03
def salvar_caminho_03(caminho):

    texto = caminho.get()
    if len(texto) < 3:
        alerta = messagebox.showinfo(
        message='Por favor, insira um caminho válido!',
        title='Atenção!'
        )
    else:
        caminho = Label(root,text=texto).place(x=110,y=160,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)
        with open(caminho_03, 'w') as arquivo:
            arquivo.write('%s' % texto)
            

#Salvar caminho 04
def salvar_caminho_04(caminho):
    
    texto = caminho.get()
    if len(texto) < 3:
        alerta = messagebox.showinfo(
        message='Por favor, insira um caminho válido!',
        title='Atenção!'
        )
    else:
        caminho = Label(root,text=texto).place(x=110,y=200,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)
        with open(caminho_04, 'w') as arquivo:
            arquivo.write('%s' % texto)
            

#Salvar caminho 05
def salvar_caminho_05(caminho):
    
    texto = caminho.get()
    if len(texto) < 3:
        alerta = messagebox.showinfo(
        message='Por favor, insira um caminho válido!',
        title='Atenção!'
            )
    else:
        caminho = Label(root,text=texto).place(x=110,y=240,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)
        with open(caminho_05, 'w') as arquivo:
            arquivo.write('%s' % texto)
            
        
#Salvar caminho 06
def salvar_caminho_06(caminho):
    
    texto = caminho.get()
    if len(texto) < 3:
        alerta = messagebox.showinfo(
        message='Por favor, insira um caminho válido!',
        title='Atenção!'
            )
    else:
        caminho = Label(root,text=texto).place(x=110,y=280,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)
        with open(caminho_06, 'w') as arquivo:
            arquivo.write('%s' % caminho.get())
            


# Procurar caminho
# Procurar caminho 01
def procurar_caminnho_01():
    with open(caminho_01, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        if len(texto) > 3:      
            caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
            botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
            botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)
        else:
            return


# Procurar caminho 02
def procurar_caminnho_02():
    with open(caminho_02, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=120,width=430,height=30)
        botao_excluir_programa_02 = Button(root,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_02 = Button(root,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 03
def procurar_caminnho_03():
    with open(caminho_03, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=160,width=430,height=30)
        botao_excluir_programa_03 = Button(root,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_03 = Button(root,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 04
def procurar_caminnho_04():
    with open(caminho_04, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=200,width=430,height=30)
        botao_excluir_programa_04 = Button(root,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_04 = Button(root,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 05
def procurar_caminnho_05():
    with open(caminho_06, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=240,width=430,height=30)
        botao_excluir_programa_05 = Button(root,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_05 = Button(root,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 06
def procurar_caminnho_06():
    with open(caminho_06, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=280,width=430,height=30)
        botao_excluir_programa_06 = Button(root,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_06 = Button(root,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=80,width=60,height=30)



# Excluir caminho 01
def excluir_caminho_01():
    botao_inserir_programa_01 = Button(root, text='Inserir', command = lambda: salvar_caminho_01(caminho_programa_01)).place(x=550,y=80,width=60,height=30)
    caminho_programa_01 = Entry(root)
    caminho_programa_01.place(x=110,y=80,width=430,height=30)
    botao_abrir_programa_01 = Button(root,text='').place(x=620,y=80,width=60,height=30)
    botao_procurar_programa_01 = Button(root, text='Procurar', command = lambda: escolher_caminho_01()).place(x=620,y=80,width=60,height=30)
    os.remove(caminho_01)

# Excluir caminho 02
def excluir_caminho_02():
    botao_inserir_programa_02 = Button(root, text='Inserir', command = lambda: salvar_caminho_02(caminho_programa_02)).place(x=550,y=120,width=60,height=30)
    caminho_programa_02 = Entry(root)
    caminho_programa_02.place(x=110,y=120,width=430,height=30)
    botao_abrir_programa_02 = Button(root,text='').place(x=620,y=120,width=60,height=30)
    botao_procurar_programa_02 = Button(root, text='Procurar', command = lambda: escolher_caminho_02()).place(x=620,y=120,width=60,height=30)
    os.remove(caminho_02)

# Excluir caminho 03
def excluir_caminho_03():
    botao_inserir_programa_03 = Button(root, text='Inserir', command = lambda: salvar_caminho_03(caminho_programa_03)).place(x=550,y=160,width=60,height=30)
    caminho_programa_03 = Entry(root)
    caminho_programa_03.place(x=110,y=160,width=430,height=30)
    botao_abrir_programa_03 = Button(root,text='').place(x=620,y=160,width=60,height=30)
    botao_procurar_programa_03 = Button(root, text='Procurar', command = lambda: escolher_caminho_03()).place(x=620,y=160,width=60,height=30)
    os.remove(caminho_03)

# Excluir caminho 04
def excluir_caminho_04():
    botao_inserir_programa_04 = Button(root, text='Inserir', command = lambda: salvar_caminho_04(caminho_programa_04)).place(x=550,y=200,width=60,height=30)
    caminho_programa_04 = Entry(root)
    caminho_programa_04.place(x=110,y=200,width=430,height=30)
    botao_abrir_programa_04 = Button(root,text='').place(x=620,y=200,width=60,height=30)
    botao_procurar_programa_04 = Button(root, text='Procurar', command = lambda: escolher_caminho_04()).place(x=620,y=200,width=60,height=30)
    os.remove(caminho_04)

# Excluir caminho 05
def excluir_caminho_05():
    botao_inserir_programa_05 = Button(root, text='Inserir', command = lambda: salvar_caminho_05(caminho_programa_05)).place(x=550,y=240,width=60,height=30)
    caminho_programa_05 = Entry(root)
    caminho_programa_05.place(x=110,y=240,width=430,height=30)
    botao_abrir_programa_05 = Button(root,text='').place(x=620,y=240,width=60,height=30)
    botao_procurar_programa_05 = Button(root, text='Procurar', command = lambda: escolher_caminho_05()).place(x=620,y=240,width=60,height=30)
    os.remove(caminho_05)

# Excluir caminho 06
def excluir_caminho_06():
    botao_inserir_programa_06 = Button(root, text='Inserir', command = lambda: salvar_caminho_06(caminho_programa_06)).place(x=550,y=280,width=60,height=30)
    caminho_programa_06 = Entry(root)
    caminho_programa_06.place(x=110,y=280,width=430,height=30)
    botao_abrir_programa_06 = Button(root,text='').place(x=620,y=280,width=60,height=30)
    botao_procurar_programa_06 = Button(root, text='Procurar', command = lambda: escolher_caminho_06()).place(x=620,y=280,width=60,height=30)
    os.remove(caminho_06)



# Abrir programa 01
def abrir_programa_01():
    with open(caminho_01, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 02
def abrir_programa_02():
    with open(caminho_02, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 03
def abrir_programa_03():
    with open(caminho_03, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 04
def abrir_programa_04():
    with open(caminho_04, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 05
def abrir_programa_05():
    with open(caminho_05, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 06
def abrir_programa_06():
    with open(caminho_06, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir todos os programas
def abrir_todos():
    if os.path.exists(caminho_01):
        with open(caminho_01, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(caminho_02):
        with open(caminho_02, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(caminho_03):
        with open(caminho_03, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(caminho_04):
        with open(caminho_04, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(caminho_05):
        with open(caminho_05, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(caminho_06):
        with open(caminho_06, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])
        
    else:
        alerta = messagebox.showinfo(
        message='Por favor, insira o caminho de algum programa para que seja aberto!',
        title='Atenção!'
            )


# Função do botão ajuda
def ajuda():
    wb.open('https://www.youtube.com/channel/UCLqxFVkks6-nwKirjQBuRUQ')




############### Programa ##############

idioma = 1
primeira_inicializacao()

# Criar root principal
root = Tk()
root.title('MSFS Manager')
root.geometry('700x400+440+200')
root.resizable(False, False)


# Menu

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(root, tearoff=False)
file_menu.add_command(label='Configurações',command=lambda:configuracoes(), foreground='#808080')
file_menu.add_command(label='Sair',command=root.destroy)

menubar.add_cascade(
    label="Arquivo",
    menu=file_menu,
    underline=0
)
options_menu = Menu(
    menubar,
    tearoff=0
)

options_menu.add_command(label='Idioma', foreground='#808080')
options_menu.add_command(label='Deixar sugestão', foreground='#808080')
options_menu.add_command(label='Reportar bug', foreground='#808080')

menubar.add_cascade(
    label="Opções",
    menu=options_menu
)
help_menu = Menu(
    menubar,
    tearoff=0
)
help_menu.add_command(label='Café?!', command=lambda: janela_pix())
help_menu.add_command(label='Ajuda',  command = lambda: ajuda())
help_menu.add_command(label='Sobre...', command= lambda: sobre())

menubar.add_cascade(
    label="Ajuda",
    menu=help_menu
)



# Texto inicial do programa
if idioma == 0:
    texto_janela_inicial = Label(root, text = 'Inclua todos os programas que deseja abrir com o MSFS Manager')
    texto_janela_inicial.place(x=140,y=30)
if idioma == 1:
    texto_janela_inicial = Label(root, text = 'Select every program you want to open with MSFS Manager')
    texto_janela_inicial.place(x=140,y=30)


# Programa 01
if os.path.exists(caminho_01):
    with open(caminho_01, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        label_programa_01 = Label(root,text='Programa 01:',anchor=W).place(x=10,y=80,width=110,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)
        
else:
    label_programa_01 = Label(root,text='Programa 01:',anchor=W).place(x=10,y=80,width=110,height=30)
    botao_inserir_programa_01 = Button(root, text='Inserir', command = lambda: salvar_caminho_01(caminho_programa_01)).place(x=550,y=80,width=60,height=30)
    botao_procurar_programa_01 = Button(root, text='Procurar', command = lambda: escolher_caminho_01()).place(x=620,y=80,width=60,height=30)

    caminho_programa_01 = Entry(root)
    caminho_programa_01.place(x=110,y=80,width=430,height=30)

# Programa 02
if os.path.exists(caminho_02):
    with open(caminho_02, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=120,width=430,height=30)
        label_programa_02 = Label(root,text='Programa 02:',anchor=W).place(x=10,y=120,width=110,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)
        
else:
    label_programa_02 = Label(root,text='Programa 02:',anchor=W).place(x=10,y=120,width=110,height=30)
    botao_inserir_programa_02 = Button(root, text='Inserir', command = lambda: salvar_caminho_02(caminho_programa_02)).place(x=550,y=120,width=60,height=30)
    botao_procurar_programa_02 = Button(root, text='Procurar', command = lambda: escolher_caminho_02()).place(x=620,y=120,width=60,height=30)

    caminho_programa_02 = Entry(root)
    caminho_programa_02.place(x=110,y=120,width=430,height=30)

# Programa 03
if os.path.exists(caminho_03):
    with open(caminho_03, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=160,width=430,height=30)
        label_programa_03 = Label(root,text='Programa 03:',anchor=W).place(x=10,y=160,width=110,height=30)
        botao_excluir_programa_03 = Button(root,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
        botao_abrir_programa_03 = Button(root,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)
        
else:
    label_programa_03 = Label(root,text='Programa 03:',anchor=W).place(x=10,y=160,width=110,height=30)
    botao_inserir_programa_03 = Button(root, text='Inserir', command = lambda: salvar_caminho_03(caminho_programa_03)).place(x=550,y=160,width=60,height=30)
    botao_procurar_programa_03 = Button(root, text='Procurar', command = lambda: escolher_caminho_03()).place(x=620,y=160,width=60,height=30)


    caminho_programa_03 = Entry(root)
    caminho_programa_03.place(x=110,y=160,width=430,height=30)

# Programa 04
if os.path.exists(caminho_04):
    with open(caminho_04, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=200,width=430,height=30)
        label_programa_04 = Label(root,text='Programa 04:',anchor=W).place(x=10,y=200,width=110,height=30)
        botao_excluir_programa_04 = Button(root,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
        botao_abrir_programa_04 = Button(root,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)
        
else:
    label_programa_04 = Label(root,text='Programa 04:',anchor=W).place(x=10,y=200,width=110,height=30)
    botao_inserir_programa_04 = Button(root, text='Inserir', command = lambda: salvar_caminho_04(caminho_programa_04)).place(x=550,y=200,width=60,height=30)
    botao_procurar_programa_04 = Button(root, text='Procurar', command = lambda: escolher_caminho_04()).place(x=620,y=200,width=60,height=30)


    caminho_programa_04 = Entry(root)
    caminho_programa_04.place(x=110,y=200,width=430,height=30)

# Programa 05
if os.path.exists(caminho_05):
    with open(caminho_05, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=240,width=430,height=30)
        label_programa_05 = Label(root,text='Programa 05:',anchor=W).place(x=10,y=240,width=110,height=30)
        botao_excluir_programa_05 = Button(root,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
        botao_abrir_programa_05 = Button(root,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)
        
else:
    label_programa_05 = Label(root,text='Programa 05:',anchor=W).place(x=10,y=240,width=110,height=30)
    botao_inserir_programa_05 = Button(root, text='Inserir', command = lambda: salvar_caminho_05(caminho_programa_05)).place(x=550,y=240,width=60,height=30)
    botao_procurar_programa_05 = Button(root, text='Procurar', command = lambda: escolher_caminho_05()).place(x=620,y=240,width=60,height=30)

    caminho_programa_05 = Entry(root)
    caminho_programa_05.place(x=110,y=240,width=430,height=30)

# Programa 06
if os.path.exists(caminho_06):
    with open(caminho_06, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=280,width=430,height=30)
        label_programa_06 = Label(root,text='Programa 06:',anchor=W).place(x=10,y=280,width=110,height=30)
        botao_excluir_programa_06 = Button(root,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
        botao_abrir_programa_06 = Button(root,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)
        
else:
    label_programa_06 = Label(root,text='Programa 06:',anchor=W).place(x=10,y=280,width=110,height=30)
    botao_inserir_programa_06 = Button(root, text='Inserir', command = lambda: salvar_caminho_06(caminho_programa_06)).place(x=550,y=280,width=60,height=30)
    botao_procurar_programa_06 = Button(root, text='Procurar', command = lambda: escolher_caminho_06()).place(x=620,y=280,width=60,height=30)


    caminho_programa_06 = Entry(root)
    caminho_programa_06.place(x=110,y=280,width=430,height=30)


#Botão abrir todos os programas
botao_abrir_todos = Button(root,text='Abrir todos', command= abrir_todos).place(x=110,y=340,width=430,height=30)


#Botão ajuda
botao_ajuda = Button(root,text='Ajuda', command = lambda: ajuda()).place(x=550,y=340,width=130,height=30)


# Versão do programa
versao = Label(root,text='v. 0.9.0 (Alpha)').place(x=580,y=0,width=130,height=30)


# Créditos
creditos = Label(root,text='Criado por Marcos Castro (MaarquinhoO) | 2023')
root.mainloop()

# Incluir logotipo na Taskbar e janela

