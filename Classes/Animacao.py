from pygame import *

class Animacao():
    sprite_sheet = None
    def __init__(self, dimensoes_sprites : Rect):
        self.sprite_atual = 19
        self.dimensoes_sprites = dimensoes_sprites
        if self.sprite_sheet is None: self.sprite_sheet = image.load("Graphics/sprite_sheet.png")

    def draw(self, tela, pai):
            tela.blit(self.sprite_sheet, pai.posicao, self.dimensoes_sprites[self.sprite_atual])
