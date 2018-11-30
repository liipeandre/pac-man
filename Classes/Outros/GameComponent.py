from Libraries import Rect
from Classes.Outros.Sprite import *
from Classes.Outros.Movimento import *

class GameComponent(object):
    """ GameComponente é uma classe base de elementos genéricos (itens, personagens, inimigos, etc.). Possui 2 construtores.
        
        - Para objetos móveis: recebe o sprite sheet e a posicao onde deverá ser desenhado.
        - Para objetos fixos: recebe em adição ao anterior, o sprite_frame de animação (fixo).

        Em ambos, o construtor recebe um booleano (desenha pontuacao), para desenhar a pontuacao e as vidas em tela, quando indicado, no lugar do sprite.
    """
    def __init__(self, posicao: list, sprite_sheet_file: str, sprite_frame=None, desenha_pontuacao=False):
        self.sprite = Sprite(self, sprite_sheet_file, sprite_frame, desenha_pontuacao)
        self.movimento = Movimento(posicao)

    def bounding_box(self):
        # apelido dos eixos 
        x, y = 0, 1

        # retorno a bounding box
        return Rect(self.movimento.posicao[x], self.movimento.posicao[y], self.sprite.sprite_size[x], self.sprite.sprite_size[y])


    def resetar(self, posicao):
        self.movimento.posicao = posicao.copy()
        self.movimento.estado = estado.parado
        self.movimento.estado2 = estado2.vivo
        self.movimento.direcao_atual = direcao.cima
        self.movimento.proxima_direcao = direcao.cima
        self.sprite.sprite_frame = [0, 0]