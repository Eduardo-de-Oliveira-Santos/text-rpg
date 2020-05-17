import Adicionar_infos
import Variaveis
from Ferramentas_Diverças import limpa_tela


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
Variaveis.text = int(input("oque fazer? "))
#Começo do Jogo#
if Variaveis.text == 1:
    limpa_tela()
    Adicionar_infos.Nome()
    pass
else:
    pass
