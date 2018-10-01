from Classes.Animacao import *
from pygame import *
from Classes.Game import *
from enum import Enum

class Acao(Enum):
    Parado = 0
    AndarCima = 1
    AndarBaixo = 2
    AndarEsquerda = 3
    AndarDireita = 4

class Pacman():
    def __init__(self, posicao_personagem: tuple, jogo):
        # posicoes do personagem na tela e a acao que ele esta fazendo
        self.posicao = posicao_personagem
        self.acao = Acao.Parado

        # carrego o sprite sheet inteiro.
        sprite_sheet = image.load("Graphics/sprite_sheet.png")

        # quebro em imagens menores (sprites do pacman)
        dimensoes_sprites = [Rect(3, 90, 15, 17), Rect(19, 90, 13, 17), Rect(34, 90, 13, 17),\
                             Rect(47, 90, 13, 17), Rect(62, 90, 13, 17), Rect(75, 90, 14, 17),\
                             Rect(47, 90, 13, 17), Rect(92, 90, 15, 17), Rect(109, 90, 15, 17),\
                             Rect(126, 90, 15, 17), Rect(3, 109, 17, 16), Rect(21, 109, 19, 16),\
                             Rect(40, 109, 18, 16), Rect(59, 109, 16, 16), Rect(79, 109, 16, 16),\
                             Rect(98, 109, 16, 16), Rect(115, 109, 14, 16), Rect(128, 109, 6, 16),\
                             Rect(136, 109, 6, 16), Rect(141, 109, 13, 16)]

        self.animacao = Animacao(dimensoes_sprites)

    def draw(self, tela):
        self.animacao.draw(tela, self)
