import Variaveis
import Player
from Ferramentas_Diverças import limpa_tela

def mercante():
    while 1:
        limpa_tela()
        print("ola voçe quer comprar ou vender?")
        print("dinhero",Variaveis.dinheiro)
        print("1- Comprar")
        print("2- Vender")
        print("3- Sair")
        Variaveis.text = int(input("oque fazer? "))

        if Variaveis.text == 1:
            limpa_tela()
            print("dinheiro:",Variaveis.dinheiro)
            print("1- armas")
            print("2- armaduras")
            print("3- poções")
            print("4- Mochilas")
            print("5- sair")
            Variaveis.text = int(input("oque fazer? "))
            
            if Variaveis.text == 1:
                limpa_tela()
                print("|--------------------------------|")
                print("|dinheiro:",Variaveis.dinheiro,"                  |")
                print("|--------------------------------|")
                print("|1- espada de madeira    V$ 200  |")
                print("|--------------------------------|")
                print("|2- espada de pedra      V$ 500  |")
                print("|--------------------------------|")
                print("|3- espada de ferro      V$ 1000 |")
                print("|--------------------------------|")
                print("|4- espada de ouro       V$ 1500 |")
                print("|--------------------------------|")
                print("|5- espada de titaniun   V$ 2500 |")
                print("|--------------------------------|")
                print("|6- sair                         |")
                print("|--------------------------------|")
                Variaveis.text = int(input("oque fazer? "))
                
                if Variaveis.text == 1 and Variaveis.dinheiro <= 200:
                    limpa_tela()
                    print("comprou espada de madeira")
                    Variaveis.dinheiro -= 200
                    Player.mochila -= 1

                elif Variaveis.text == 1 and Variaveis.dinheiro > 200:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 2 and Variaveis.dinheiro <= 500:
                    limpa_tela()
                    print("comprou espada de pedra")
                    Variaveis.dinheiro -= 500
                    Player.mochila -= 1
                
                elif Variaveis.text == 2 and Variaveis.dinheiro > 500:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 3 and Variaveis.dinheiro <= 1000:
                    limpa_tela()
                    print("comprou espada de ferro")
                    Variaveis.dinheiro -= 1000
                    Player.mochila -= 1

                elif Variaveis.text == 3 and Variaveis.dinheiro > 1000:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 4 and Variaveis.dinheiro <= 1500:
                    limpa_tela()
                    print("comprou espada de ouro")
                    Variaveis.dinheiro -= 1500
                    Player.mochila -= 1

                elif Variaveis.text == 4 and Variaveis.dinheiro > 1500:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 5 and Variaveis.dinheiro <= 2500:
                    limpa_tela()
                    print("comprou espada de titaniun")
                    Variaveis.dinheiro -= 2500
                    Player.mochila -= 1

                elif Variaveis.text == 5 and Variaveis.dinheiro > 2500:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 6:
                    print("ok")
                
                
            elif Variaveis.text == 2:
                limpa_tela()
                print("|-----------------------------------|")
                print("|dinheiro:",Variaveis.dinheiro,"                     |")
                print("|-----------------------------------|")
                print("|1- armadura de couro       V$ 300  |")
                print("|-----------------------------------|")
                print("|2- armadura de anel        V$ 700  |")
                print("|-----------------------------------|")
                print("|3- armadura de ferro       V$ 1500 |")
                print("|-----------------------------------|")
                print("|4- armadura de ouro        V$ 2500 |")
                print("|-----------------------------------|")
                print("|5- armadura de titanium    V$ 4000 |")
                print("|-----------------------------------|")
                print("|6- armadura de samurai     V$ 6000 |")
                print("|-----------------------------------|")
                print("|6- sair                            |")
                print("|-----------------------------------|")
                Variaveis.text = int(input("oque fazer? "))
                if Variaveis.text == 1 and Variaveis.dinheiro <= 300:
                    limpa_tela()
                    print("comprou armadura de couro")
                    Variaveis.dinheiro -= 300
                    Player.mochila -= 1

                elif Variaveis.text == 1 and Variaveis.dinheiro > 300:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 2 and Variaveis.dinheiro <= 700:
                    limpa_tela()
                    print("comprou armadura de anel")
                    Variaveis.dinheiro -= 700
                    Player.mochila -= 1
                
                elif Variaveis.text == 2 and Variaveis.dinheiro > 700:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 3 and Variaveis.dinheiro <= 1500:
                    limpa_tela()
                    print("comprou armadura de ferro")
                    Variaveis.dinheiro -= 1500
                    Player.mochila -= 1

                elif Variaveis.text == 3 and Variaveis.dinheiro > 1500:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 4 and Variaveis.dinheiro <= 2500:
                    limpa_tela()
                    print("comprou armadura de ouro")
                    Variaveis.dinheiro -= 2500
                    Player.mochila -= 1

                elif Variaveis.text == 4 and Variaveis.dinheiro > 2500:
                    limpa_tela()
                    print("voce nao tem dinheiro")

                if Variaveis.text == 5 and Variaveis.dinheiro <= 4000:
                    limpa_tela()
                    print("comprou armadura de titaniun")
                    Variaveis.dinheiro -= 4000
                    Player.mochila -= 1

                elif Variaveis.text == 5 and Variaveis.dinheiro > 4000:
                    limpa_tela()
                    print("voce nao tem dinheiro")
                
                if Variaveis.text == 6 and Variaveis.dinheiro <= 6000:
                    limpa_tela()
                    print("comprou armadura de samurai")
                    Variaveis.dinheiro -= 6000
                    Player.mochila -= 1

                elif Variaveis.text == 6 and Variaveis.dinheiro > 6000:
                    limpa_tela()
                    print("voce nao tem dinheiro")
                
                if Variaveis.text == 7:
                    print("ok")
                
            
            elif Variaveis.text == 5:
                return
        
        elif Variaveis.text == 2:
            print("dinheiro:",Variaveis.dinheiro)

        elif Variaveis.text == 3:
            return

        input("aperte enter!")
if __name__ == '__main__':
    mercante()