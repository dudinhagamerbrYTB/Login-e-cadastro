from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import sqlite3

#criação da janela de login
Wm = Tk()
Wm.geometry('400x300')
Wm.title("Login")
Wm.configure(bg='#F0F2F8')
Wm.call('wm', 'iconphoto', Wm._w, PhotoImage(file='imagens/iconbitmap.ico'))

#variaveis globais
psw = StringVar()


#labels
log = Label(Wm, text='Login', bg='#F0F2F8')
log.place(x=150,y=40)
log.configure(font=('Arial 20 bold'))

emailab = Label(Wm, text='E-mail', bg='#F0F2F8')
emailab.place(x=30,y=100)
emailab.configure(font=('Arial 10 bold'))

senhalab = Label(Wm, text='Senha', bg='#F0F2F8')
senhalab.place(x=30,y=150)
senhalab.configure(font=('Arial 10 bold'))


#caixas de entrada
email = Entry(Wm, bg='#000000', fg='#FFFFFF', textvariable='E-mail')
email.place(x=98,y=100, width=200, height=25)

senha = Entry(Wm, bg='#000000', fg='#FFFFFF', textvariable = psw, show="*")
senha.place(x=98,y=150, width=200, height=25)

#botões
botentrar = Button(Wm, text='Entrar')
botentrar.place(x=160, y=200, height=25)
botentrar.configure(font=('Arial 10'))

botcad = Button(Wm, text='Cadastrar')
botcad.place(x=155, y=250, height=20)
botcad.configure(font=('Arial 8 underline'))


Wm.mainloop()