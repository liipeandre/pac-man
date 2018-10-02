from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *

class Clyde(object):
    def __init__(self, posicao_personagem: tuple, jogo):
        # posicoes do personagem na tela e a acao que ele esta fazendo
        self.posicao = posicao_personagem
        self.acao = Acao.Parado

        # carrego o sprite sheet inteiro.
        sprite_sheet = image.load("Graphics/sprite_sheet.png")

        # quebro em imagens menores (sprites do personagens, cada retangulo é um sprite, começando do zero)
        dimensoes_sprites = [Rect(3, 179, 14, 13), Rect(20, 179, 14, 13), Rect(37, 179, 14, 13),\
                             Rect(54, 179, 14, 13), Rect(71, 179, 14, 13), Rect(88, 179, 14, 13),\
                             Rect(105, 179, 14, 13), Rect(122, 179, 14, 13), Rect(3, 198, 14, 13),\
                             Rect(20, 198, 14, 13), Rect(37, 198, 14, 13), Rect(54, 198, 14, 13)]

        # armazeno a animação do personagem
        self.animacao = Animacao(dimensoes_sprites)

    def draw(self, tela):
        # desenho a animação, dado o sprite atual e as dimensoes já armazenadas.
        self.animacao.draw(tela, self)

