import player
import vars
import Quarto
from ferramentas_diverças import limpa_tela

pontos = 20

def dividir_pontos():
    while 1:
        print("pontos disponiveis:",pontos)
        print("1- agilidade ")
        print("2- furtividade")
        print("3- sorte")
        print("4- labia")
        print("5- inteligencia")
        print("6- força")
        print("7- mira")
        print("8- carisma")
        vars.text = int(input("oque fazer? "))

        if vars.text == 1:
            player.agilidade += 1
        if vars.text == 2:
            player.furtividade += 1
        if vars.text == 3:
            player.sorte += 1
        if vars.text == 4:
            player.labia += 1
        if vars.text == 5:
            player.inteligencia += 1
        if vars.text == 6:
            player.força += 1
        if vars.text == 7:
            player.mira += 1
        if vars.text == 8:
            player.carisma += 1
        if pontos == 0:
            Quarto.game()


    