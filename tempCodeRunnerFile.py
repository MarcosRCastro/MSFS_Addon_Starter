# Texto inicial do programa
texto_janela_inicial = Label(root, text = 'Inclua todos os programas que deseja abrir com o MSFS Manager')
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