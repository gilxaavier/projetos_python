print ("=" *30)
print("Bem vindo ao jogo da velha")
print("O jogo começa com o jogador 'x' e depois com o jogador 'o'")

print("Tabuleiro")
print("|_|_|_|")
print("|_|_|_|")
print("| | | |")

input("Aperte qualquer tecla para começar! \n")

peca0 = "_"
peca1 = "_"
peca2 = "_"
peca3= "_"
peca4 = "_"
peca5 = "_"
peca6 = " "
peca7 = " "
peca8 = " "

print("Inicio")
print(f"|{peca0}|{peca1}|{peca2} ")
print(f"|{peca3}|{peca4}|{peca5} ")
print(f"|{peca6}|{peca7}|{peca8} ")

posicao_x = int(input("Digite a posição da peça x (0-8): \n"))

if posicao_x == 0:
    peca0= "x"
if posicao_x == 1:
    peca1 = "x"
if posicao_x == 2:
    peca2 = "x"
if posicao_x == 3:
    peca3 = "x"
if posicao_x == 4:
    peca4 = "x"
if posicao_x == 5:
    peca5 = "x"
if posicao_x == 6:
    peca6 = "x"
if posicao_x == 7:
    peca7 = "x"
if posicao_x ==8:
    peca8 = "x"

print(f"|{peca0}|{peca1}|{peca2} ")
print(f"|{peca3}|{peca4}|{peca5} ")
print(f"|{peca6}|{peca7}|{peca8} ")