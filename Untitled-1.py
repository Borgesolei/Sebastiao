import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opcoes)
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()

    if jogador not in opcoes:
        print("Opção inválida. Tente novamente.")
        return

    print(f"Computador escolheu: {computador}")
    print(f"Jogador escolheu: {jogador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
