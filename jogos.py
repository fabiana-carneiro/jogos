from forca import jogar_forca
from adivinhacao import jogar_adivinhacao

def escolha_jogo():

    print("#################################")
    print("#######Escolha o seu jogo!#######")
    print("#################################")

    print("(1)Forca (2)Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        jogar_forca()
    elif(jogo == 2):
        print("Jogando adivinhação")
        jogar_adivinhacao()

if(__name__ == "__main__"):
    escolha_jogo()