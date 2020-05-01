import vars

def status():
    #Status#
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1- vida")
    print("2- defesa")
    print("3- atack")
    print("4- dinhero")
    print("5- poçoes")
    print("6- sair")
    text = int(input("oque fazer? "))
    #check vida#
    if text == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("vida:",vars.vida)
        print("1- sair")
        text = int(input("oque fazer? "))
        pass
    #check defesa#
    if text == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("defesa:",vars.defesa)
        print("1- sair")
        text = int(input("oque fazer? "))
        pass
    #check atack#
    if text == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("atack:",vars.atack)
        print("1- sair")
        text = int(input("oque fazer? "))
        pass
    #check dinhero#
    if text == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("dinhero:",vars.dinheiro)
        print("1- sair")
        text = int(input("oque fazer? "))
        pass
    #check poçoes#
    if text == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("poçoes:",vars.poçoes)
        print("1- sair")
        text = int(input("oque fazer? "))
        pass
    #sair#
    if text == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("vida:",vars.vida)
        print("1- sair")
        text = int(input("oque fazer? "))
        pass
    pass
