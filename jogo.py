# Jogo de adivinhar o número
# Escreva o código embaixo:

import random

secreto = random.randint(1, 100)
tentativas = 0

print("pensei em um numero de 1 a 100. tente adivinhar!")

while True:
    palpite = int(input("seu palpite: "))
    tentativas = tentativas + 1

    if palpite < secreto:
        print("e maior que isso")
    elif palpite > secreto:
        print("e menor que isso")
    else:
        print(f"acertou! era {secreto}. voce precisou de {tentativas} tentativas")
        break