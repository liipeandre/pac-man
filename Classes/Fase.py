from Classes.Outros.ControleFase import ControleFase
from Classes.Outros.ElementosFase import ElementosFase
from Classes.Outros.GeradorItens import GeradorItens
from Classes.Outros.MapLoader import MapLoader
from Classes.Outros.ControleAudio import ControleAudio

class Fase():
    def __init__(self, nome_fase:str, controle_fase=None, jogo=None):
        if controle_fase is None:
            # dados de controle da fase
            self.jogo = jogo
            self.controle_fase = ControleFase([460, 200], fase_atual=self)
            self.elementos_fase = ElementosFase(fase_atual=self)
            self.carregador_mapa = MapLoader(nome_fase, self.elementos_fase)
            self.gerador_itens = GeradorItens()
            self.controle_audio = ControleAudio()

        else:
            # dados de controle da fase
            self.jogo = jogo
            self.elementos_fase = ControleFase([460, 200], controle_fase)
            self.elementos_fase = ElementosFase()
            self.carregador_mapa = MapLoader(nome_fase, self.elementos_fase)
            self.gerador_itens = GeradorItens()
            self.controle_audio = ControleAudio()

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