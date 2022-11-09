import random 

# Foi proposta a criação de um dado, no qual o úsuario decide se quer ou não joga-lo.

print("Você gostaria de jogar o dado? \n --------------------------")

jogar = ["SIM", "Sim", "sim", "S", "s" ]
while True:
    dado = input("Você gostaria de jogar o dado? ")
    if dado  in  jogar:
        x = random.randint(1, 6)
        print(f"Bela jogada, o valor sorteado foi: {x}")

        print("-----------------------------")
    
    else:
        print(f"Jogo encerrado.")
        break
