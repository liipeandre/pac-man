from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *
from math import pi
from numpy import subtract

class Parede(object):
    def __init__(self, posicao_elemento: tuple, jogo):
        # posicoes do elemento na tela e a acao que ele esta fazendo
        self.posicao = posicao_elemento
        self.acao = Acao.Parado
        self.dimensoes_bounding_box = (16, 16)

    def draw(self, tela):
        # desenho a animação, dado o sprite atual e as dimensoes já armazenadas.
        azul = (0, 120, 248)
        x, y = 0, 1
        draw.rect(tela, azul, [self.posicao[x], self.posicao[y], 16, 16], 1)
