import os
import Status
import Variaveis
import Quarto
import Cidade
from Ferramentas_Diverças import limpa_tela


def hospital():
    while 1:
        if Variaveis.vida < Variaveis.vida_max:
            limpa_tela()
            print("ola bem vindo ao hospital")
            print("voce parece machucado voce quer se curar?")
            print("1- sim")
            print("2- nao")
            Variaveis.text = int(input("oque fazer? "))
            if Variaveis.text == 0:
                limpa_tela()
                Status.status()
            elif Variaveis.text == 1:
                limpa_tela()
                Variaveis.vida = vida_max
                print("voce esta curado ate mais")
                return
            if Variaveis.text == 2:
                limpa_tela()
                print("ok adeus")
                return
        if Variaveis.vida >= Variaveis.vida_max:
            limpa_tela()
            print("voce ja esta saldavel nao a porque ficar aqui")
            return
        input('Enter para continuar')

if __name__ == '__main__':
     hospital()