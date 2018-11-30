from Libraries import shuffle, choice
from Classes.Outros.Objeto import Objeto

class GeradorItens(object):
    """ Sorteia itens que aparecerão de tempos em tempos. """

    def __init__(self):
        # defino a quantidade e tipo de fichas de itens
        self.num_fichas  = [2048, 64, 32, 16, 8, 4, 2, 1]
        self.tipo_fichas = ["nenhum", "cherry", "strawberry", "orange", "apple", "melon", "galaxy boss", "bell"]


    def sortear(self, elementos_fase):
        # crio uma lista de fichas
        fichas = []
        for num_fichas, tipo_ficha in zip(self.num_fichas, self.tipo_fichas):
            fichas += [tipo_ficha] * num_fichas

        # embaralha e sorteia uma ficha
        shuffle(fichas)
        tipo_item = choice(fichas)

        # crio o item sorteado
        if elementos_fase.item is not None and tipo_item != "nenhum" and elementos_fase.item.tipo_item != "key": elementos_fase.item = Objeto(elementos_fase.posicao_itens, tipo_item)