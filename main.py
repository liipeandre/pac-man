import pygame, sys
from pygame.locals import *
from Classes.Game import *

def main():
    # inicio o pygame
    pygame.init()

    # crio a janela com o nome pacman
    tamanho_tela = (1024, 768)
    tela = pygame.display.set_mode(tamanho_tela)
    pygame.display.set_caption("Pac-man!")

    # crio um objeto do tipo jogo
    jogo = Game(tela)

    # loop do jogo
    jogo.run()

    # desaloca recursos do pygame
    pygame.quit()

if __name__ == "__main__":
    main()
