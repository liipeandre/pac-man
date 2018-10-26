from Classes.Outros.GameComponent import *
from Classes.Outros.ElementosFase import *
from pygame import *
from numpy import subtract



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
            jogo.pontuacao_e_vidas.pontuacao += jogo.fase_atual.item.pontuacao

            # exclui o item
            jogo.fase_atual.item = None
        
        for pacdot in jogo.fase_atual.pacdots[:5].copy():
            if jogo.fase_atual.pacman.bounding_box().colliderect(pacdot.bounding_box()):

                # incrementa pontuacao
                jogo.pontuacao_e_vidas.pontuacao += pacdot.pontuacao

                # exclui a pacdot
                jogo.fase_atual.pacdots.remove(pacdot)

        # se o pacman colidiu com uma powerpill, incrementa a pontuacao e muda o estado dos fantasmas
        for powerpill in jogo.fase_atual.powerpills.copy():
            if jogo.fase_atual.pacman.bounding_box().colliderect(powerpill.bounding_box()):

                # incrementa pontuacao
                jogo.pontuacao_e_vidas.pontuacao += powerpill.pontuacao

                # muda o estado dos fantasmas
                jogo.fase_atual.blinky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.pinky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.inky.acao = Acao.ModoFugaouMorte
                jogo.fase_atual.clyde.acao = Acao.ModoFugaouMorte

                # exclui a powerpill
                jogo.fase_atual.powerpills.remove(powerpill)

        # se acabou os pacdots, insere a chave para passar de fase
        if not jogo.fase_atual.pacdots and jogo.fase_atual.chave is None:
            jogo.fase_atual.chave = Chave(jogo.fase_atual.posicao_chave)

        # se pacman colidir com uma chave, ele passa de fase e incrementa pontuacao
        if jogo.fase_atual.chave is not None and jogo.fase_atual.pacman.bounding_box().colliderect(jogo.fase_atual.chave.bounding_box()):
            jogo.pontuacao_e_vidas.pontuacao += jogo.fase_atual.chave.pontuacao
            jogo.fase_atual.fim_fase = True
            jogo.fase_atual.chave = None