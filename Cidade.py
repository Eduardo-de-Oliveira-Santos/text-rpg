import os
import Status
import vars
import Quarto
import Hospital

CLEAR = 'cls' if os.name == 'nt' else 'clear'
limpa_tela = lambda : os.system(CLEAR)

def cidade():
    while 1:
        limpa_tela()
        print("voce esta na sua cidade natal para onde ir?")
        print("0- status")
        print("1- voltar para a casa")
        print("2- ir para o hospital")
        print("3- ir para a loja")
        vars.text = int(input("oque fazer? "))

        if vars.text == 1:
            Quarto.game()
        elif vars.text == 2:
            Hospital.hospital()

        input('Enter para continuar')

if __name__ == '__main__':
     cidade()