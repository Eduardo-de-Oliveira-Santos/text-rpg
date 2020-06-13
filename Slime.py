import Monstros_vars
import Variaveis
import Player
import random
import Hospital
from Ferramentas_Diverças import limpa_tela
 

def batalha():
    while 1:
        limpa_tela()
        print("-----------------------------------")
        print("{Inimigo} vida:",Monstros_vars.vida_slime)
        print("-----------------------------------")
        print("")
        print("")
        print("")
        print("")
        print("-----------------------------------")
        print("{Você} vida:",Variaveis.vida)
        print("-----------------------------------")
        print("1- atacar")
        print("2- defender")
        print("3- usar poçao")
        print("4- tentar fugir")
        Variaveis.text = int(input('oque fazer? '))


        if Variaveis.vida <= 0:
            print("voçe foi derrotado!!!")
            input('Enter para continuar')
            Hospital.hospital()


        if Monstros_vars.vida_slime <= 0:
            print("voçe derrotou o slime!!!!")
            ganho_em_dinheiro = random.randrange(1, 1000)
            ganho_em_experiencia = random.randrange(1, 20)
            Variaveis.dinheiro += ganho_em_dinheiro
            Player.xp += 20
            if Player.xp <= 100:
                print("Voce subiu de nivel")
                Player.xp -= 100
                Player.nivel += 1
            return

        #comando de ataque
        if Variaveis.text == 1:
            miss = random.randrange(1, 100)
            miss_inimigo = random.randrange(1, 100)
            dano_inimigo = random.randrange(10, 30) + Monstros_vars.força_slime

            if miss <= 20 and miss_inimigo <= 10:
                print("voce errou")
                print("o inimigo errou")

            if miss <= 20 and miss_inimigo > 10:
                print("voce errou")
                Variaveis.vida -= dano_inimigo
                print("voce levou",dano_inimigo,"de dano")

            if miss > 20 and miss_inimigo <= 10:
                dano = random.randrange(20, 36) + Player.força
                Monstros_vars.vida_slime -= dano
                print("voce causou",dano,"pontos de dano")
                print("o inimigo errou")

            if miss > 20 and miss_inimigo > 10:
                dano = random.randrange(20, 36) + Player.força
                Monstros_vars.vida_slime -= dano
                print("voce causou",dano,"pontos de dano")
                Variaveis.vida -= dano_inimigo
                print("voce levou",dano_inimigo,"de dano")


        input('Enter para continuar')



    
if __name__ == '__main__':
     batalha()
