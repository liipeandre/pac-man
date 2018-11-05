from enum import IntEnum

class estado(IntEnum):
    parado = 0
    andando = 1
    modo_fuga = 2
    morrendo = 3
    morto = 4
    

class direcao(IntEnum):
    cima = 0
    baixo = 1
    esquerda = 2
    direita = 3
    indefinida = 4


class Movimento(object):
    """ Classe que mantém dados com relação a movimentação do componente."""
    def __init__(self, posicao: tuple):
        self.posicao = posicao
        self.estado = estado.parado
        self.direcao_atual = direcao.cima
        self.proxima_direcao = direcao.cima
        self.velocidade = 4