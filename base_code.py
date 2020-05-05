import os
import Status
import vars
import Quarto
from ferramentas_diverças import limpa_tela


#Menu#
print("                                                                                            ")
print("_|_|_|_|_|  _|_|_|_|  _|      _|  _|_|_|_|_|                  _|_|_|    _|_|_|      _|_|_|  ")
print("    _|      _|          _|  _|        _|                      _|    _|  _|    _|  _|        ")
print("    _|      _|_|_|        _|          _|                      _|_|_|    _|_|_|    _|  _|_|  ")
print("    _|      _|          _|  _|        _|                      _|    _|  _|        _|    _|  ")
print("    _|      _|_|_|_|  _|      _|      _|                      _|    _|  _|          _|_|_|  ")
print("                                                                                            ")

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
