from pygame import *
from Classes.Personagens.Pacman import *
from Classes.Personagens.Blinky import *

class Game():
    def __init__(self, tela):
        self.tela = tela
        self.pacman = Pacman((50, 50), self)
        self.blinky = Blinky((100, 100), self)
        return

    def tratar_eventos(self):
        ''' Trata eventos do teclado '''
        return

    def atualizar_tela(self):
        ''' trata eventos visuais e sonoros (audio) '''

        # limpa a tela
        preto = (255, 255, 255)
        self.tela.fill(preto)

        # desenha elementos graficos (pontuacao, contador vidas, etc.)

        # desenha o labirinto.

        # desenha os itens.

        # desenha cada personagem em tela.
        self.pacman.draw(self.tela)
        self.blinky.draw(self.tela)

    def atualiza_estado_jogo(self):
        ''' atualiza estado do jogo (movimentacao da IA, logica de colisao, itens, pontuacao, etc.)'''
        return

    def run(self): 
        while True:
            try:
                # trata eventos do teclado.
                self.tratar_eventos()

                # atualiza estado do jogo.
                self.atualiza_estado_jogo()

                # escreve no buffer de tela + rotinas de jogo.
                self.atualizar_tela()

                # atualizar a tela, com os dados do buffer
                display.update()

                # aguarda um certo tempo para reiniciar o processo.
                time.delay(1000)
            except "FimJogo":
                break
