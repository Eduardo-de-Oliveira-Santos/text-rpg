import os
import Dividir_Pontos
import Player
import Quarto
from Ferramentas_Diverças import limpa_tela

def Nome():
    limpa_tela()
    Player.nome = input("Qual vai ser seu nome? ")
    Player.idade = input("Qual vai ser sua idade? ")
    Quarto.game()
    #Dividir_Pontos.D_Pontos()
