from pygame import *
from Classes.Personagens.Pacman import *
from Classes.Personagens.Blinky import *
from Classes.Personagens.Pinky import *
from Classes.Personagens.Inky import *
from Classes.Personagens.Clyde import *
from Classes.Tiles.Parede import *
from Classes.Fase import *
from Classes.Outros.Pontuacao_e_Vidas import *

class Game():
    def __init__(self, tela):
        # pontuacao do jogo
        self.pontuacao_e_vidas = Pontuacao_e_Vidas((460, 200), self)

        # variaveis de controle do jogo
        self.rodando = True
        self.clock = time.Clock()
        self.fps = 120
        self.tela = tela

        # variaveis de controle da fase do jogo
        self.lista_fases = ["Map01", "Map02", "Map03"]
        self.fase_atual = Fase(choice(self.lista_fases), self)


    def tratar_eventos(self):
        ''' Trata eventos do teclado '''

        # capturo as teclas presionadas
        event.pump()
        teclas = key.get_pressed()

        # faz a movimentacao do pacman
        self.fase_atual.pacman.move(teclas, self)


    def atualizar_tela(self):
        ''' trata eventos visuais e sonoros (audio) '''
        # limpa a tela
        preto = (0, 0, 0)
        self.tela.fill(preto)

        # desenha a fase atual com elementos graficos (pontuacao, contador vidas, etc.)
        self.fase_atual.draw(self)

    def atualiza_estado_jogo(self):
        ''' atualiza estado do jogo (movimentacao da IA, logica de colisao, itens, pontuacao, etc.)'''
        # movimenta os fantasmas a partir da IA.
        #self.fase_atual.blinky.move(self)
        #self.fase_atual.pinky.move(self)
        #self.fase_atual.inky.move(self)
        #self.fase_atual.clyde.move(self)

        # sistema de itens e pontuacao
        self.fase_atual.sistema_pontuacao(self)
        return

    def run(self):
        # seta o evento de sortear item, a cada n segundos
        segundos = 10 
        sortear_item = USEREVENT + 1
        time.set_timer(sortear_item, segundos * 1000)    # x1000, pois a funcao recebe o tempo em milisegundos

        while self.rodando:
            # TODO: colocar musica de abertura

            # enquanto a fase não terminar ou as vidas do pacman não acabarem
            while not self.fase_atual.fim_fase and self.pontuacao_e_vidas.vidas != 0:

                # trata eventos de jogo
                for evento in event.get():
                    if evento.type == sortear_item:

                        # sorteia o item
                        self.fase_atual.gerador_itens()

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

            # se pacman morreu todas as vidas, acabou o jogo
            if self.pontuacao_e_vidas.vidas == 0:
                self.rodando = False

            # senão adiciona uma nova fase aleatoriamente e vai para a proxima.
            else:
                self.fase_atual = Fase(choice(self.lista_fases), self)