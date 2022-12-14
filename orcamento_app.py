from tkinter import *
from tkinter import Tk, ttk

color_0 = "#2e2d2b"
color_1 = "#feffff"
color_2 = "#4fa882"
color_3 = "#38576b"
color_4 = "#403d3d"
color_5 = "#e06636"
color_6 = "#038cfc"
color_7 = "#3fbfb9"
color_8 = "#263238"
color_9 = "#e9edf5"
color_10 = "#6e8faf"
color_11 = "#f2f4f2"

#CRiando janela
janela = Tk()
janela.title("")
janela.geometry("250x400")
janela.configure(background=color_1)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Frane 

frame_cima = Frame(janela, width=300, height=50, bg=color_1, relief="flat")
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=300, height=90, bg=color_1, relief="flat")
frame_meio.grid(row=1, column=0)

frame_baixo = Frame(janela, width=300, height=290, bg=color_9, relief="flat")
frame_baixo.grid(row=2, column=0)

app_ = Label(frame_cima, text="Orçamento", compound=LEFT, padx=5, relief=FLAT, font=("Verdana 20"), bg=color_1, fg=color_4)
app_.place(x=0, y=0)


app_linha = Label(frame_cima,width=295, relief=FLAT, font=("Verdana 1"), bg=color_3, fg=color_4)
app_linha.place(x=0, y=47)

def calcular():
    salary = float(e_valor.get())

    fifty_percent = (50 / 100) * salary
    thirty_percent = (30 / 100) * salary
    twenty_percent = (20 / 100) * salary

    necessidades["text"] = (f"R${fifty_percent:.2f}")
    gastos["text"] =(f"R${thirty_percent:.2f}")
    poupanca["text"] =(f"R${twenty_percent:.2f}")

    print("-"* 20)


app_ = Label(frame_meio, text="Renda Mensal: ", relief=FLAT, anchor=NW,  font=("Ivy 10"), bg=color_1, fg=color_4)
app_.place(x=7, y=15)

e_valor = Entry(frame_meio, width=10, font="Ivy 14", justify="center", relief="solid")
e_valor.place(x=10, y=47)


b_calcular= Button(frame_meio,command=calcular, text="Calcular".upper(), relief=RIDGE, anchor=NW, font=("Ivy 10"), bg=color_1, fg=color_4)
b_calcular.place(x=150, y=40)

app_ = Label(frame_baixo, text="Seus valores de 50% 30% 20%", relief=FLAT, width=35, anchor=NW,  font=("Verdana 11"), bg=color_3, fg=color_1)
app_.place(x=0, y=0)

total_necessidades = Label(frame_baixo, text="Necessidades: ", relief=FLAT, width=35, anchor=NW,  font=("Verdana 11"), bg=color_9, fg=color_0)
total_necessidades.place(x=19, y=40)

necessidades = Label(frame_baixo, relief=FLAT, width=35, anchor=NW,  font=("Verdana 12"), bg=color_1, fg=color_4)
necessidades.place(x=10, y=75)


total_gastos = Label(frame_baixo, text="Gastos: ", relief=FLAT, width=35, anchor=NW,  font=("Verdana 11"), bg=color_9, fg=color_0)
total_gastos.place(x=10, y=115)

gastos = Label(frame_baixo, relief=FLAT, width=35, anchor=NW,  font=("Verdana 12"), bg=color_1, fg=color_4)
gastos.place(x=10, y=145)


total_poupanca = Label(frame_baixo, text="Poupanças: ", relief=FLAT, width=35, anchor=NW,  font=("Verdana 10"), bg=color_9, fg=color_0)
total_poupanca.place(x=10, y=185)

poupanca = Label(frame_baixo, relief=FLAT, width=35, anchor=NW,  font=("Verdana 12"), bg=color_1, fg=color_4)
poupanca.place(x=10, y=215)


janela.mainloop()