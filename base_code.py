import os
import Status
import vars


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
text = int(input("oque fazer? "))
#Começo do Jogo#
if text == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("você acorda em um quarto com uma espada um arco uma armadura e um escudo")
    print("0- status")
    print("1- pegar espada")
    print("2- pegar arco")
    print("3- pegar armadura")
    print("4- pegar escudo")
    print("5- procurar outras coisas")
    print("6- sair do quarto")
    text = int(input("oque fazer? "))

    #Status#
    if text == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        Status.status()
        pass

    #Pegou Espada#
    elif text == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("voce pegou a espada")
        vars.itens += ("espada")
        vars.itens_pegos += 1
        vars.atack += 10
        pass

    #Pegou Arco#
    elif text == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("voce pegou o arco")
        vars.itens += ("arco")
        vars.itens_pegos += 1
        vars.atack_longa_distancia += 10
        pass
    #Pegou Armadura#
    elif text == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("voce pegou o armadura")
        vars.itens += ("armadura")
        vars.itens_pegos += 1
        vars.defesa += 10
        pass

    #Pegou Escudo#
    elif text == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("voce pegou o escudo")
        vars.itens += ("escudo")
        vars.itens_pegos += 1
        vars.defesa += 10
        pass

    #Procurar Outras Coisas#
    elif text == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("você achou um bau pareçe estar destrancado")
        print("1- abrir")
        print("2- deixar pra lá")
        pass

    #Sair do Quarto#
    elif text == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("você quer sair sem pegar nada?")
        pass
    pass
else:
    pass