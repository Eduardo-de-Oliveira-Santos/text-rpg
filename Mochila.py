import Player
import Quarto
import Cheats
import Variaveis
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
            
        if Variaveis.text == 513:
            Cheats.agilidade()
        if Variaveis.text == 514:
            Cheats.agilidade()
        if Variaveis.text == 515:
            Cheats.agilidade()
        if Variaveis.text == 516:
            Cheats.agilidade()
        if Variaveis.text == 517:
            Cheats.agilidade()
        if Variaveis.text == 518:
            Cheats.agilidade()
        

if __name__ == '__main__':
     mochila()