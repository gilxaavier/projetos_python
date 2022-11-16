from tkinter import * 
from datetime import datetime
import tkinter as tk

cor1 = "#3d3d3d"
cor2 = "#fafcff"
cor3 = "#23c25c"
cor4 = "#eb463b"
cor5 = "#dedcdc"
cor6 = "#3080f0"

fundo = cor1
cor = cor2

janela = Tk()

janela.title()
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

tempo = datetime.now()

hora = tempo.strftime("%H:%M:%S")
dia_semana = tempo.strftime("%A")
dia = tempo.day
mes = tempo.strftime("%b")

print(hora)

janela.mainloop()