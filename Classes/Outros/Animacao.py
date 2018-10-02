from pygame import *
from enum import Enum

class Acao(Enum):
    Parado = 0
    AndarCima = 1
    AndarBaixo = 2
    AndarEsquerda = 3
    AndarDireita = 4

class Animacao():
    sprite_sheet = None
    def __init__(self, dimensoes_sprites : Rect):
        self.sprite_atual = 0
        self.dimensoes_sprites = dimensoes_sprites
        if self.sprite_sheet is None: self.sprite_sheet = image.load("Graphics/sprite_sheet.png")

    def draw(self, tela, pai):
            tela.blit(self.sprite_sheet, pai.posicao, self.dimensoes_sprites[self.sprite_atual])
