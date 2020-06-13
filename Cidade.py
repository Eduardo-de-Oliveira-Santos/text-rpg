import os
import Status
import Variaveis
import Quarto
import Hospital
import Loja
import Slime
from Ferramentas_Diverças import limpa_tela

def cidade():
    while 1:
        limpa_tela()
        print("voce esta na sua cidade natal para onde ir?")
        print("0- status")
        print("1- voltar para a casa")
        print("2- ir para o hospital")
        print("3- ir para a loja")
        print("4- ir para a floresta")
        Variaveis.text = int(input("oque fazer? "))
        if Variaveis.text == 0:
            limpa_tela()
            Status.status()
        if Variaveis.text == 1:
            Quarto.game()
        elif Variaveis.text == 2:
            Hospital.hospital()
        elif Variaveis.text == 3:
            Loja.mercante()
        elif Variaveis.text == 4:
            Slime.batalha()


        input('Enter para continuar')

if __name__ == '__main__':
     cidade()