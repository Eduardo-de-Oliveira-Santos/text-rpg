import Historia  #Adicionar_infos
import Variaveis
from Ferramentas_Diverças import limpa_tela


print("******************************************************************")
print("*    ____  ________  _______  _   _______    __ __ ________  ___ *")
print("*   / __ \/ ____/  |/  / __ \/ | / / ___/   / //_//  _/ __ \/   |*")
print("*  / / / / __/ / /|_/ / / / /  |/ /\__ \   / ,<   / // /_/ / /| |*")
print("* / /_/ / /___/ /  / / /_/ / /|  /___/ /  / /| |_/ // _, _/ ___ |*")
print("*/_____/_____/_/  /_/\____/_/ |_//____/  /_/ |_/___/_/ |_/_/  |_|*")
print("******************************************************************")
print("******************************************************************")
print("*      __    __           __               ___ __  _             *")
print("*     / /_  / /___ ______/ /__   ___  ____/ (_) /_(_)___  ____   *")
print("*    / __ \/ / __ `/ ___/ //_/  / _ \/ __  / / __/ / __ \/ __ \  *")
print("*   / /_/ / / /_/ / /__/ ,<    /  __/ /_/ / / /_/ / /_/ / / / /  *")
print("*  /_.___/_/\__,_/\___/_/|_|   \___/\__,_/_/\__/_/\____/_/ /_/   *")
print("******************************************************************")

print("1- jogar")
print("2- sair")
Variaveis.text = int(input("oque fazer? "))
#Começo do Jogo#
if Variaveis.text == 1:
    limpa_tela()
    Historia.enredo()
else:
    pass