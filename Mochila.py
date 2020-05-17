import Player
import Quarto
from Ferramentas_Diverças import limpa_tela


def mochila():
    while 1:
        limpa_tela()
        print("espaços disponiveis:",Player.mochila)
        print(Player.itens)
        print("1- voltar")
        Variaveis.text = int(input("oque fazer? "))

        if Variaveis.text == 1:
            return

if __name__ == '__main__':
     mochila()