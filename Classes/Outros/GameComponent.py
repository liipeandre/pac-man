from Classes.Outros.Sprite import *
from Classes.Outros.Movimento import *

class GameComponent(object):
    """ GameComponente é uma classe base de elementos genéricos (itens, personagens, inimigos, etc.). Possui 2 construtores.
        
        - Para objetos móveis: recebe o sprite sheet e a posicao onde deverá ser desenhado.
        - Para objetos fixos: recebe em adição ao anterior, o sprite_frame de animação (fixo).

        Em ambos, o construtor recebe um booleano (desenha pontuacao), para desenhar a pontuacao e as vidas em tela, quando indicado, no lugar do sprite.
    """
    def __init__(self, posicao: list, sprite_sheet_file: str):
        self.sprite = Sprite(self, sprite_sheet_file)
        self.movimento = Movimento(posicao)

    def __init__(self, posicao: list, sprite_sheet_file: str, sprite_frame):
        self.sprite = Sprite(self, sprite_sheet_file, sprite_frame)
        self.movimento = Movimento(posicao)

    def __init__(self, posicao: list, sprite_sheet_file: str, desenha_pontuacao=False):
        self.sprite = Sprite(self, sprite_sheet_file, desenha_pontuacao)
        self.movimento = Movimento(posicao)

    def bounding_box(self):
        # apelido dos eixos 
        x, y = 0, 1

        # retorno a bounding box
        return Rect(self.movimento.posicao[x], self.movimento.posicao[y], self.sprite.sprite_size[x], self.sprite.sprite_size[y])