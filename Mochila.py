import player
import Quarto

def mochila():
    while 1:
        print("espaços disponiveis:",player.mochila)
        print(player.itens)
        print("1- voltar")
        vars.text = int(input("oque fazer? "))

        if vars.text == 1:
            return

if __name__ == '__main__':
     mochila()