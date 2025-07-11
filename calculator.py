# Importando Tkinter
from tkinter import *
from tkinter import ttk

# cores
co1 = "#ffcffd" # white
co2 = "#d911b5" # purple
co3 = "#ffffff" # off white
co4 = "#f3e700" # yellow
co5 = "#000000" # black
fundo = co2 # Definindo fundo como a cor principal

# janela
janela = Tk() # Para criar janela em branco(fundo)
janela.title('Calculadora') # título da janela
janela.geometry('235x318') # tamanho da janela
janela.configure(background=co2) # bg: background

# separação da janela
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280) # cria a fenda entre as duas janelas
Frame_tela = Frame(janela, width=300, height=56, background=co1, pady=0, relief="flat") # tela menor superior
Frame_tela.grid(row=1, column=0, sticky=NW) # onde o cursor vai aparecer para digitar
Frame_quadros = Frame(janela, width=300, height=340, background=fundo, pady=0, padx=0, relief='flat')
Frame_quadros.grid(row=2, column=0, sticky=NW) #onde os botões vão aparacer

def entrar_valor(event): #função de entrada de valores
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

    app_scream = Label(Frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat", anchor= "e", bd=0, justify=RIGHT, font=('Ivy 18'), bg='#37474f', fg=co1) #onde o cursor vai aparecer para digitar
    app_scream.place(x=0, y=0) #posição do cursor

def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


# visor
app_tela = Label(Frame_tela, text='', width=16, height=2, padx=7, relief='flat', anchor='e', justify=RIGHT, font=('Ivy', 18), bg=co1, fg=co5)

app_tela.place(x=0, y=0) #posição do cursor

b1 = Button(Frame_quadros, command = lambda: limpar_tela (), text = 'C', width=11, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b1.place(x=0, y=0) #posição do botão C

b2 = Button(Frame_quadros, command = lambda: entrar_valor ('%'), text = '%', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b2.place(x=118, y=0) #posição do botão %

b3 = Button(Frame_quadros, command = lambda: entrar_valor ('/'), text = '/', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b3.place(x=177, y=0) #posição do botão /

b4 = Button(Frame_quadros,command = lambda: entrar_valor ('7'), text = '7', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b4.place(x=0, y=52) #posição do botão 7

b5 = Button(Frame_quadros,command = lambda: entrar_valor ('8'), text = '8', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b5.place(x=59, y=52) #posição do botão 8

b6 = Button(Frame_quadros,command = lambda: entrar_valor ('9'), text = '9', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b6.place(x=118, y=52) #posição do botão 9

b7 = Button(Frame_quadros, command = lambda: entrar_valor ('*'), text = '*', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b7.place(x=177, y=52) #posição do botão *

b8 = Button(Frame_quadros, command = lambda: entrar_valor ('4'), text = '4', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b8.place(x=0, y=104) #posição do botão 4

b9 = Button(Frame_quadros, command = lambda: entrar_valor ('5'), text = '5', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b9.place(x=59, y=104) #posição do botão 5

b10 = Button(Frame_quadros, command = lambda: entrar_valor ('6'), text = '6', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b10.place(x=118, y=104) #posição do botão 6

b11 = Button(Frame_quadros, command = lambda: entrar_valor ('-'), text = '-', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b11.place(x=177, y=104) #posição do botão -

b12 = Button(Frame_quadros, command = lambda: entrar_valor ('1'), text = '1', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b12.place(x=0, y=156) #posição do botão 1

b13 = Button(Frame_quadros, command = lambda: entrar_valor ('2'), text = '2', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b13.place(x=59, y=156) #posição do botão 2

b14 = Button(Frame_quadros, command = lambda: entrar_valor ('3'), text = '3', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b14.place(x=118, y=156) #posição do botão 3

b15 = Button(Frame_quadros, command = lambda: entrar_valor ('+'), text = '+', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b15.place(x=177, y=156) #posição do botão +

b16 = Button(Frame_quadros, command = lambda: entrar_valor ('0'), text = '0', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b16.place(x=0, y=208) #posição do botão 0

b17 = Button(Frame_quadros, command = lambda: entrar_valor ('.'), text = '.', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b17.place(x=59, y=208) #posição do botão .

b18 = Button(Frame_quadros, command = lambda: calcular (), text = '=', width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'), relief="raised", overrelief= "ridge") #botão C
b18.place(x=118, y=208) #posição do botão =

todos_valores = "" #armazenar todos os valores digitados

valor_texto = StringVar () #variável para armazenar o texto da tela

def entrar_valor(event): #função de entrada de valores
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

    app_scream = Label(Frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat", anchor= "e", bd=0, justify=RIGHT, font=('Ivy 18'), bg='#37474f', fg=co1) #onde o cursor vai aparecer para digitar
    app_scream.place(x=0, y=0) #posição do cursor

def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""


# Mantenha a janela aberta até apertar exit
janela.mainloop()