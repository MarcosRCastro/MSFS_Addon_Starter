import os
from tkinter import *
import webbrowser as wb
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from PIL import ImageTk, Image
import win32com.client as win32
import pyperclip as pc


# Variáveis
local_dos_arquivos = 'C:\\MSFS_Addon_Starter'
primeira_ini = 0

arq_caminho_01 = local_dos_arquivos + '\\caminho01.txt'
arq_caminho_02 = local_dos_arquivos + '\\caminho02.txt'
arq_caminho_03 = local_dos_arquivos + '\\caminho03.txt'
arq_caminho_04 = local_dos_arquivos + '\\caminho04.txt'
arq_caminho_05 = local_dos_arquivos + '\\caminho05.txt'
arq_caminho_06 = local_dos_arquivos + '\\caminho06.txt'





############## Funçoes ###################

# Verificar se é primeira inicialização
def primeira_inicializacao():
    if os.path.exists('C:\MSFS_Addon_Starter'):
        print('Diretório já existe.')
        with open('C:\MSFS_Addon_Starter\local.txt', 'r') as arquivo:
            local_dos_arquivos = arquivo.readlines()
            return local_dos_arquivos
    else:
        os.makedirs('C:\MSFS_Addon_Starter')
        with open('C:\MSFS_Addon_Starter\local.txt', 'w') as arquivo:
            arquivo.write('1')
        mensagem_boas_vindas()
       
# Mensagem de boas vindas na primeira inicialização
def mensagem_boas_vindas():
    bem_vindo = messagebox.showinfo(
        message='Seja bem vindo ao MSFS Addon Starter!\n\n'
        'Este programa está em desenvolvimento, assim, provavelmente durante sua utilização você encontre alguns erros ou bugs. Peço que nos informe sempre que encontrar um problema e sempre que tiver uma ideia ou sugestão.\n\n'
        'Bons voos Comandante!!',
        title='Olá!'
    )
    escolher_local_arquivos = messagebox.askyesno(
        message='Você deseja escolher a pasta para salvar os arquivos? \n(Se oprtar por não, eles serão salvos na pasta "C:\")',
        icon= 'question', title='Antes de iniciarmos'
    )
    if escolher_local_arquivos == True:
        local_dos_arquivos = filedialog.askdirectory()
        
        # Criar pasta para salvar arquivos
        local_dos_arquivos = local_dos_arquivos + '\\MSFS_Addon_Starter\\'
        if os.path.exists(local_dos_arquivos):
            print('Diretório já existe.')
            print(local_dos_arquivos)
            with open(local_dos_arquivos + 'local_arquivos.txt', 'r') as arquivo:
                local_dos_arquivos = arquivo.readlines()
        else:
            os.makedirs(local_dos_arquivos)
            print('Diretório criado na pasta', local_dos_arquivos)
            with open(local_dos_arquivos + 'local_arquivos.txt', 'w') as arquivo:
                arquivo.write(local_dos_arquivos)
    
    else:
        local_dos_arquivos = 'C:\\MSFS_Addon_Starter\\'
        with open(local_dos_arquivos + 'local.txt', 'w') as arquivo:
            arquivo.write(local_dos_arquivos)

# Janela configurações
def configuracoes():
    janela_configuracoes = Tk()
    janela_configuracoes.title('Configurações')
    janela_configuracoes.geometry('500x350+520+220')
    janela_configuracoes.resizable(False, False)
    janela_configuracoes.configure(background='#dde')

    
    escolha_idioma = StringVar()
    escolha_idioma = Combobox(janela_configuracoes, textvariable=escolha_idioma).place(x=14,y=20,width=200,height=30)
    escolha_idioma.current(0)
    escolha_idioma['values'] = ('Português', 'Inglês')

# Janela reportar Bug     
def reportar_bug():
    janela_email_bug = Tk()
    janela_email_bug.title('Alerta de Bug')
    janela_email_bug.geometry('500x350+520+220')
    janela_email_bug.resizable(False, False)
    janela_email_bug.configure(background='#dde')
    Label(janela_email_bug, text="Explique o erro abaixo:", background='#dde').place(x=140,y=20,width=200,height=30)
  
    texto = scrolledtext.ScrolledText(janela_email_bug, wrap=WORD,
                                      width=50, height=12).place(x=20,y=60,width=460,height=230)
    explicacao = Entry(texto)

    botao_enviar = Button(janela_email_bug, text='Enviar', command= lambda: enviar_texto_bug(explicacao)).place(x=420,y=300,width=60,height=30)
    botao_cancelar = Button(janela_email_bug, text='Cancelar', command= lambda: janela_email_bug.destroy()).place(x=350,y=300,width=60,height=30)


# Janela para fazer sugestão
def sugestao():
    janela_sugestao = Tk()
    janela_sugestao.title('Alerta de Bug')
    janela_sugestao.geometry('500x350+520+220')
    janela_sugestao.resizable(False, False)
    janela_sugestao.configure(background='#dde')

    info = Label(janela_sugestao, text='Deixe sua ideia ou sugestão abaixo:', background='#dde').place(x=20,y=20,width=430,height=30)
    explicacao = Entry(janela_sugestao).place(x=20,y=50,width=460,height=230)
    botao_enviar = Button(janela_sugestao, text='Enviar', command= lambda: enviar_sugestao(explicacao)).place(x=420,y=300,width=60,height=30)
    botao_cancelar = Button(janela_sugestao, text='Cancelar', command= lambda: janela_sugestao.destroy()).place(x=350,y=300,width=60,height=30)


# Função enviar texto na página de avisar sobre bug
def enviar_texto_bug(explicacao): ##### Não está funcionando
    print(explicacao)
    # criar a integração com o outlook
    #outlook = win32.Dispatch('outlook.application')
    # criar um email
    #email = outlook.CreateItem(0)
    # configurar as informações do seu e-mail
    #email.To = 'maarquinhoo@outlook.com.br'
    #email.Subject = ('Reporte de Bug no MSFS Addon Starter | ' + data.today())
    #email.HTMLBody = explicacao
    #email.Send()
    #messagebox.showinfo(message='Bug reportado! Obrigado por nos avisar.')

# Função enviar sugestão na página sugestão
def enviar_sugestao(explicacao): ##### Não está funcionando
    # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')
    # criar um email
    email = outlook.CreateItem(0)
    # configurar as informações do seu e-mail
    email.To = 'maarquinhoo@outlook.com.br'
    email.Subject = ('Sugestão para MSFS Addon Starter | ' + data.today())
    email.HTMLBody = explicacao
    email.Send()
    messagebox.showinfo(message='Sugestão enviada. Obrigado pela dedicação.')



# Janela "Sobre"
def sobre():
    janela_sobre = Tk()
    janela_sobre.title('Sobre o MSFS Addons Starter')
    janela_sobre.geometry('500x350+520+220')
    janela_sobre.resizable(False, False)
    janela_sobre.configure(background='#dde')
    

    info = Label(janela_sobre, text='O "Microsoft Flight Simulator Addons Starter" foi criado pelo programador\n'
                                    'Marcos Castro com o intuito de facilitar a abertura de todos os programas\n'
                                    'utilizados para a simulação de voo. A versão Alpha do MSFS Addons Starter\n'
                                    'é a atual versão e ainda contará com muitas melhorias.\n\n'
                                    'Se você tem alguma ideia, sugestão para melhoria do programa não\n'
                                    'deixe de nos enviar, pois queremos que ele seja o melhor possível para\n'
                                    'você.\n\n'
                                    'Lembrando que o MSFS Addons Starter foi criado para o MSFS, porém pode\n'
                                    'ser usado para abrir quaisquer programas que você quiser. Então, use e abuse.\n\n'
                                    'Se você quiser ajudar no desenvolvimento deste programa, além de nos enviar\n'
                                    'sugestões e reporte de bugs, faça-nos uma doação. Qualquer valor será bem vindo.', background='#dde').place(x=20,y=5,width=450,height=250)

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
    janela_pix.configure(background='#dde')
    codigo = '69482510-6503-4a5c-af1a-e4b4c8ee9e4f'
    info = Label(janela_pix, text='Use a chave PIX abaixo para fazer uma doação.\n' 
                                    'Ajude-nos a comprar um café, até porque códigos não\n'
                                    'existem sem boas doses de cafeína.\n\n', background='#dde').place(x=30,y=20,width=430,height=120)
    info02 = Label(janela_pix, text='69482510-6503-4a5c-af1a-e4b4c8ee9e4f').place(x=30,y=100,width=430,height=120)
    botao_copiar = Button(janela_pix, text='Copiar', command= lambda: pc.copy(codigo)).place(x=200,y=290,width=120,height=30)
    botao_voltar = Button(janela_pix, text='Voltar', command= lambda: janela_pix.destroy()).place(x=340,y=290,width=120,height=30)


# Escolher caminho
# Abrir pastar para escolher o   caminho do programa
def escolher_caminho_01():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_01, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)

def escolher_caminho_02():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_02, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(root,text=texto).place(x=110,y=120,width=430,height=30)
        botao_excluir_programa_02 = Button(root,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
        botao_abrir_programa_02 = Button(root,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)

def escolher_caminho_03():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_03, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(root,text=texto).place(x=110,y=160,width=430,height=30)
        botao_excluir_programa_03 = Button(root,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
        botao_abrir_programa_03 = Button(root,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)

def escolher_caminho_04():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_04, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(root,text=texto).place(x=110,y=200,width=430,height=30)
        botao_excluir_programa_04 = Button(root,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
        botao_abrir_programa_04 = Button(root,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)

def escolher_caminho_05():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_05, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(root,text=texto).place(x=110,y=240,width=430,height=30)
        botao_excluir_programa_05 = Button(root,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
        botao_abrir_programa_05 = Button(root,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)

def escolher_caminho_06():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_06, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(root,text=texto).place(x=110,y=280,width=430,height=30)
        botao_excluir_programa_06 = Button(root,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
        botao_abrir_programa_06 = Button(root,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)
    

#Salvar caminho 01
def salvar_caminho_01(caminho):
    
    with open(arq_caminho_01, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)

#Salvar caminho 02
def salvar_caminho_02(caminho):
    with open(arq_caminho_02, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(root,text=texto).place(x=110,y=120,width=430,height=30)
        botao_excluir_programa_02 = Button(root,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
        botao_abrir_programa_02 = Button(root,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)

#Salvar caminho 03
def salvar_caminho_03(caminho):
    with open(arq_caminho_03, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(root,text=texto).place(x=110,y=160,width=430,height=30)
        botao_excluir_programa_03 = Button(root,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
        botao_abrir_programa_03 = Button(root,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)

#Salvar caminho 04
def salvar_caminho_04(caminho):
    with open(arq_caminho_04, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(root,text=texto).place(x=110,y=200,width=430,height=30)
        botao_excluir_programa_04 = Button(root,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
        botao_abrir_programa_04 = Button(root,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)

#Salvar caminho 05
def salvar_caminho_05(caminho):
    with open(arq_caminho_05, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(root,text=texto).place(x=110,y=240,width=430,height=30)
        botao_excluir_programa_05 = Button(root,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
        botao_abrir_programa_05 = Button(root,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)

#Salvar caminho 06
def salvar_caminho_06(caminho):
    with open(arq_caminho_06, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(root,text=texto).place(x=110,y=280,width=430,height=30)
        botao_excluir_programa_06 = Button(root,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
        botao_abrir_programa_06 = Button(root,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)


# Procurar caminho
# Procurar caminho 01
def procurar_caminnho_01():
    with open(arq_caminho_01, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 02
def procurar_caminnho_02():
    with open(arq_caminho_02, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_02 = Button(root,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_02 = Button(root,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 03
def procurar_caminnho_03():
    with open(arq_caminho_03, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_03 = Button(root,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_03 = Button(root,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 04
def procurar_caminnho_04():
    with open(arq_caminho_04, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_04 = Button(root,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_04 = Button(root,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 05
def procurar_caminnho_05():
    with open(arq_caminho_06, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_05 = Button(root,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_05 = Button(root,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 06
def procurar_caminnho_06():
    with open(arq_caminho_06, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_06 = Button(root,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_06 = Button(root,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=80,width=60,height=30)



# Excluir caminho 01
def excluir_caminho_01():
    botao_inserir_programa_01 = Button(root, text='Inserir', command = lambda: salvar_caminho_01(caminho_programa_01)).place(x=550,y=80,width=60,height=30)
    caminho_programa_01 = Entry(root)
    caminho_programa_01.place(x=110,y=80,width=430,height=30)
    botao_abrir_programa_01 = Button(root,text='').place(x=620,y=80,width=60,height=30)
    botao_procurar_programa_01 = Button(root, text='Procurar', command = lambda: escolher_caminho_01()).place(x=620,y=80,width=60,height=30)
    os.remove(arq_caminho_01)

# Excluir caminho 02
def excluir_caminho_02():
    botao_inserir_programa_02 = Button(root, text='Inserir', command = lambda: salvar_caminho_02(caminho_programa_02)).place(x=550,y=120,width=60,height=30)
    caminho_programa_02 = Entry(root)
    caminho_programa_02.place(x=110,y=120,width=430,height=30)
    botao_abrir_programa_02 = Button(root,text='').place(x=620,y=120,width=60,height=30)
    botao_procurar_programa_02 = Button(root, text='Procurar', command = lambda: escolher_caminho_02()).place(x=620,y=120,width=60,height=30)
    os.remove(arq_caminho_02)

# Excluir caminho 03
def excluir_caminho_03():
    botao_inserir_programa_03 = Button(root, text='Inserir', command = lambda: salvar_caminho_03(caminho_programa_03)).place(x=550,y=160,width=60,height=30)
    caminho_programa_03 = Entry(root)
    caminho_programa_03.place(x=110,y=160,width=430,height=30)
    botao_abrir_programa_03 = Button(root,text='').place(x=620,y=160,width=60,height=30)
    botao_procurar_programa_03 = Button(root, text='Procurar', command = lambda: escolher_caminho_03()).place(x=620,y=160,width=60,height=30)
    os.remove(arq_caminho_03)

# Excluir caminho 04
def excluir_caminho_04():
    botao_inserir_programa_04 = Button(root, text='Inserir', command = lambda: salvar_caminho_04(caminho_programa_04)).place(x=550,y=200,width=60,height=30)
    caminho_programa_04 = Entry(root)
    caminho_programa_04.place(x=110,y=200,width=430,height=30)
    botao_abrir_programa_04 = Button(root,text='').place(x=620,y=200,width=60,height=30)
    botao_procurar_programa_04 = Button(root, text='Procurar', command = lambda: escolher_caminho_04()).place(x=620,y=200,width=60,height=30)
    os.remove(arq_caminho_04)

# Excluir caminho 05
def excluir_caminho_05():
    botao_inserir_programa_05 = Button(root, text='Inserir', command = lambda: salvar_caminho_05(caminho_programa_05)).place(x=550,y=240,width=60,height=30)
    caminho_programa_05 = Entry(root)
    caminho_programa_05.place(x=110,y=240,width=430,height=30)
    botao_abrir_programa_05 = Button(root,text='').place(x=620,y=240,width=60,height=30)
    botao_procurar_programa_05 = Button(root, text='Procurar', command = lambda: escolher_caminho_05()).place(x=620,y=240,width=60,height=30)
    os.remove(arq_caminho_05)

# Excluir caminho 06
def excluir_caminho_06():
    botao_inserir_programa_06 = Button(root, text='Inserir', command = lambda: salvar_caminho_06(caminho_programa_06)).place(x=550,y=280,width=60,height=30)
    caminho_programa_06 = Entry(root)
    caminho_programa_06.place(x=110,y=280,width=430,height=30)
    botao_abrir_programa_06 = Button(root,text='').place(x=620,y=280,width=60,height=30)
    botao_procurar_programa_06 = Button(root, text='Procurar', command = lambda: escolher_caminho_06()).place(x=620,y=280,width=60,height=30)
    os.remove(arq_caminho_06)



# Abrir programa 01
def abrir_programa_01():
    with open(arq_caminho_01, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 02
def abrir_programa_02():
    with open(arq_caminho_02, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 03
def abrir_programa_03():
    with open(arq_caminho_03, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 04
def abrir_programa_04():
    with open(arq_caminho_04, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 05
def abrir_programa_05():
    with open(arq_caminho_05, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir programa 06
def abrir_programa_06():
    with open(arq_caminho_06, 'r') as arquivo:
        dados = arquivo.readlines()
    dados = [x.strip('\n') for x in dados]
    os.startfile(dados[0])

# Abrir todos os programas
def abrir_todos():
    if os.path.exists(arq_caminho_01):
        with open(arq_caminho_01, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(arq_caminho_02):
        with open(arq_caminho_02, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(arq_caminho_03):
        with open(arq_caminho_03, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(arq_caminho_04):
        with open(arq_caminho_04, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(arq_caminho_05):
        with open(arq_caminho_05, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])

    if os.path.exists(arq_caminho_06):
        with open(arq_caminho_06, 'r') as arquivo:
            dados = arquivo.readlines()
        dados = [x.strip('\n') for x in dados]
        os.startfile(dados[0])


# Função do botão ajuda
def ajuda():
    wb.open('https://www.youtube.com/channel/UCLqxFVkks6-nwKirjQBuRUQ')




############### Programa ##############


# Criar root principal
root = Tk()
root.title('MSFS Addons Starter - Aqui você economiza cliques!')
root.geometry('700x400+440+200')
root.resizable(False, False)
root.configure(background='#dde')


# Menu

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(root, tearoff=False)
file_menu.add_command(label='Configurações',command=lambda:configuracoes())
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
texto_janela_inicial = Label(root, text = 'Inclua todos os programas que deseja abrir com o MSFS Addons Starter')
texto_janela_inicial.configure(background='#dde')
texto_janela_inicial.place(x=140,y=30)


primeira_inicializacao()


# Programa 01
if os.path.exists(arq_caminho_01):
    with open(arq_caminho_01, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=80,width=430,height=30)
        label_programa_01 = Label(root,text='Programa 01:', background='#dde',anchor=W).place(x=10,y=80,width=110,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)
        
else:
    label_programa_01 = Label(root,text='Programa 01:', background='#dde',anchor=W).place(x=10,y=80,width=110,height=30)
    botao_inserir_programa_01 = Button(root, text='Inserir', command = lambda: salvar_caminho_01(caminho_programa_01)).place(x=550,y=80,width=60,height=30)
    botao_procurar_programa_01 = Button(root, text='Procurar', command = lambda: escolher_caminho_01()).place(x=620,y=80,width=60,height=30)

    caminho_programa_01 = Entry(root)
    caminho_programa_01.place(x=110,y=80,width=430,height=30)

# Programa 02
if os.path.exists(arq_caminho_02):
    with open(arq_caminho_02, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=120,width=430,height=30)
        label_programa_02 = Label(root,text='Programa 02:', background='#dde',anchor=W).place(x=10,y=120,width=110,height=30)
        botao_excluir_programa_01 = Button(root,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
        botao_abrir_programa_01 = Button(root,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)
        
else:
    label_programa_02 = Label(root,text='Programa 02:', background='#dde',anchor=W).place(x=10,y=120,width=110,height=30)
    botao_inserir_programa_02 = Button(root, text='Inserir', command = lambda: salvar_caminho_02(caminho_programa_02)).place(x=550,y=120,width=60,height=30)
    botao_procurar_programa_02 = Button(root, text='Procurar', command = lambda: escolher_caminho_02()).place(x=620,y=120,width=60,height=30)

    caminho_programa_02 = Entry(root)
    caminho_programa_02.place(x=110,y=120,width=430,height=30)

# Programa 03
if os.path.exists(arq_caminho_03):
    with open(arq_caminho_03, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=160,width=430,height=30)
        label_programa_03 = Label(root,text='Programa 03:', background='#dde',anchor=W).place(x=10,y=160,width=110,height=30)
        botao_excluir_programa_03 = Button(root,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
        botao_abrir_programa_03 = Button(root,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)
        
else:
    label_programa_03 = Label(root,text='Programa 03:', background='#dde',anchor=W).place(x=10,y=160,width=110,height=30)
    botao_inserir_programa_03 = Button(root, text='Inserir', command = lambda: salvar_caminho_03(caminho_programa_03)).place(x=550,y=160,width=60,height=30)
    botao_procurar_programa_03 = Button(root, text='Procurar', command = lambda: escolher_caminho_03()).place(x=620,y=160,width=60,height=30)


    caminho_programa_03 = Entry(root)
    caminho_programa_03.place(x=110,y=160,width=430,height=30)

# Programa 04
if os.path.exists(arq_caminho_04):
    with open(arq_caminho_04, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=200,width=430,height=30)
        label_programa_04 = Label(root,text='Programa 04:', background='#dde',anchor=W).place(x=10,y=200,width=110,height=30)
        botao_excluir_programa_04 = Button(root,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
        botao_abrir_programa_04 = Button(root,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)
        
else:
    label_programa_04 = Label(root,text='Programa 04:', background='#dde',anchor=W).place(x=10,y=200,width=110,height=30)
    botao_inserir_programa_04 = Button(root, text='Inserir', command = lambda: salvar_caminho_04(caminho_programa_04)).place(x=550,y=200,width=60,height=30)
    botao_procurar_programa_04 = Button(root, text='Procurar', command = lambda: escolher_caminho_04()).place(x=620,y=200,width=60,height=30)


    caminho_programa_04 = Entry(root)
    caminho_programa_04.place(x=110,y=200,width=430,height=30)

# Programa 05
if os.path.exists(arq_caminho_05):
    with open(arq_caminho_05, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=240,width=430,height=30)
        label_programa_05 = Label(root,text='Programa 05:', background='#dde',anchor=W).place(x=10,y=240,width=110,height=30)
        botao_excluir_programa_05 = Button(root,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
        botao_abrir_programa_05 = Button(root,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)
        
else:
    label_programa_05 = Label(root,text='Programa 05:', background='#dde',anchor=W).place(x=10,y=240,width=110,height=30)
    botao_inserir_programa_05 = Button(root, text='Inserir', command = lambda: salvar_caminho_05(caminho_programa_05)).place(x=550,y=240,width=60,height=30)
    botao_procurar_programa_05 = Button(root, text='Procurar', command = lambda: escolher_caminho_05()).place(x=620,y=240,width=60,height=30)

    caminho_programa_05 = Entry(root)
    caminho_programa_05.place(x=110,y=240,width=430,height=30)

# Programa 06
if os.path.exists(arq_caminho_06):
    with open(arq_caminho_06, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(root,text=texto).place(x=110,y=280,width=430,height=30)
        label_programa_06 = Label(root,text='Programa 06:', background='#dde',anchor=W).place(x=10,y=280,width=110,height=30)
        botao_excluir_programa_06 = Button(root,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
        botao_abrir_programa_06 = Button(root,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)
        
else:
    label_programa_06 = Label(root,text='Programa 06:', background='#dde',anchor=W).place(x=10,y=280,width=110,height=30)
    botao_inserir_programa_06 = Button(root, text='Inserir', command = lambda: salvar_caminho_06(caminho_programa_06)).place(x=550,y=280,width=60,height=30)
    botao_procurar_programa_06 = Button(root, text='Procurar', command = lambda: escolher_caminho_06()).place(x=620,y=280,width=60,height=30)


    caminho_programa_06 = Entry(root)
    caminho_programa_06.place(x=110,y=280,width=430,height=30)


#Botão abrir todos os programas
botao_abrir_todos = Button(root,text='Abrir todos', command= abrir_todos).place(x=110,y=340,width=430,height=30)


#Botão ajuda
botao_ajuda = Button(root,text='Ajuda', command = lambda: ajuda()).place(x=550,y=340,width=130,height=30)


# Versão do programa
versao = Label(root,text='v. 0.5 (Alpha)', background='#dde').place(x=580,y=0,width=130,height=30)


# Créditos
creditos = Label(root,text='Criado por Marcos Castro (MaarquinhoO) | 2023', background='#dde')
root.mainloop()




# Incluir logotipo na Taskbar e janela