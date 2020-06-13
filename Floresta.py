import os
import Status
import Variaveis
import Player
import Slime
from Ferramentas_Diverças import limpa_tela


def floresta():
    while 1:
        limpa_tela()
        print("0- Status")
        print("1- voltar para a cidade")
        print("2- cortar arvores")
        print("3- procurar monstros")
        Variaveis.text = int(input("oque fazer? "))

        if Variaveis.text == 0:
            limpa_tela()
            Status.status()
            
        if Variaveis.text == 1:
            return
        
        if Variaveis.text == 2:
            limpa_tela()
            print("cortou 1 tronco de madeira")
            Player.madeiras += 1

        if Variaveis.text == 3:
            limpa_tela()
            Slime.batalha()
            

        input('Enter para continuar')



    
if __name__ == '__main__':
     floresta()
