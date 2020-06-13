import os
import Status
import Variaveis
import Cidade
import Player
import Mochila
from Ferramentas_Diverças import limpa_tela


def game():
    while 1:
        limpa_tela()
        print("você acorda em um quarto com uma espada um arco uma armadura e um escudo")
        print("0- status")
        print("1- mochila")
        print("2- pegar espada")
        print("3- pegar arco")
        print("4- pegar armadura")
        print("5- pegar escudo")
        print("6- procurar outras coisas")
        print("7- sair do quarto")
        Variaveis.text = int(input("oque fazer? "))

        #Status#
        if Variaveis.text == 0:
           limpa_tela()
           Status.status()

        elif Variaveis.text == 1:
            limpa_tela()
            Mochila.mochila()

        #Pegou Espada#
        elif Variaveis.text == 2:
            limpa_tela()
            print("voce pegou a espada ruim")
            Player.itens += "espada ruim"
            Variaveis.itens_pegos += 1
            Player.mochila -= 1
            Variaveis.atack += 10

        #Pegou Arco#
        elif Variaveis.text == 3:
            limpa_tela()
            print("voce pegou o arco velho")
            Player.itens += "arco velho"
            Variaveis.itens_pegos += 1
            Player.mochila -= 1
            Variaveis.atack_longa_distancia += 10

        #Pegou Armadura#
        elif Variaveis.text == 4:
            limpa_tela()
            print("voce pegou o armadura estragada")
            Player.itens += "armadura estragada"
            Variaveis.itens_pegos += 1
            Player.mochila -= 1
            Variaveis.defesa += 10

        #Pegou Escudo#
        elif Variaveis.text == 5:
          limpa_tela()
          print("voce pegou o escudo quebrado")
          Player.itens += "escudo quebrado"
          Variaveis.itens_pegos += 1
          Player.mochila -= 1
          Variaveis.defesa += 10


        #Procurar Outras Coisas#
        elif Variaveis.text == 6:
            limpa_tela()
            print("você achou um bau pareçe estar destrancado")
            print("1- abrir")
            print("2- deixar pra lá")
            Variaveis.text = int(input("oque fazer? "))
            if Variaveis.text == 1 and Variaveis.dinheiro >= 500:
                print("voce achou 1000 moedas")
                Variaveis.dinheiro += 1000

        #Sair do Quarto#
        elif Variaveis.text == 7:
            limpa_tela()
            if Variaveis.itens_pegos == 1:
                Cidade.cidade()
            else:
                print("você quer sair sem pegar nada?")
                print("1- sair")
                print("2- voltar")
                Variaveis.text = int(input("oque fazer? "))
                if Variaveis.text == 1:
                    Cidade.cidade()
                else:
                    print("acho melhor pegar algo primeiro")
        
        else:
            print("comando invalido")
            
        input('Enter para continuar')
if __name__ == '__main__':
     game()
