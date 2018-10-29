from Libraries import *
from Classes.Game import Game

def main():
    # inicio o pygame
    init()

    # posiciono a tela no centro
    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300, 80)

    # crio a janela com o nome pacman
    tamanho_tela = (730, 434)
    tela = display.set_mode(tamanho_tela)
    display.set_caption("Pac-man!")

    # crio um objeto do tipo jogo
    jogo = Game(tela)

    # loop do jogo
    jogo.run()

    # desaloca recursos do pygame
    quit()

if __name__ == "__main__":
    main()
