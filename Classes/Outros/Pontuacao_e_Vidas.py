from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *
from math import pi
from numpy import subtract

class Pontuacao_e_Vidas(object):
    def __init__(self, posicao_elemento: tuple, jogo):
        # posicoes do elemento na tela e a acao que ele esta fazendo
        self.pontuacao = 0
        self.vidas = 3
        self.posicao = posicao_elemento
        self.acao = Acao.Parado

    def draw(self, tela):
        # apelido dos eixos 
        x, y = 0, 1

        # defino a fonte e o tamanho da fonte
        cor = (255, 255, 255)
        antialiasing = True
        gerador_texto = font.SysFont('Comic Sans MS', 18)

        # renderizo os textos em tela
        texto1 = gerador_texto.render("Pontuação: " + str(self.pontuacao), antialiasing, cor)
        texto2 = gerador_texto.render("Vidas: " + str(self.vidas), antialiasing, cor)

        # desenho o texto na tela
        tela.blit(texto1, [self.posicao[x], self.posicao[y], 30, 30])
        tela.blit(texto2, [self.posicao[x], self.posicao[y] + 30, 30, 30])

    def sistema_pontuacao(self, jogo):
        # apelido dos eixos 
        x, y = 0, 1

        # ordena os pacdots pela proximidade
        jogo.fase_atual.pacdots.sort(key=lambda elemento: abs(elemento.posicao[x] - jogo.fase_atual.pacman.posicao[x]) +\
                                                                      abs(elemento.posicao[y] - jogo.fase_atual.pacman.posicao[y]))

        # verifica se pacman colidiu com algum item (itens, pacdots e powerpills)
        # se colidiu, incrementa a pontuacao e exclui o item
        # copy() serve para iterar uma cópia da lista, pois não posso iterar e alterar a própria lista
        # testa se houve colisao com os itens, pacdots e outro elementos do jogo
        if jogo.fase_atual.item is not None and jogo.fase_atual.pacman.bounding_box().colliderect(jogo.fase_atual.item.bounding_box()):

            # incrementa pontuacao
            jogo.pontuacao_e_vidas.pontuacao += jogo.fase_atual.item.pontuacao

            # exclui o item
            jogo.fase_atual.item = None
        
        for pacdot in jogo.fase_atual.pacdots[:5].copy():
            if jogo.fase_atual.pacman.bounding_box().colliderect(pacdot.bounding_box()):

                # incrementa pontuacao
                jogo.pontuacao_e_vidas.pontuacao += pacdot.pontuacao

                # exclui a pacdot
                jogo.fase_atual.pacdots.remove(pacdot)

        # se o pacman colidiu com uma powerpill, incrementa a pontuacao e muda o estado dos fantasmas
        for powerpill in jogo.fase_atual.powerpills.copy():
            if jogo.fase_atual.pacman.bounding_box().colliderect(powerpill.bounding_box()):

                # incrementa pontuacao
                jogo.pontuacao_e_vidas.pontuacao += powerpill.pontuacao

                # muda o estado dos fantasmas
                jogo.fase_atual.blinky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.pinky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.inky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.clyde.acao = Acao.ModoFugaouMorte

                # exclui a powerpill
                jogo.fase_atual.powerpills.remove(powerpill)

        # se acabou os pacdots, insere a chave para passar de fase
        if not jogo.fase_atual.pacdots and jogo.fase_atual.chave is None:
            jogo.fase_atual.chave = Chave(jogo.fase_atual.posicao_chave)

        # se pacman colidir com uma chave, ele passa de fase e incrementa pontuacao
        if jogo.fase_atual.chave is not None and jogo.fase_atual.pacman.bounding_box().colliderect(jogo.fase_atual.chave.bounding_box()):
            jogo.pontuacao_e_vidas.pontuacao += jogo.fase_atual.chave.pontuacao
            jogo.fase_atual.fim_fase = True
            jogo.fase_atual.chave = None