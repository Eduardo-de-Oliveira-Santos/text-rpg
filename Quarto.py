import os
import Status
import vars

CLEAR = 'cls' if os.name == 'nt' else 'clear' 
limpa_tela = lambda : os.system(CLEAR)

def game():
    while 1:
        limpa_tela()
        print("você acorda em um quarto com uma espada um arco uma armadura e um escudo")
        print("0- status")
        print("1- pegar espada")
        print("2- pegar arco")
        print("3- pegar armadura")
        print("4- pegar escudo")
        print("5- procurar outras coisas")
        print("6- sair do quarto")
        vars.text = int(input("oque fazer? "))

        #Status#
        if vars.text == 0:
           limpa_tela()
           Status.status()

        #Pegou Espada#
        elif vars.text == 1:
            limpa_tela()
            print("voce pegou a espada")
            vars.itens += ("espada")
            vars.itens_pegos += 1
            vars.atack += 10

        #Pegou Arco#
        elif vars.text == 2:
            limpa_tela()
            print("voce pegou o arco")
            vars.itens += ("arco")
            vars.itens_pegos += 1
            vars.atack_longa_distancia += 10

        #Pegou Armadura#
        elif vars.text == 3:
            limpa_tela()
            print("voce pegou o armadura")
            vars.itens += ("armadura")
            vars.itens_pegos += 1
            vars.defesa += 10

        #Pegou Escudo#
        elif vars.text == 4:
          limpa_tela()
          print("voce pegou o escudo")
          vars.itens += ("escudo")
          vars.itens_pegos += 1
          vars.defesa += 10


        #Procurar Outras Coisas#
        elif vars.text == 5:
            limpa_tela()
            print("você achou um bau pareçe estar destrancado")
            print("1- abrir")
            print("2- deixar pra lá")
            vars.text = int(input("oque fazer? "))
            if vars.text == 1:
                print("voce achou 1000 moedas")
                vars.dinheiro += 1000

        #Sair do Quarto#
        elif vars.text == 6:
            limpa_tela()
            if vars.itens >= 1:
                pass
            else:
                print("você quer sair sem pegar nada?")
                print("1- sair")
                print("2- voltar")
                vars.text = int(input("oque fazer? "))
                pass
        
        
        input('Enter para continuar')
if __name__ == '__main__':
     game()
