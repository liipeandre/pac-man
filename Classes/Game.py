from pygame import *
from Classes.Personagens.Pacman import *
from Classes.Personagens.Blinky import *
from Classes.Personagens.Pinky import *
from Classes.Personagens.Inky import *
from Classes.Personagens.Clyde import *
from Classes.Tiles.Parede import *
from Classes.Fase import *

class Game():
    def __init__(self, tela):
        # pontuacao do jogo
        self.pontuacao = 0
        self.vidas = 2

        # variaveis de controle do jogo
        self.rodando = True
        self.clock = time.Clock()
        self.fps = 120
        self.tela = tela
        self.fase_atual = 0
        self.pontuacao = 0
        lista_fases = ["Map01", "Map02", "Map03"]
        self.fases = [Fase(nome_fase, self) for nome_fase in lista_fases]


    def tratar_eventos(self):
        ''' Trata eventos do teclado '''
        # apelido a fase atual
        fase_atual = self.fases[self.fase_atual]

        # capturo as teclas presionadas
        event.pump()
        teclas = key.get_pressed()

        # faz a movimentacao do pacman
        fase_atual.pacman.move(teclas, self)


    def atualizar_tela(self):
        ''' trata eventos visuais e sonoros (audio) '''
        # apelido a fase atual
        fase_atual = self.fases[self.fase_atual]

        # limpa a tela
        preto = (0, 0, 0)
        self.tela.fill(preto)

        # desenha a fase atual com elementos graficos (pontuacao, contador vidas, etc.)
        fase_atual.draw(self)

    def atualiza_estado_jogo(self):
        ''' atualiza estado do jogo (movimentacao da IA, logica de colisao, itens, pontuacao, etc.)'''
        # apelido a fase atual
        fase_atual = self.fases[self.fase_atual]

        

        # movimenta os fantasmas a partir da IA.
        #fase_atual.blinky.move(self)
        #fase_atual.pinky.move(self)
        #fase_atual.inky.move(self)
        #fase_atual.clyde.move(self)
        return

    def run(self):
        while self.rodando:
            # trata eventos do teclado.
            self.tratar_eventos()

            # atualiza estado do jogo.
            self.atualiza_estado_jogo()

            # escreve no buffer de tela + rotinas de jogo.
            self.atualizar_tela()

            # atualizar a tela, com os dados do buffer
            display.update()

            # atualiza os fps
            self.clock.tick(self.fps)