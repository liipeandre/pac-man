from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *
from math import pi
from numpy import subtract

class PowerPill(object):
    def __init__(self, posicao_elemento: tuple, jogo):
        # defino a pontuacao do item
        self.pontuacao = 50

        # posicoes do elemento na tela e a acao que ele esta fazendo
        self.posicao = posicao_elemento
        self.acao = Acao.Parado
        self.dimensoes = (9, 9)

    def draw(self, tela):
        # apelido dos eixos 
        x, y = 0, 1

        # desenho a animação, dado o sprite atual e as dimensoes já armazenadas.
        amarelo = (255, 163, 71)
        self.raio = 6
        draw.circle(tela, amarelo, [self.posicao[x] + 8, self.posicao[y] + 8], 6, 0)

    def bounding_box(self):
        # apelido dos eixos 
        x, y = 0, 1
        return Rect(self.posicao[x] + 8, self.posicao[y] + 8, self.dimensoes[x], self.dimensoes[y])
