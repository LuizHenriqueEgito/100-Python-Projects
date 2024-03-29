from src.menu_principal import MenuInicial
from src.game import game

def run_aplication():
    menu_inicial = MenuInicial(window_size=(850,500), window_color=(10,10,10), set_display='SnakeGame')
    jogar = menu_inicial.run()
    if jogar:
        game()
    else:
        print('saindo ...')