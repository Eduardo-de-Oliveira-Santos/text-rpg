import os
import Dividir_Pontos
import Player
from Ferramentas_Diverças import limpa_tela

def Nome():
    limpa_tela()
    Player.nome = input("Qual vai ser seu nome? ")
    Player.idade = input("Qual vai ser sua idade? ")
    Dividir_Pontos.D_Pontos()
