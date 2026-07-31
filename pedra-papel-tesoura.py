# PASSO 1 — fazer só o computador jogar
# 1. importe a biblioteca de sorteio (igual você fez no jogo.py)
# 2. crie uma variável com a lista das 3 opções
# 3. sorteie uma delas
# 4. imprima o que saiu
import  random

meus_pontos = 0
pontos_do_computador = 0

while meus_pontos < 3 and pontos_do_computador < 3:
    opçoes = ["pedra", "papel", "tesoura"]
    sorteio = random.choice(opçoes)
    print("o computador escolheu:", sorteio)

    jogador = input("sua jogada? ").lower().strip()
    print(f"você: {jogador} x computador: {sorteio}")

    if jogador == sorteio:
        print("empate!")
    elif (jogador == "pedra" and sorteio == "tesoura") or (jogador == "papel" and sorteio == "pedra") or (jogador == "tesoura" and sorteio == "papel"):
        print("você ganhou!")
        meus_pontos +=1
    else:
        print("você perdeu!")
        pontos_do_computador +=1
        
    print(f"placar: você {meus_pontos} x computador {pontos_do_computador}")
