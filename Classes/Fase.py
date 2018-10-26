from pygame import *
from Classes.Outros.ElementosFase import *
from Classes.Outros.ControleFase import *
from Classes.Outros.MapLoader import *
from Classes.Outros.GeradorItens import *

class Fase():
    def __init__(self, nome_fase:str):
        # dados de controle da fase
        self.controle_fase = ControleFase([460, 200])
        self.elementos_fase = ElementosFase()
        self.carregador_mapa = MapLoader(nome_fase, self.elementos_fase)
        self.gerador_itens = GeradorItens()

    def __init__(self, nome_fase:str, controle_fase: ControleFase):
        # dados de controle da fase
        self.controle_fase = ControleFase([460, 200], controle_fase)
        self.elementos_fase = ElementosFase()
        self.carregador_mapa = MapLoader(nome_fase, self.elementos_fase)
        self.gerador_itens = GeradorItens()

    def draw(self, tela):
        # desenha os personagens do jogo em tela
        self.pacman.sprite.draw(tela)
        self.blinky.sprite.draw(tela)
        self.pinky.sprite.draw(tela)
        self.inky.sprite.draw(tela)
        self.clyde.sprite.draw(tela)

        # desenha as paredes da fase
        for parede in self.paredes: parede.sprite.draw(tela)

        # desenha a pontuacao
        jogo.pontuacao_e_vidas.draw(tela)

        # desenha o item
        if self.item is not None: self.item.sprite.draw(tela) 

        # desenha as pacdots
        for pacdot in self.pacdots: pacdot.sprite.draw(tela)

        # desenha as powerpills
        for powerpill in self.powerpills: powerpill.sprite.draw(tela)

        # desenha a chave
        if self.chave is not None: self.chave.sprite.draw(tela)