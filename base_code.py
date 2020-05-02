import os
import Status
import vars
import Quarto

CLEAR = 'cls' if os.name == 'nt' else 'clear' 
limpa_tela = lambda : os.system(CLEAR)

#Menu#
print("                                                                      ")
print("#######                                       ######  ######   #####  ")
print("   #    ###### #    # #####                   #     # #     # #     # ")
print("   #    #       #  #    #                     #     # #     # #       ")
print("   #    #####    ##     #                     ######  ######  #  #### ")
print("   #    #        ##     #                     #   #   #       #     # ")
print("   #    #       #  #    #                     #    #  #       #     # ")
print("   #    ###### #    #   #                     #     # #        #####  ")
print("                                                                      ")

print("1- jogar")
print("2- sair")
vars.text = int(input("oque fazer? "))
#Começo do Jogo#
if vars.text == 1:
    limpa_tela()
    Quarto.game()
    pass
else:
    pass
