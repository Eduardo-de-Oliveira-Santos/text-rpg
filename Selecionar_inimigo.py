import random
import Unknown
import Unknown_1
import Bandido
import Bruxa#
import Cavaleiro#
import Demonio#
import Goblin#
import Lobo#
import Unknown_2#
import Slime#
import Urso#
import Zumbis#

def selecionar():
    monstro_selecionado = random.randrange(1, 12)
    if monstro_selecionado == 1:
        Slime.batalha()
    
    if monstro_selecionado == 2:
        Zumbis.batalha()
    
    if monstro_selecionado == 3:
        Urso.batalha()
    
    if monstro_selecionado == 4:
        Lobo.batalha()
    
    if monstro_selecionado == 5:
        Unknown_2.batalha()
    
    if monstro_selecionado == 6:
        Goblin.batalha()
    
    if monstro_selecionado == 7:
        Demonio.batalha()
    
    if monstro_selecionado == 8:
        Cavaleiro.batalha()

    if monstro_selecionado == 9:
        Bruxa.batalha()

    if monstro_selecionado == 10:
        Bandido.batalha()

    if monstro_selecionado == 11:
        Unknown.batalha()
        
    if monstro_selecionado == 12:
        Unknown_1.batalha()
