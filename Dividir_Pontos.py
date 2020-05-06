import player
import vars
import Quarto
from ferramentas_diverças import limpa_tela

pontos = 20

def dividir_pontos():
    while 1:
        print("pontos disponiveis:",pontos)
        print("1- agilidade = ",player.agilidade)
        print("2- furtividade = ",player.furtividade)
        print("3- sorte = ",player.sorte)
        print("4- labia = ",player.labia)
        print("5- inteligencia = ",player.inteligencia)
        print("6- força = ",player.força)
        print("7- mira = ",player.mira)
        print("8- carisma = ",player.carisma)
        vars.text = int(input("oque fazer? "))

        if vars.text == 1:
            player.agilidade += 1
            pontos -= 1
            limpa_tela()
        if vars.text == 2:
            player.furtividade += 1
            pontos -= 1
            limpa_tela()
        if vars.text == 3:
            player.sorte += 1
            pontos -= 1
            limpa_tela()
        if vars.text == 4:
            player.labia += 1
            pontos -= 1
            limpa_tela()
        if vars.text == 5:
            player.inteligencia += 1
            pontos -= 1
            limpa_tela()
        if vars.text == 6:
            player.força += 1
            pontos -= 1
            limpa_tela()
        if vars.text == 7:
            player.mira += 1
            pontos -= 1
            limpa_tela()
        if vars.text == 8:
            player.carisma += 1
            pontos -= 1
            limpa_tela()
        if pontos == 0:
            Quarto.game()

if __name__ == '__main__':
     status()


    