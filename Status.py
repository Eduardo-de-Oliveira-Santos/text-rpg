import Variaveis
import os
import Player
from Ferramentas_Diverças import limpa_tela


def status():
    while 1: #loop infinito, vai reduzir algumas linhas no codigo
        limpa_tela()
        print("Vida:",Variaveis.vida)
        print("poções:",Variaveis.poçoes)
        print("Defesa:",Variaveis.defesa)
        print("Atack:",Variaveis.atack)
        print("Dinhero:",Variaveis.dinheiro)
        print("nivel:",Player.nivel)
        print("xp:",Player.xp)
        print("ocupação:",Player.ocupaçao)
        print("1- sair")
        Variaveis.text = int(input('oque fazer? '))

        #sair#
        if Variaveis.text == 1:
            return
        else:
            print("comando invalido")
        

if __name__ == '__main__':
     status()
