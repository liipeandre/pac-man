from Classes.Outros.GameComponent import *
from Classes.Outros.ElementosFase import *
from Classes.Outros.Objeto import *

class ControleFase(object, GameComponent):
    """ Realiza o controle da pontuação e das vidas. """
    def __init__(self, posicao: list):
        # cosntrutor base
        super(GameComponent, self).__init__(posicao, "Nenhum", True)

        # controle de fim de fase
        self.fim_fase = False

        # pontuacao e vidas da fase.
        self.pontuacao = 0
        self.vidas = 3

    def __init__(self, posicao: list, controle_fase: ControleFase):
        # cosntrutor base
        super(GameComponent, self).__init__(posicao, "Nenhum", True)

        # controle de fim de fase
        self.fim_fase = False

        # pontuacao e vidas da fase.
        self.pontuacao = controle_fase.pontuacao
        self.vidas = controle_fase.vidas      

    def sistema_itens_pontuacao(self, elementos_fase: ElementosFase):
        # apelido dos eixos 
        x, y = 0, 1

        # ordena os pacdots pela proximidade
        elementos_fase.pacdots.sort(key=lambda elemento: abs(elemento.posicao[x] - self.movimento.posicao[x]) +\
                                                                      abs(elemento.posicao[y] - self.movimento.posicao[y]))

        # verifica se pacman colidiu com algum objeto (itens, pacdots e powerpills)
        # se colidiu, incrementa a pontuacao e exclui o item
        # copy() serve para iterar uma cópia da lista, pois não posso iterar e alterar a própria lista
        if elementos_fase.item is not None and elementos_fase.pacman.bounding_box().colliderect(elementos_fase.item.bounding_box()):

            # incrementa pontuacao
            self.pontuacao += elementos_fase.item.pontuacao

            # exclui o item
            elementos_fase.item = None
        
        for pacdot in elementos_fase.pacdots[:5].copy():
            if elementos_fase.pacman.bounding_box().colliderect(pacdot.bounding_box()):

                # incrementa pontuacao
                self.pontuacao += pacdot.pontuacao

                # exclui a pacdot
                elementos_fase.pacdots.remove(pacdot)

        # se o pacman colidiu com uma powerpill, incrementa a pontuacao e muda o estado dos fantasmas
        for powerpill in elementos_fase.powerpills.copy():
            if elementos_fase.pacman.bounding_box().colliderect(powerpill.bounding_box()):

                # incrementa pontuacao
                self.pontuacao += powerpill.pontuacao

                # muda o estado dos fantasmas
                jogo.fase_atual.blinky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.pinky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.inky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.clyde.acao = Acao.ModoFugaouMorte

                # exclui a powerpill
                elementos_fase.powerpills.remove(powerpill)

        # se acabou os pacdots, insere a chave para passar de fase
        if not elementos_fase.pacdots and elementos_fase.chave is None:
            elementos_fase.chave = Objeto(elementos_fase.posicao_chave, "key")

        # se pacman colidir com uma chave, ele passa de fase e incrementa pontuacao
        if elementos_fase.chave is not None and elementos_fase.pacman.bounding_box().colliderect(elementos_fase.chave.bounding_box()):
            self.pontuacao += elementos_fase.chave.pontuacao
            self.fim_fase = True
            elementos_fase.chave = None