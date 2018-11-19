from enum import IntEnum

class estado(IntEnum):
    parado = 0
    andando = 1


class estado2(IntEnum):
    nenhum = 0
    modo_fuga = 1
    morrendo = 2
    morto = 3


class direcao(IntEnum):
    cima = 0
    baixo = 1
    esquerda = 2
    direita = 3
    indefinida = 4


class Movimento(object):
    """ Classe que mantém dados com relação a movimentação do componente."""
    def __init__(self, posicao: list):
        self.posicao = posicao
        self.estado = estado.parado
        # estado2 é usado pelos fantasmas, pois os fantasmas podem andar em 
        # estado normal e em modo fuga.
        self.estado2 = estado2.nenhum
        self.direcao_atual = direcao.cima
        self.proxima_direcao = direcao.cima
        self.velocidade = 4