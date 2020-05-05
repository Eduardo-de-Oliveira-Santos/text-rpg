import os
import Status
import vars
import Quarto
import Hospital
from ferramentas_diverças import limpa_tela

def cidade():
    while 1:
        limpa_tela()
        print("voce esta na sua cidade natal para onde ir?")
        print("0- status")
        print("1- voltar para a casa")
        print("2- ir para o hospital")
        print("3- ir para a loja")
        vars.text = int(input("oque fazer? "))
        if vars.text == 0:
            limpa_tela()
            Status.status()
        if vars.text == 1:
            Quarto.game()
        elif vars.text == 2:
            Hospital.hospital()

        input('Enter para continuar')

if __name__ == '__main__':
     cidade()