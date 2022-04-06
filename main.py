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
janela.geometry("235x266") #tamanho da janela
janela.config(bg=cor1) #mudando cor da janela

#criando Frames
Frame_tela=Frame(janela, width=235, height=50, bg=cor3)
Frame_tela.grid(row=0,column=0) 

Frame_corpo=Frame(janela, width=235, height=268)
Frame_corpo.grid(row=1,column=0) 

#criando botoes

b_1 = Button(Frame_corpo, text="C", width=16, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(Frame_corpo, text="%", width=7, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(Frame_corpo, text="/", width=7, height=3, bg=cor5, fg=cor2, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=178, y=0)


b_4 = Button(Frame_corpo, text="7", width=8, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=40)
b_5 = Button(Frame_corpo, text="8", width=8, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=40)
b_6 = Button(Frame_corpo, text="9", width=7, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=40)
b_7 = Button(Frame_corpo, text="*", width=7, height=3, bg=cor5, fg=cor2, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=178, y=40)

b_8 = Button(Frame_corpo, text="4", width=8, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=80)
b_9 = Button(Frame_corpo, text="5", width=8, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=80)
b_10 = Button(Frame_corpo, text="6", width=7, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=80)
b_11 = Button(Frame_corpo, text="-", width=7, height=3, bg=cor5, fg=cor2, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=178, y=80)

b_12 = Button(Frame_corpo, text="1", width=8, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=120)
b_13 = Button(Frame_corpo, text="2", width=8, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=120)
b_14 = Button(Frame_corpo, text="3", width=7, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=120)
b_15 = Button(Frame_corpo, text="+", width=7, height=3, bg=cor5, fg=cor2, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=178, y=120)

b_16 = Button(Frame_corpo, text="0", width=16, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=160)
b_17 = Button(Frame_corpo, text=".", width=7, height=3, bg=cor4, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=160)
b_18 = Button(Frame_corpo, text="=", width=7, height=3, bg=cor5, fg=cor2, font=('iv 9 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=178, y=160)





janela.mainloop() 


