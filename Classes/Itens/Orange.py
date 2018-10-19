from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *
from math import pi

class Orange(object):
    def __init__(self, posicao_elemento: tuple):
        # defino a pontuacao do item
        self.pontuacao = 500
        
        # posicoes do elemento na tela e a acao que ele esta fazendo
        self.posicao = posicao_elemento
        self.acao = Acao.Parado
        self.dimensoes = (12, 12)

        # carrego o sprite sheet inteiro.
        sprite_sheet = image.load("Graphics/sprite_sheet.png")

        # quebro em imagens menores (sprites do elemento, cada retangulo é um sprite, começando do zero)
        dimensoes_sprites = [Rect(321, 239, 12, 12)]

        # defino a sequencia de sprites para cada acao
        sequencia_sprites = [[0]]

        # armazeno a animação do personagem
        self.animacao = Animacao(dimensoes_sprites, sequencia_sprites)

    def draw(self, tela):
        # desenho a animação, dado o sprite atual e as dimensoes já armazenadas.
        self.animacao.draw(tela, self)

    def bounding_box(self):
        # apelido dos eixos 
        x, y = 0, 1
        return Rect(self.posicao[x], self.posicao[y], self.dimensoes[x], self.dimensoes[y])