import Historia  #Adicionar_infos
import Variaveis
from Ferramentas_Diverças import limpa_tela
from colorama import init, Fore, Style

init()

print(f'{Fore.RED}******************************************************************{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.GREEN}    ____  ________  _______  _   _______    __ __ ________  ___ {Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.GREEN}   / __ \/ ____/  |/  / __ \/ | / / ___/   / //_//  _/ __ \/   |{Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.GREEN}  / / / / __/ / /|_/ / / / /  |/ /\__ \   / ,<   / // /_/ / /| |{Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.GREEN} / /_/ / /___/ /  / / /_/ / /|  /___/ /  / /| |_/ // _, _/ ___ |{Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.GREEN}/_____/_____/_/  /_/\____/_/ |_//____/  /_/ |_/___/_/ |_/_/  |_|{Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}******************************************************************{Fore.RESET}')
print(f'{Fore.RED}******************************************************************{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.BLUE}      __    __           __               ___ __  _             {Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.BLUE}     / /_  / /___ ______/ /__   ___  ____/ (_) /_(_)___  ____   {Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.BLUE}    / __ \/ / __ `/ ___/ //_/  / _ \/ __  / / __/ / __ \/ __ \  {Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.BLUE}   / /_/ / / /_/ / /__/ ,<    /  __/ /_/ / / /_/ / /_/ / / / /  {Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}*{Fore.RESET}{Fore.BLUE}  /_.___/_/\__,_/\___/_/|_|   \___/\__,_/_/\__/_/\____/_/ /_/   {Fore.RESET}{Fore.RED}*{Fore.RESET}')
print(f'{Fore.RED}******************************************************************{Fore.RESET}')

print(f'{Fore.GREEN}1- jogar{Fore.RESET}')
print(f'{Fore.RED}2- sair{Fore.RESET}')
Variaveis.text = int(input("oque fazer? "))
#Começo do Jogo#
if Variaveis.text == 1:
    limpa_tela()
    Historia.enredo()
else:
    pass