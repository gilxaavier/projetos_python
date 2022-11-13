import sys
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

posicao_o = int(input("Digite a posição da peça o (0-8: \n"))

if posicao_o == 0:
    peca0 = "o" 
if posicao_o == 1:
    peca1 = "o" 
if posicao_o == 2:
    peca2 = "o" 
if posicao_o == 3:
    peca3 = "o" 
if posicao_o == 4:
    peca4 = "o" 
if posicao_o == 5:
    peca5 = "o" 
if posicao_o == 6:
    peca6 = "o" 
if posicao_o == 7:
    peca7 = "o" 
if posicao_o == 8:
    peca8 = "o" 

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


posicao_o = int(input("Digite a posicao da peca o (0-8):\n"))

if(posicao_o == 0):
    peca0 = 'o'
if(posicao_o == 1):
    peca1 = 'o'
if(posicao_o == 2):
    peca2 = 'o'
if(posicao_o == 3):
    peca3 = 'o'
if(posicao_o == 4):
    peca4 = 'o'
if(posicao_o == 5):
    peca5 = 'o'
if(posicao_o == 6):
    peca6 = 'o'
if(posicao_o == 7):
    peca7 = 'o'
if(posicao_o == 8):
    peca8 = 'o'

print(f"|{peca0}|{peca1}|{peca2}|")
print(f"|{peca3}|{peca4}|{peca5}|")
print(f"|{peca6}|{peca7}|{peca8}|")

posicao_x = int(input("Digite a posicao da peca x (0-8):\n"))

if(posicao_x == 0):
    peca0 = 'x'
if(posicao_x == 1):
    peca1 = 'x'
if(posicao_x == 2):
    peca2 = 'x'
if(posicao_x == 3):
    peca3 = 'x'
if(posicao_x == 4):
    peca4 = 'x'
if(posicao_x == 5):
    peca5 = 'x'
if(posicao_x == 6):
    peca6 = 'x'
if(posicao_x == 7):
    peca7 = 'x'
if(posicao_x == 8):
    peca8 = 'x'

print(f"|{peca0}|{peca1}|{peca2}|")
print(f"|{peca3}|{peca4}|{peca5}|")
print(f"|{peca6}|{peca7}|{peca8}|")

if (
    (peca0 == peca1 == peca2 == "x") or
    (peca3 == peca4 == peca5 == "x") or
    (peca6 == peca7 == peca8 == "x") or
    (peca1 == peca4 == peca7 == "x") or
    (peca2 == peca5 == peca8 == "x") or
    (peca0 == peca4 == peca8 == "x") or
    (peca2 == peca4 == peca6 == "x") 
):
    print("Parabéns, o jodaor ganhou.")
    sys.exit(0)