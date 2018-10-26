from Classes.Outros.GameComponent import *

class Pinky(object, GameComponent):
    """inimigo do jogo, controlado pela IA."""
    def __init__(self, posicao: list):
        # construtor base
        super(Componente, self).__init__(posicao, "Pinky.bmp")

    def bounding_box(self):
        return Rect(self.movimento.posicao, self.sprite.sprite_size)

    def move(self):
        return