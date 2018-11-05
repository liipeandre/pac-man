from Classes.Outros.ControleFase import ControleFase
from Classes.Outros.ElementosFase import ElementosFase
from Classes.Outros.GeradorItens import GeradorItens
from Classes.Outros.MapLoader import MapLoader
from Classes.Outros.Sound import Sons

class Fase():
    def __init__(self, nome_fase:str, controle_fase=None):
        if controle_fase is None:
            # dados de controle da fase
            self.controle_fase = ControleFase([460, 200])
            self.elementos_fase = ElementosFase()
            self.carregador_mapa = MapLoader(nome_fase, self.elementos_fase)
            self.gerador_itens = GeradorItens()
            self.sons = Sons()

        else:
            # dados de controle da fase
            self.elementos_fase = ControleFase([460, 200], controle_fase)
            self.elementos_fase = ElementosFase()
            self.carregador_mapa = MapLoader(nome_fase, self.elementos_fase)
            self.gerador_itens = GeradorItens()

    def draw(self, tela):
        # atualiza a animacao
        self.controle_fase.atualiza_sprite_frame(self.elementos_fase.pacman.sprite)
        self.controle_fase.atualiza_sprite_frame(self.elementos_fase.blinky.sprite)
        self.controle_fase.atualiza_sprite_frame(self.elementos_fase.pinky.sprite)
        self.controle_fase.atualiza_sprite_frame(self.elementos_fase.inky.sprite)
        self.controle_fase.atualiza_sprite_frame(self.elementos_fase.clyde.sprite)

        # desenha as paredes da fase
        for parede in self.elementos_fase.paredes: parede.sprite.draw(tela)

        # desenha a pontuacao
        self.controle_fase.sprite.draw(tela)

        # desenha o item
        if self.elementos_fase.item is not None: self.elementos_fase.item.sprite.draw(tela) 

        # desenha as pacdots
        for pacdot in self.elementos_fase.pacdots: pacdot.sprite.draw(tela)

        # desenha as powerpills
        for powerpill in self.elementos_fase.powerpills: powerpill.sprite.draw(tela)

        # desenha a chave
        if self.elementos_fase.chave is not None: self.elementos_fase.chave.sprite.draw(tela)

        # desenha os personagens do jogo em tela
        self.elementos_fase.blinky.sprite.draw(tela)
        self.elementos_fase.pinky.sprite.draw(tela)
        self.elementos_fase.inky.sprite.draw(tela)
        self.elementos_fase.clyde.sprite.draw(tela)
        self.elementos_fase.pacman.sprite.draw(tela)