from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *

class Pacman(object):
    def __init__(self, posicao_personagem: tuple, jogo):
        # posicoes do personagem na tela e a acao que ele esta fazendo
        self.posicao = posicao_personagem
        self.acao = Acao.Parado

        # carrego o sprite sheet inteiro.
        sprite_sheet = image.load("Graphics/sprite_sheet.png")

        # quebro em imagens menores (sprites do personagem, cada retangulo é um sprite, começando do zero)
        dimensoes_sprites = [Rect(3, 90, 14, 14), Rect(20, 90, 12, 14), Rect(35, 90, 9, 14),\
                             Rect(48, 90, 12, 14), Rect(63, 90, 9, 14), Rect(75, 92, 14, 12),\
                             Rect(48, 90, 12, 14), Rect(92, 95, 14, 9), Rect(109, 92, 14, 12),\
                             Rect(126, 95, 14, 9), Rect(3, 112, 16, 7), Rect(22, 113, 16, 6),\
                             Rect(41, 114, 16, 5), Rect(60, 114, 16, 5), Rect(79, 113, 16, 6),\
                             Rect(98, 113, 14, 6), Rect(115, 112, 10, 7), Rect(128, 113, 6, 6),\
                             Rect(137, 113, 2, 6), Rect(142, 109, 12, 10)]

        # armazeno a animação do personagem
        self.animacao = Animacao(dimensoes_sprites)

    def draw(self, tela):
        # desenho a animação, dado o sprite atual e as dimensoes já armazenadas.
        self.animacao.draw(tela, self)
