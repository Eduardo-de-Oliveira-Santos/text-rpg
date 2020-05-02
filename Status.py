import vars
import os

CLEAR = 'cls' if os.name == 'nt' else 'clear' 
limpa_tela = lambda : os.system(CLEAR)

def status():
    while 1: #loop infinito, vai reduzir algumas linhas no codigo
        limpa_tela()
        print(" ________________________________________________________")
        print("|  Vida:",vars.vida,"/////////","poções:",vars.poçoes,"//|")
        print("|////////////////////////////////////////////////////////|")
        print("|////////////////////////////////////////////////////////|")
        print("|////////////////////////////////////////////////////////|")
        print("|  Defesa:",vars.defesa,"////////","Atack:",vars.atack,"/|")
        print("|////////////////////////////////////////////////////////|")
        print("|////////////////////////////////////////////////////////|")
        print("|///////////////Dinhero:",vars.dinheiro,"////////////////|")
        print("|////////////////////////////////////////////////////////|")
        print("|                      1- sair                           |")
        print("|________________________________________________________|")


        #sair#
        if vars.text == 1:
            return
            
        vars.text = input('oque fazer? ')
if __name__ == '__main__':
     status()
