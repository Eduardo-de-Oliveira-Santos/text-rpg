import os
import Status
import Variaveis
import Quarto
import Cidade
from Ferramentas_Diverças import limpa_tela


def hospital():
    while 1:
        if Variaveis.vida <= 0:
            limpa_tela()
            Variaveis.vida == Variaveis.vida_max
            print("voce esta curado ate mais")
            Cidade.cidade()

        elif Variaveis.vida < Variaveis.vida_max:
            limpa_tela()
            print("ola bem vindo ao hospital")
            print("voce parece machucado voce quer se curar?")
            print("1- sim")
            print("2- nao")
            Variaveis.text = int(input("oque fazer? "))
            if Variaveis.text == 1:
                limpa_tela()
                Variaveis.vida == Variaveis.vida_max
                print("voce esta curado ate mais")
                Cidade.cidade()

            if Variaveis.text == 2:
                limpa_tela()
                print("ok adeus")
                Cidade.cidade()
        
            
        elif Variaveis.vida >= Variaveis.vida_max:
            limpa_tela()
            print("voce ja esta saldavel nao a porque ficar aqui")
            Cidade.cidade()


        input('Enter para continuar')

if __name__ == '__main__':
     hospital()