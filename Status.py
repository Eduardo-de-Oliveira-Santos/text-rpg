import vars
import os

CLEAR = 'cls' if os.name == 'nt' else 'clear' 
limpa_tela = lambda : os.system(CLEAR)

def status():
    while 1: #loop infinito, vai reduzir algumas linhas no codigo
        #Status#
        limpa_tela()
        print("1- vida")
        print("2- defesa")
        print("3- atack")
        print("4- dinhero")
        print("5- poçoes")
        print("6- sair")
        vars.text = int(input("oque fazer? "))

        #check vida#
        if vars.text == 1:
            print("vida:",vars.vida)
        
        #check defesa#
        elif vars.text == 2:
            print("defesa:",vars.defesa)

        #check atack#
        elif vars.text == 3:
            print("atack:",vars.atack)

        #check dinhero#
        elif vars.text == 4:
            print("dinhero:",vars.dinheiro)
                                                                                     
        #check poçoes#
        elif vars.text == 5:
            print("poçoes:",vars.poçoes)

        #sair#
        elif vars.text == 6:
            return
            
        input('Enter para continuar')
if __name__ == '__main__':
     status()
