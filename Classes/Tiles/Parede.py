from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *
from math import pi
from numpy import subtract

class Parede(object):
    def __init__(self, posicao_elemento: tuple, jogo, fase):
        # posicoes do elemento na tela e a acao que ele esta fazendo
        self.posicao = posicao_elemento
        self.acao = Acao.Parado

        # tamanho de cada quadro (dimensoes da parede)
        self.tamanho_quadro = fase.tamanho_quadro

        # a dimensao da bounding box é igual ao tamanho do quadro da fase
        self.dimensoes_bounding_box = (self.tamanho_quadro, self.tamanho_quadro)

    def draw(self, tela):
        # desenho a animação, dado o sprite atual e as dimensoes já armazenadas.
        azul = (0, 120, 248)
        x, y = 0, 1
        draw.rect(tela, azul, [self.posicao[x], self.posicao[y], self.tamanho_quadro, self.tamanho_quadro], 1)

    def bounding_box(self):
        # apelido dos eixos 
        x, y = 0, 1
        return Rect(self.posicao[x], self.posicao[y], self.dimensoes_bounding_box[x], self.dimensoes_bounding_box[y])