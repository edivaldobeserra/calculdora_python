from tkinter import *
from tkinter import*
from tkinter import ttk
from turtle import bgcolor 



cor1= "#080807"  #Preto
cor2= "#ffffff"  #Branco
cor3= "#0d098f"  #Azul
cor4= "#6b6b70"  #cinza
cor5= "#eb884b"  #Laranja



janela=Tk() #criar a janela
janela.title("calculadora") #titulo da janela
janela.geometry("235x318") #tamanho da janela
janela.config(bg=cor1) #mudando cor da janela

#criando Frames
Frame_tela=Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0,column=0) 

Frame_corpo=Frame(janela, width=235, height=268)
Frame_corpo.grid(row=1,column=0) 

#criando botoes

b_1 = Button(Frame_corpo, text="C", width=15, height=2, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(Frame_corpo, text="%", width=7, height=2, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=117, y=0)
b_3 = Button(Frame_corpo, text="/", width=7, height=2, bg=cor5, fg=cor2, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=178, y=0)


janela.mainloop() 


