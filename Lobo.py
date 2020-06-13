import Monstros_vars
import Variaveis
import Player
import random
import Hospital
from Ferramentas_Diverças import limpa_tela
from colorama import init, Fore, Style

init()
 

def batalha():
    while 1:
        if Variaveis.vida <= 0:
            print("voçe foi derrotado!!!")
            input('Enter para continuar')
            Hospital.hospital()


        if Monstros_vars.vida_lobo <= 0:
            print("voçe derrotou o lobo!!!!")
            ganho_em_dinheiro = random.randrange(1, 1000)
            ganho_em_experiencia = random.randrange(1, 20)
            Variaveis.dinheiro += ganho_em_dinheiro
            Player.xp += 20
            input('Enter para continuar')
            if Player.xp >= 100:
                print("Voce subiu de nivel")
                Player.xp -= 100
                Player.nivel += 1
                input('Enter para continuar')
            return
        limpa_tela()
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(f'{Fore.RED}۩lobo۩{Fore.RESET}                 vida:',Monstros_vars.vida_lobo)
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("")
        print("")
        print("")
        print("")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(f'{Fore.GREEN}۩Você۩{Fore.RESET}                  vida:',Variaveis.vida)
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("1- atacar")
        print("2- defender")
        print("3- usar poçao")
        print("4- tentar fugir")
        Variaveis.text = int(input('oque fazer? '))

        #comando de ataque
        if Variaveis.text == 1:
            miss = random.randrange(1, 100)
            miss_inimigo = random.randrange(1, 100)
            dano_inimigo = random.randrange(0, 11) + Monstros_vars.força_lobo

            if miss <= 20 and miss_inimigo <= 10:
                print("voce errou")
                print("o inimigo errou")

            if miss <= 20 and miss_inimigo > 10:
                print("voce errou")
                Variaveis.vida -= dano_inimigo
                print("voce levou",dano_inimigo,"de dano")

            if miss > 20 and miss_inimigo <= 10:
                dano = random.randrange(Player.dano_min, Player.dano_max) + Player.força
                Monstros_vars.vida_lobo -= dano
                print("voce causou",dano,"pontos de dano")
                print("o inimigo errou")

            if miss > 20 and miss_inimigo > 10:
                dano = random.randrange(Player.dano_min, Player.dano_max) + Player.força
                Monstros_vars.vida_lobo -= dano
                print("voce causou",dano,"pontos de dano")
                Variaveis.vida -= dano_inimigo
                print("voce levou",dano_inimigo,"de dano")

        #comando de ataque
        if Variaveis.text == 2:
            dano_inimigo = random.randrange(0, 11) + Monstros_vars.força_lobo
            defesa = random.randrange(Player.defesa_min, Player.defesa_max) + Variaveis.defesa
            print("voce defendeu",defesa,"pontos mais levou",dano_inimigo,"pontos de dano")
            Variaveis.vida -= dano_inimigo - defesa

        #comando de poçôes
        if Variaveis.text == 3:
            if Variaveis.poçoes == 0:
                print("você esta sem poçoes")

            if Variaveis.poçoes >= 1:
                Variaveis.poçoes -= 1
                Variaveis.vida == Variaveis.vida_max
                print("voçe curou toda sua vida agora você tem",Variaveis.poçoes,"poções")





        input('Enter para continuar')



    
if __name__ == '__main__':
     batalha()
