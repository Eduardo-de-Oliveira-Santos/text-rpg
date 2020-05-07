import vars
import os
import player
from ferramentas_diverças import limpa_tela


def status():
    while 1: #loop infinito, vai reduzir algumas linhas no codigo
        limpa_tela()
        print("Vida:",vars.vida)
        print("poções:",vars.poçoes)
        print("Defesa:",vars.defesa)
        print("Atack:",vars.atack)
        print("Dinhero:",vars.dinheiro)
        print("nivel:",player.nivel)
        print("xp:",player.xp)
        print("ocupação:",player.ocupaçao)
        print("1- sair")
        vars.text = int(input('oque fazer? '))

        #sair#
        if vars.text == 1:
            return
        else:
            pass

if __name__ == '__main__':
     status()
