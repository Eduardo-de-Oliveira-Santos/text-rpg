import os
import Variaveis
import Dividir_Pontos
import Player
from Ferramentas_Diverças import limpa_tela

def Nome():
    limpa_tela()
    Player.Nome = input("Qual vai ser seu nome? ")
    Dividir_Pontos.dividir_pontos()
