from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *
from math import pi

class Orange(object):
    def __init__(self, posicao_elemento: tuple, jogo):
        # posicoes do elemento na tela e a acao que ele esta fazendo
        self.posicao = posicao_elemento
        self.acao = Acao.Parado

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
