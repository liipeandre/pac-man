from pygame import *
from Classes.Personagens.Pacman import *
from Classes.Personagens.Blinky import *
from Classes.Personagens.Pinky import *
from Classes.Personagens.Inky import *
from Classes.Personagens.Clyde import *
from Classes.Tiles.Parede import *
from Classes.Fase import *
from Classes.Outros.ControleFase import *

class Game():
    def __init__(self, tela):
        # variaveis de controle do jogo
        self.rodando = True
        self.clock = time.Clock()
        self.fps = 120
        self.tela = tela

        # variaveis de controle da fase do jogo
        self.lista_fases = ["Map01", "Map02", "Map03"]
        self.fase_atual = Fase(choice(self.lista_fases))



    def run(self):
        # seta o evento de sortear item, a cada n segundos
        segundos = 10 
        sortear_item = USEREVENT + 1
        time.set_timer(sortear_item, segundos * 1000)    # x1000, pois a funcao recebe o tempo em milisegundos

        while self.rodando:
            # TODO: colocar musica de abertura

            # enquanto a fase não terminar ou as vidas do pacman não acabarem
            while not self.fase_atual.controle_fase.fim_fase and self.fase_atual.controle_fase.vidas != 0:
                
                # trata eventos de jogo
                for evento in event.get():
                    if evento.type == sortear_item:

                        # sorteia o item
                        self.fase_atual.gerador_itens()

                # trata eventos do teclado.
                self.tratar_eventos()

                # atualiza estado do jogo (movimentacao de personagens, sistema de itens e colisao).
                self.atualiza_estado_jogo()

                # escreve no buffer de tela os elementos visuais.
                self.atualizar_tela()

                # atualizar a tela, com os dados do buffer
                display.update()

                # atualiza os fps
                self.clock.tick(self.fps)

            # se acabaram as vidas do pacman, acabou o jogo
            if self.fase_atual.controle_fase.vidas == 0:
                self.rodando = False

            # senão adiciona uma nova fase aleatoriamente e vai para a proxima.
            else:
                self.fase_atual = Fase(choice(self.lista_fases), self.fase_atual.controle_fase)



    def tratar_eventos(self):
        ''' Trata eventos do jogo'''
        for evento in event.get():

            # sorteia o item, se evento acontecer
            if evento.type == sortear_item: 
                self.fase_atual.gerador_itens.sortear(self.fase_atual.elementos_fase)



    def atualizar_tela(self):
        ''' trata eventos visuais e sonoros (audio) '''
        # limpa a tela
        preto = (0, 0, 0)
        self.tela.fill(preto)

        # desenha a fase atual com elementos graficos (pontuacao, contador vidas, etc.)
        self.fase_atual.draw(self.tela)



    def atualiza_estado_jogo(self):
        ''' atualiza estado do jogo (movimentacao da IA, logica de colisao, itens, pontuacao, etc.)'''
        # movimenta os personagens e os fantasmas.
        self.fase_atual.pacman.move(self.fase_atual.elementos_fase)
        self.fase_atual.blinky.move(self.fase_atual.elementos_fase)
        self.fase_atual.pinky.move(self.fase_atual.elementos_fase)
        self.fase_atual.inky.move(self.fase_atual.elementos_fase)
        self.fase_atual.clyde.move(self.fase_atual.elementos_fase)

        # sistema de colisao com itens e pontuacao
        self.fase_atual.controle_fase.sistema_itens_pontuacao(self.fase_atual.elementos_fase)

        # TODO: deteccao de colisao de pacman com fantasmas