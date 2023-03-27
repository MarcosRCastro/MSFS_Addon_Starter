import os
from tkinter import *
import webbrowser as wb
from tkinter import messagebox
from tkinter import filedialog



arq_caminho_01 = 'C:\MSFS_Addon_Starter\caminho01.txt'
arq_caminho_02 = 'C:\MSFS_Addon_Starter\caminho02.txt'
arq_caminho_03 = 'C:\MSFS_Addon_Starter\caminho03.txt'
arq_caminho_04 = 'C:\MSFS_Addon_Starter\caminho04.txt'
arq_caminho_05 = 'C:\MSFS_Addon_Starter\caminho05.txt'
arq_caminho_06 = 'C:\MSFS_Addon_Starter\caminho06.txt'

# Criar pasta
if os.path.exists('C:\MSFS_Addon_Starter'):
    print('Diretório já existe.')
else:
    os.makedirs('C:\MSFS_Addon_Starter')
    print('Diretório criado na pasta C:')


# Escolher caminho
# Abrir pastar para escolher o caminho do programa
def escolher_caminho_01():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_01, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_01 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)

def escolher_caminho_02():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_02, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(janela_principal,text=texto).place(x=110,y=120,width=430,height=30)
        botao_excluir_programa_02 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
        botao_abrir_programa_02 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)

def escolher_caminho_03():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_03, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(janela_principal,text=texto).place(x=110,y=160,width=430,height=30)
        botao_excluir_programa_03 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
        botao_abrir_programa_03 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)

def escolher_caminho_04():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_04, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(janela_principal,text=texto).place(x=110,y=200,width=430,height=30)
        botao_excluir_programa_04 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
        botao_abrir_programa_04 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)

def escolher_caminho_05():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_05, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(janela_principal,text=texto).place(x=110,y=240,width=430,height=30)
        botao_excluir_programa_05 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
        botao_abrir_programa_05 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)

def escolher_caminho_06():
    filename = filedialog.askopenfilename()
    print(filename)
    with open(arq_caminho_06, 'w') as arquivo:
        arquivo.write('%s' % filename)
        arquivo.write('\n')
        texto = filename
        caminho = Label(janela_principal,text=texto).place(x=110,y=280,width=430,height=30)
        botao_excluir_programa_06 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
        botao_abrir_programa_06 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)
    

#Salvar caminho 01
def salvar_caminho_01(caminho):
    with open(arq_caminho_01, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_01 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)

#Salvar caminho 02
def salvar_caminho_02(caminho):
    with open(arq_caminho_02, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(janela_principal,text=texto).place(x=110,y=120,width=430,height=30)
        botao_excluir_programa_02 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
        botao_abrir_programa_02 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)

#Salvar caminho 03
def salvar_caminho_03(caminho):
    with open(arq_caminho_03, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(janela_principal,text=texto).place(x=110,y=160,width=430,height=30)
        botao_excluir_programa_03 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
        botao_abrir_programa_03 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)

#Salvar caminho 04
def salvar_caminho_04(caminho):
    with open(arq_caminho_04, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(janela_principal,text=texto).place(x=110,y=200,width=430,height=30)
        botao_excluir_programa_04 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
        botao_abrir_programa_04 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)

#Salvar caminho 05
def salvar_caminho_05(caminho):
    with open(arq_caminho_05, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(janela_principal,text=texto).place(x=110,y=240,width=430,height=30)
        botao_excluir_programa_05 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
        botao_abrir_programa_05 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)

#Salvar caminho 06
def salvar_caminho_06(caminho):
    with open(arq_caminho_06, 'w') as arquivo:
        arquivo.write('%s' % caminho.get())
        arquivo.write('\n')
        texto = caminho.get()
        caminho = Label(janela_principal,text=texto).place(x=110,y=280,width=430,height=30)
        botao_excluir_programa_06 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
        botao_abrir_programa_06 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)


# Procurar caminho
# Procurar caminho 01
def procurar_caminnho_01():
    with open(arq_caminho_01, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_01 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 02
def procurar_caminnho_02():
    with open(arq_caminho_02, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_02 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_02 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 03
def procurar_caminnho_03():
    with open(arq_caminho_03, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_03 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_03 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 04
def procurar_caminnho_04():
    with open(arq_caminho_04, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_04 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_04 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 05
def procurar_caminnho_05():
    with open(arq_caminho_06, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_05 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_05 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=80,width=60,height=30)

# Procurar caminho 06
def procurar_caminnho_06():
    with open(arq_caminho_06, 'w') as arquivo:
        arquivo.write('%s' % caminho)
        arquivo.write('\n')
        texto = caminho
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        botao_excluir_programa_06 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_06 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=80,width=60,height=30)



# Excluir caminho 01
def excluir_caminho_01():
    botao_inserir_programa_01 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_01(caminho_programa_01)).place(x=550,y=80,width=60,height=30)
    caminho_programa_01 = Entry(janela_principal)
    caminho_programa_01.place(x=110,y=80,width=430,height=30)
    botao_abrir_programa_01 = Button(janela_principal,text='').place(x=620,y=80,width=60,height=30)
    botao_procurar_programa_01 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_01()).place(x=620,y=80,width=60,height=30)
    os.remove(arq_caminho_01)

# Excluir caminho 02
def excluir_caminho_02():
    botao_inserir_programa_02 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_02(caminho_programa_02)).place(x=550,y=120,width=60,height=30)
    caminho_programa_02 = Entry(janela_principal)
    caminho_programa_02.place(x=110,y=120,width=430,height=30)
    botao_abrir_programa_02 = Button(janela_principal,text='').place(x=620,y=120,width=60,height=30)
    botao_procurar_programa_02 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_02()).place(x=620,y=120,width=60,height=30)
    os.remove(arq_caminho_02)

# Excluir caminho 03
def excluir_caminho_03():
    botao_inserir_programa_03 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_03(caminho_programa_03)).place(x=550,y=160,width=60,height=30)
    caminho_programa_03 = Entry(janela_principal)
    caminho_programa_03.place(x=110,y=160,width=430,height=30)
    botao_abrir_programa_03 = Button(janela_principal,text='').place(x=620,y=160,width=60,height=30)
    botao_procurar_programa_03 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_03()).place(x=620,y=160,width=60,height=30)
    os.remove(arq_caminho_03)

# Excluir caminho 04
def excluir_caminho_04():
    botao_inserir_programa_04 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_04(caminho_programa_04)).place(x=550,y=200,width=60,height=30)
    caminho_programa_04 = Entry(janela_principal)
    caminho_programa_04.place(x=110,y=200,width=430,height=30)
    botao_abrir_programa_04 = Button(janela_principal,text='').place(x=620,y=200,width=60,height=30)
    botao_procurar_programa_04 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_04()).place(x=620,y=200,width=60,height=30)
    os.remove(arq_caminho_04)

# Excluir caminho 05
def excluir_caminho_05():
    botao_inserir_programa_05 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_05(caminho_programa_05)).place(x=550,y=240,width=60,height=30)
    caminho_programa_05 = Entry(janela_principal)
    caminho_programa_05.place(x=110,y=240,width=430,height=30)
    botao_abrir_programa_05 = Button(janela_principal,text='').place(x=620,y=240,width=60,height=30)
    botao_procurar_programa_05 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_05()).place(x=620,y=240,width=60,height=30)
    os.remove(arq_caminho_05)

# Excluir caminho 06
def excluir_caminho_06():
    botao_inserir_programa_06 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_06(caminho_programa_06)).place(x=550,y=280,width=60,height=30)
    caminho_programa_06 = Entry(janela_principal)
    caminho_programa_06.place(x=110,y=280,width=430,height=30)
    botao_abrir_programa_06 = Button(janela_principal,text='').place(x=620,y=280,width=60,height=30)
    botao_procurar_programa_06 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_06()).place(x=620,y=280,width=60,height=30)
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






# Criar janela_principal principal
janela_principal = Tk()
janela_principal.title('MSFS Addons Starter - Aqui você economiza cliques!')
janela_principal.geometry('700x400')
janela_principal.configure(background='#dde')

# Texto inicial do programa
texto_janela_inicial = Label(janela_principal, text = 'Inclua todos os programas que deseja abrir com o MSFS Addons Starter')
texto_janela_inicial.configure(background='#dde')
texto_janela_inicial.place(x=140,y=30)


# Programa 01
if os.path.exists(arq_caminho_01):
    with open(arq_caminho_01, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(janela_principal,text=texto).place(x=110,y=80,width=430,height=30)
        label_programa_01 = Label(janela_principal,text='Programa 01:', background='#dde',anchor=W).place(x=10,y=80,width=110,height=30)
        botao_excluir_programa_01 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_01()).place(x=550,y=80,width=60,height=30)
        botao_abrir_programa_01 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_01()).place(x=620,y=80,width=60,height=30)
        
else:
    label_programa_01 = Label(janela_principal,text='Programa 01:', background='#dde',anchor=W).place(x=10,y=80,width=110,height=30)
    botao_inserir_programa_01 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_01(caminho_programa_01)).place(x=550,y=80,width=60,height=30)
    botao_procurar_programa_01 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_01()).place(x=620,y=80,width=60,height=30)

    caminho_programa_01 = Entry(janela_principal)
    caminho_programa_01.place(x=110,y=80,width=430,height=30)

# Programa 02
if os.path.exists(arq_caminho_02):
    with open(arq_caminho_02, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(janela_principal,text=texto).place(x=110,y=120,width=430,height=30)
        label_programa_02 = Label(janela_principal,text='Programa 02:', background='#dde',anchor=W).place(x=10,y=120,width=110,height=30)
        botao_excluir_programa_01 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_02()).place(x=550,y=120,width=60,height=30)
        botao_abrir_programa_01 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_02()).place(x=620,y=120,width=60,height=30)
        
else:
    label_programa_02 = Label(janela_principal,text='Programa 02:', background='#dde',anchor=W).place(x=10,y=120,width=110,height=30)
    botao_inserir_programa_02 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_02(caminho_programa_02)).place(x=550,y=120,width=60,height=30)
    botao_procurar_programa_02 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_02()).place(x=620,y=120,width=60,height=30)

    caminho_programa_02 = Entry(janela_principal)
    caminho_programa_02.place(x=110,y=120,width=430,height=30)

# Programa 03
if os.path.exists(arq_caminho_03):
    with open(arq_caminho_03, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(janela_principal,text=texto).place(x=110,y=160,width=430,height=30)
        label_programa_03 = Label(janela_principal,text='Programa 03:', background='#dde',anchor=W).place(x=10,y=160,width=110,height=30)
        botao_excluir_programa_03 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_03()).place(x=550,y=160,width=60,height=30)
        botao_abrir_programa_03 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_03()).place(x=620,y=160,width=60,height=30)
        
else:
    label_programa_03 = Label(janela_principal,text='Programa 03:', background='#dde',anchor=W).place(x=10,y=160,width=110,height=30)
    botao_inserir_programa_03 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_03(caminho_programa_03)).place(x=550,y=160,width=60,height=30)
    botao_procurar_programa_03 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_03()).place(x=620,y=160,width=60,height=30)


    caminho_programa_03 = Entry(janela_principal)
    caminho_programa_03.place(x=110,y=160,width=430,height=30)

# Programa 04
if os.path.exists(arq_caminho_04):
    with open(arq_caminho_04, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(janela_principal,text=texto).place(x=110,y=200,width=430,height=30)
        label_programa_04 = Label(janela_principal,text='Programa 04:', background='#dde',anchor=W).place(x=10,y=200,width=110,height=30)
        botao_excluir_programa_04 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_04()).place(x=550,y=200,width=60,height=30)
        botao_abrir_programa_04 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_04()).place(x=620,y=200,width=60,height=30)
        
else:
    label_programa_04 = Label(janela_principal,text='Programa 04:', background='#dde',anchor=W).place(x=10,y=200,width=110,height=30)
    botao_inserir_programa_04 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_04(caminho_programa_04)).place(x=550,y=200,width=60,height=30)
    botao_procurar_programa_04 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_04()).place(x=620,y=200,width=60,height=30)


    caminho_programa_04 = Entry(janela_principal)
    caminho_programa_04.place(x=110,y=200,width=430,height=30)

# Programa 05
if os.path.exists(arq_caminho_05):
    with open(arq_caminho_05, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(janela_principal,text=texto).place(x=110,y=240,width=430,height=30)
        label_programa_05 = Label(janela_principal,text='Programa 05:', background='#dde',anchor=W).place(x=10,y=240,width=110,height=30)
        botao_excluir_programa_05 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_05()).place(x=550,y=240,width=60,height=30)
        botao_abrir_programa_05 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_05()).place(x=620,y=240,width=60,height=30)
        
else:
    label_programa_05 = Label(janela_principal,text='Programa 05:', background='#dde',anchor=W).place(x=10,y=240,width=110,height=30)
    botao_inserir_programa_05 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_05(caminho_programa_05)).place(x=550,y=240,width=60,height=30)
    botao_procurar_programa_05 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_05()).place(x=620,y=240,width=60,height=30)

    caminho_programa_05 = Entry(janela_principal)
    caminho_programa_05.place(x=110,y=240,width=430,height=30)

# Programa 06
if os.path.exists(arq_caminho_06):
    with open(arq_caminho_06, 'r') as arquivo:
        texto = arquivo.readlines()
        texto = [x.strip('\n') for x in texto]
        caminho = Label(janela_principal,text=texto).place(x=110,y=280,width=430,height=30)
        label_programa_06 = Label(janela_principal,text='Programa 06:', background='#dde',anchor=W).place(x=10,y=280,width=110,height=30)
        botao_excluir_programa_06 = Button(janela_principal,text='Excluir',command = lambda: excluir_caminho_06()).place(x=550,y=280,width=60,height=30)
        botao_abrir_programa_06 = Button(janela_principal,text='Abrir',command=lambda:abrir_programa_06()).place(x=620,y=280,width=60,height=30)
        
else:
    label_programa_06 = Label(janela_principal,text='Programa 06:', background='#dde',anchor=W).place(x=10,y=280,width=110,height=30)
    botao_inserir_programa_06 = Button(janela_principal, text='Inserir', command = lambda: salvar_caminho_06(caminho_programa_06)).place(x=550,y=280,width=60,height=30)
    botao_procurar_programa_06 = Button(janela_principal, text='Procurar', command = lambda: escolher_caminho_06()).place(x=620,y=280,width=60,height=30)


    caminho_programa_06 = Entry(janela_principal)
    caminho_programa_06.place(x=110,y=280,width=430,height=30)


#Botão abrir todos os programas
botao_abrir_todos = Button(janela_principal,text='Abrir todos', command= abrir_todos).place(x=110,y=340,width=430,height=30)


#Botão ajuda
botao_ajuda = Button(janela_principal,text='Ajuda', command = lambda: ajuda()).place(x=550,y=340,width=130,height=30)


# Versão do programa
versao = Label(janela_principal,text='v. 0.2', background='#dde').place(x=610,y=0,width=130,height=30)


# Créditos
creditos = Label(janela_principal,text='Criado por Marcos Castro (MaarquinhoO) | 2023', background='#dde')
janela_principal.mainloop()
