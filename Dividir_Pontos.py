import Player
import Variaveis
import Quarto
from Ferramentas_Diverças import limpa_tela

pontos = 20

def dividir_pontos():
    while 1:
        print("pontos disponiveis:", pontos)
        print("1- agilidade = ", Player.agilidade)
        print("2- furtividade = ", Player.furtividade)
        print("3- sorte = ", Player.sorte)
        print("4- labia = ", Player.labia)
        print("5- inteligencia = ", Player.inteligencia)
        print("6- força = ", Player.força)
        print("7- mira = ", Player.mira)
        print("8- carisma = ", Player.carisma)
        Variaveis.text = int(input("oque fazer? "))
        if Variaveis.text == 1:
            Player.agilidade += 1
            pontos -= 1
            limpa_tela()
        elif Variaveis.text == 2:
            Player.furtividade += 1
            pontos -= 1
            limpa_tela()
        elif Variaveis.text == 3:
            Player.sorte += 1
            pontos -= 1
            limpa_tela()
        elif Variaveis.text == 4:
            Player.labia += 1
            pontos -= 1
            limpa_tela()
        elif Variaveis.text == 5:
            Player.inteligencia += 1
            pontos -= 1
            limpa_tela()
        elif Variaveis.text == 6:
            Player.força += 1
            pontos -= 1
            limpa_tela()
        elif Variaveis.text == 7:
            Player.mira += 1
            pontos -= 1
            limpa_tela()
        elif Variaveis.text == 8:
            Player.carisma += 1
            pontos -= 1
            limpa_tela()
        elif pontos == 0:
            Quarto.game()

        input('Enter para continuar')

if __name__ == '__main__':
    dividir_pontos()


    
