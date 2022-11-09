import random
print("Você tem 8 tentativas para acertar um número entre 0 e 100")

#Foi proposta a ciação de um jogo de advinhação entre os valores de 0 a 100, na qual o jogador tem 8 chances para acertar o valor. 

aleatorio = random.randint(0, 100)
print(aleatorio)
count = 1

while True:
    chute = int (input("Digite um número entre 0 e 100: "))
    
    if chute == aleatorio:
        print(f"Parabéns! você acertou, o número aleatório era: {aleatorio}!")
        break
    
    if count == 8:
        print(f"Que pena, suas chances acabaram o número aleatório era: {aleatorio}.")
        break
    
    elif chute > aleatorio:
        print("Você errou, chute um valor menor.")
        
    elif chute < aleatorio:
        print("Você errou chute um valor maior.")
    
    count +=1
    
    
    
    
    