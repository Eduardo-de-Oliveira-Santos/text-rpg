import Variaveis
import os
import Player
from Ferramentas_Diverças import limpa_tela
from colorama import init, Fore, Style


def status():
    while 1:
        limpa_tela()
        print(f'{Fore.RED}Vida{Fore.RESET}:',Variaveis.vida)
        print(f'{Fore.RED}Poções{Fore.RESET}:',Variaveis.poçoes)
        print(f'{Fore.BLUE}Defesa{Fore.RESET}:',Variaveis.defesa)
        print(f'{Fore.RED}Atack{Fore.RESET}:',Variaveis.atack)
        print(f'{Fore.GREEN}Dinhero{Fore.RESET}:',Variaveis.dinheiro)
        print(f'{Fore.YELLOW}Nivel{Fore.RESET}:',Player.nivel)
        print(f'{Fore.YELLOW}XP{Fore.RESET}:',Player.xp)
        print(f'{Fore.GREEN}Ocupação{Fore.RESET}:',Player.ocupaçao)
        print(f'{Fore.RED}1- Sair{Fore.RESET}')
        Variaveis.text = int(input('oque fazer? '))

        #sair#
        if Variaveis.text == 1:
            return
        else:
            limpa_tela()
            print(f'{Fore.RED}Comando Invalido{Fore.RESET}')
        
        input(f'{Fore.GREEN}Enter para continuar{Fore.RESET}')
if __name__ == '__main__':
     status()
