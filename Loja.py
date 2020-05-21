import Variaveis
from Ferramentas_Diverças import limpa_tela

def mercante():
    while 1:
        limpa_tela()
        print("ola voçe quer comprar ou vender?","dinhero",Variaveis.dinheiro)
        print("1- Comprar")
        print("2- Vender")
        print("3- Sair")
        Variaveis.text = int(input("oque fazer? "))

        if Variaveis.text == 1:
            print("dinheiro:",Variaveis.dinheiro)
            
        
        if Variaveis.text == 2:
            print("dinheiro:",Variaveis.dinheiro)

        if Variaveis.text == 3:
            return

        input("aperte enter!")
if __name__ == '__main__':
    mercante()