import os

CLEAR = 'cls' if os.name == 'nt' else 'clear' 
limpa_tela = lambda : os.system(CLEAR)