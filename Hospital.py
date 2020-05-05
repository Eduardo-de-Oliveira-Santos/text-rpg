import os
import Status
import vars
import Quarto
import Cidade
from ferramentas_diverças import limpa_tela


def hospital():
    while 1:
        if vars.vida < vars.vida_max:
            limpa_tela()
            print("ola bem vindo ao hospital")
            print("voce parece machucado voce quer se curar?")
            print("1- sim")
            print("2- nao")
            vars.text = int(input("oque fazer? "))
            if vars.text == 0:
                limpa_tela()
                Status.status()
            elif vars.text == 1:
                limpa_tela()
                vars.vida = vida_max
                print("voce esta curado ate mais")
                return
            if vars.text == 2:
                limpa_tela()
                print("ok adeus")
                return
        if vars.vida >= vars.vida_max:
            limpa_tela()
            print("voce ja esta saldavel nao a porque ficar aqui")
            return
        input('Enter para continuar')

if __name__ == '__main__':
     hospital()