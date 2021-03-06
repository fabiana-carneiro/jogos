print("#################################")
print("Bem vindo ao jogo de Adivinhação!")
print("#################################")

numero_secreto = 23
total_tentativas = 3


for rodada in range(1,total_tentativas + 1) :
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou ", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o numero secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o numero secreto.")

    rodada = rodada + 1

print("Fim de jogo!")