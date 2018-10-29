from Libraries import Rect
from Classes.Outros.GameComponent import GameComponent
from Classes.Outros.Movimento import *
from Classes.Outros.Sprite import Sprite

class Inky(GameComponent):
    """inimigo do jogo, controlado pela IA."""
    def __init__(self, posicao: list):
        # construtor base
        super().__init__(posicao, "Inky.bmp")

    def bounding_box(self):
        return Rect(self.movimento.posicao, self.sprite.sprite_size)

    def move(self, elementos_fase):
        return