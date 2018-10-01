from pygame import *
from Classes.Pacman import *

class Game():
    def __init__(self, tela):
        self.pacman = Pacman((50, 50), self)
        return

    def update_game(self, tela):
        ''' Imprime os elementos em tela '''
        # limpa a tela
        preto = (0, 0, 0)
        tela.fill(preto)

        self.pacman.draw(tela)
        #if self.pacman.animacao.sprite_atual < len(self.pacman.animacao.dimensoes_sprites) - 1:
        #    self.pacman.animacao.sprite_atual += 1
        #else: self.pacman.animacao.sprite_atual = 0
        time.delay(1000)

    def handle_events(self):
        ''' Trata eventos do teclado '''
        return

    def run(self, tela):
        while True:
            # trata eventos do teclado + rotinas de jogo
            #self.handle_events()

            # escreve no buffer de tela
            self.update_game(tela)

            # atualizar a tela, com os dados do buffer
            display.update()
