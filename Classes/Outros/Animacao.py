from pygame import *
from enum import IntEnum

class Acao(IntEnum):
    Parado = 0
    AndarCima = 1
    AndarBaixo = 2
    AndarDireita = 3
    AndarEsquerda = 4
    ModoFugaouMorte = 5
    ComidoAndarCima = 6
    ComidoAndarBaixo = 7
    ComidoAndarDireita = 8
    ComidoAndarEsquerda = 9


class Animacao():
    sprite_sheet = None
    def __init__(self, dimensoes_sprites : Rect, sequencia_sprites : list):
        self.sprite_atual = 0
        self.sequencia_sprites = sequencia_sprites
        self.dimensoes_sprites = dimensoes_sprites
        if self.sprite_sheet is None: self.sprite_sheet = image.load("Graphics/sprite_sheet.png")

    def draw(self, tela, pai):
            # desenho o sprite na tela
            tela.blit(self.sprite_sheet, pai.posicao, self.dimensoes_sprites[self.sequencia_sprites[int(pai.acao)][self.sprite_atual]])
            
            # incremento o sprite atual para o proximo da lista
            if pai.acao != Acao.Parado:
                if self.sprite_atual < len(self.sequencia_sprites[int(pai.acao)]) - 1:      # se nao fim da lista.
                    self.sprite_atual += 1                                                  # incremento o sprite atual
                else: 
                    self.sprite_atual = 0       # senao, volto para o inicio da lista