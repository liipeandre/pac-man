from Libraries import *
from Classes.Fase import *
from Classes.Outros.Movimento import estado2

class Game():
    def __init__(self, tela):
        # variaveis de controle do jogo
        self.rodando = True
        self.clock = time.Clock()
        self.fps = 30
        self.tela = tela
        
        # variaveis de controle da fase do jogo
        self.lista_fases = ["Map01", "Map02", "Map03"]
        self.fase_atual = Fase(choice(self.lista_fases), jogo=self)


    def run(self):
        # seta o evento de sortear item, a cada n segundos
        sortear_item = USEREVENT + 1
        time.set_timer(sortear_item, 10 * 1000)    # x1000 (milisegundos)
                                                   # x10 (intervalo de sorteio de cada item) 

        while self.rodando:
            # enquanto pacman nao morrer todas as vidas
            fase_nova = True
            while self.fase_atual.controle_fase.vidas > 0:

                # enquanto a fase não terminar ou pacman nao morrer
                while not self.fase_atual.controle_fase.fim_fase and self.fase_atual.elementos_fase.pacman.movimento.estado2 != estado2.morto:

                    # escreve no buffer de tela os elementos visuais.
                    self.atualizar_tela()

                    # atualizar a tela, com os dados do buffer
                    display.update()

                    # se for uma fase nova, toca a música de abertura e espera alguns segundos
                    if fase_nova:
                        indice = self.fase_atual.controle_audio.nome_arquivos_audio.index("pacman_beginning.ogg")
                        self.fase_atual.controle_audio.sons[indice].play()
                        time.wait(4500)
                        fase_nova = False

                    # trata eventos do teclado.
                    self.tratar_eventos()

                    # atualiza estado do jogo (movimentacao de personagens, sistema de itens e colisao).
                    self.atualiza_estado_jogo()

                    # atualiza contador do jogo
                    self.clock.tick_busy_loop(self.fps)

                # se nao acabou a fase, pacman morreu, entao reseta a posicao dos personagens 
                if not self.fase_atual.controle_fase.fim_fase:
                    self.fase_atual.controle_fase.resetar_posicoes_personagens(self.fase_atual.elementos_fase)

            # se acabaram as vidas do pacman, acabou o jogo
            if self.fase_atual.controle_fase.vidas == 0:
                self.rodando = False

            # senão adiciona uma nova fase aleatoriamente e vai para a proxima.
            else:
                self.fase_atual = Fase(choice(self.lista_fases), self.fase_atual.elementos_fase, jogo=self)



    def tratar_eventos(self):
        ''' Trata eventos do jogo'''
        sortear_item = USEREVENT + 1
        mudar_fantasmas_normal = USEREVENT + 2

        for evento in event.get():
            # sorteia o item, se evento acontecer
            if evento.type == sortear_item:
                self.fase_atual.gerador_itens.sortear(self.fase_atual.elementos_fase)

            # se fantasmas estão em modo fuga, voltam ao normal.
            if evento.type == mudar_fantasmas_normal:
                if self.fase_atual.elementos_fase.blinky.movimento.estado2 == estado2.modo_fuga:
                   self.fase_atual.elementos_fase.blinky.movimento.estado2 = estado2.nenhum

                if self.fase_atual.elementos_fase.pinky.movimento.estado2 == estado2.modo_fuga:
                   self.fase_atual.elementos_fase.pinky.movimento.estado2 = estado2.nenhum

                if self.fase_atual.elementos_fase.inky.movimento.estado2 == estado2.modo_fuga:
                   self.fase_atual.elementos_fase.inky.movimento.estado2 = estado2.nenhum

                if self.fase_atual.elementos_fase.clyde.movimento.estado2 == estado2.modo_fuga:
                   self.fase_atual.elementos_fase.clyde.movimento.estado2 = estado2.nenhum

                # desabilita o timer 
                time.set_timer(mudar_fantasmas_normal, 0 * 1000)

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
        self.fase_atual.elementos_fase.pacman.move(self.fase_atual.elementos_fase)
        self.fase_atual.elementos_fase.blinky.move(self.fase_atual.elementos_fase)
        self.fase_atual.elementos_fase.pinky.move(self.fase_atual.elementos_fase)
        self.fase_atual.elementos_fase.inky.move(self.fase_atual.elementos_fase)
        self.fase_atual.elementos_fase.clyde.move(self.fase_atual.elementos_fase)

        # sistema de colisao com itens e pontuacao
        self.fase_atual.controle_fase.sistema_itens_pontuacao(self.fase_atual.elementos_fase)

        # sistema de colisao de pacman com fantasmas
        self.fase_atual.controle_fase.sistema_colisao_fantasmas(self.fase_atual.elementos_fase)