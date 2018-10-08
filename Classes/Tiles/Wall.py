from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *
from math import pi
from numpy import subtract

class Wall(object):
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

    def posicao_alvo(self, objeto):
        """ Posicao de outro objeto """
        # computo a posicao pelas coordenadas do objeto.
        posicao = tuple(subtract(self.posicao, objeto.posicao))
        
        # defino o raio de busca em pixels
        raio_busca = 50

        # retorno a posicao resultante
        if posicao[0] == 0 and posicao[1] in range(0,  raio_busca):     return "cima"
        elif posicao[0] == 0 and posicao[1] in range(-raio_busca, 0):   return "baixo"
        elif posicao[0] in range(-raio_busca, 0) and posicao[1] == 0:   return "esquerda"
        elif posicao[0] in range(0,  raio_busca) and posicao[1] == 0:   return "direita"
        else: return "nao vizinho"
