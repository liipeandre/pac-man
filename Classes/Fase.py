from pygame import *
from Classes.Personagens.Pacman import *
from Classes.Personagens.Blinky import *
from Classes.Personagens.Pinky import *
from Classes.Personagens.Inky import *
from Classes.Personagens.Clyde import *
from Classes.Itens.PowerPill import *
from Classes.Itens.Apple import *
from Classes.Itens.Bell import *
from Classes.Itens.Chave import *
from Classes.Itens.Cherry import *
from Classes.Itens.GalaxyBoss import *
from Classes.Itens.Melon import *
from Classes.Itens.Orange import *
from Classes.Itens.Pacdot import *
from Classes.Itens.PowerPill import *
from Classes.Itens.Strawberry import *
from Classes.Tiles.Parede import *
from random import randint, shuffle, choice


class Fase():
    def __init__(self, nome_fase:str, jogo):
        # listas de elementos do jogo
        # sorteio itens
        self.num_fichas_nada = 127
        self.num_fichas_cherry = 64
        self.num_fichas_strawberry = 32
        self.num_fichas_orange = 16
        self.num_fichas_apple = 8
        self.num_fichas_melon = 4
        self.num_fichas_galaxy_boss = 2
        self.num_fichas_bell = 1

        self.fichas_sorteio = ["N"] * self.num_fichas_nada + \
                              ["C"] * self.num_fichas_cherry + \
                              ["S"] * self.num_fichas_strawberry + \
                              ["O"] * self.num_fichas_orange + \
                              ["A"] * self.num_fichas_apple + \
                              ["M"] * self.num_fichas_melon + \
                              ["G"] * self.num_fichas_galaxy_boss + \
                              ["B"] * self.num_fichas_bell

        # controle de fim de fase[
        self.fim_fase = False

        # personagens
        self.pacman = None
        self.blinky = None
        self.pinky = None
        self.inky = None
        self.clyde = None

        # itens, paredes do mapa
        self.paredes = []
        self.item = None
        self.pacdots = []
        self.powerpills = []
        self.chave = None

        # espacamento entre 2 elementos do jogo
        self.tamanho_quadro = 16
        
        # recuo do mapa a partir da lateral esquerda
        self.recuo = 0

        # carrego o mapa a partir do arquivo
        with open("Maps/" + nome_fase + ".txt", "r") as arquivo:
            mapa = arquivo.readlines()
            self.altura_mapa = len(mapa)
            self.largura_mapa = len(mapa[0])
            for i in range(len(mapa)):
                for j in range(len(mapa[i])):
                    if mapa[i][j] == 'A': 
                        self.pacman = Pacman([self.recuo + self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif mapa[i][j] == 'B': 
                        self.blinky = Blinky([self.recuo + self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif mapa[i][j] == 'C': 
                        self.pinky = Pinky([self.recuo + self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                        self.casa_fantasmas = (self.tamanho_quadro * j, self.tamanho_quadro * i)
                    elif mapa[i][j] == 'D': 
                        self.inky = Inky([self.recuo + self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif mapa[i][j] == 'E': 
                        self.clyde = Clyde([self.recuo + self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif mapa[i][j] == '1' or mapa[i][j] == 'S': 
                        self.paredes.append(Parede([self.recuo + self.tamanho_quadro * j, self.tamanho_quadro * i], jogo, self))
                    elif mapa[i][j] == 'P':
                        self.powerpills.append(PowerPill([self.recuo + self.tamanho_quadro * j, self.tamanho_quadro * i], jogo))
                    elif mapa[i][j] == ' ':
                        self.pacdots.append(Pacdot([self.recuo + self.tamanho_quadro * j, self.tamanho_quadro * i], jogo))
                    elif mapa[i][j] == 'K':
                        self.posicao_chave = (self.tamanho_quadro * j, self.tamanho_quadro * i)
                    elif mapa[i][j] == 'I':
                        self.posicao_itens = (self.tamanho_quadro * j, self.tamanho_quadro * i)

    def draw(self, jogo):
        # desenha os personagens do jogo em tela
        self.pacman.draw(jogo.tela)
        self.blinky.draw(jogo.tela)
        self.pinky.draw(jogo.tela)
        self.inky.draw(jogo.tela)
        self.clyde.draw(jogo.tela)

        # desenha as paredes da fase
        for parede in self.paredes: parede.draw(jogo.tela)

        # desenha a pontuacao
        jogo.pontuacao_e_vidas.draw(jogo.tela)

        # desenha o item
        if self.item is not None:
            self.item.draw(jogo.tela) 

        # desenha as pacdots
        for pacdot in self.pacdots: pacdot.draw(jogo.tela)

        # desenha as powerpills
        for powerpill in self.powerpills: powerpill.draw(jogo.tela)

        # desenha a chave
        if self.chave is not None:
            self.chave.draw(jogo.tela)

    def sistema_pontuacao(self, jogo):
        # computa o sistema de pontuacao
        jogo.pontuacao_e_vidas.sistema_pontuacao(jogo)


    def controle_colisao(self, jogo):
        # se pacman encostou em um dos fantasmas, verifica se eles estao em modo de fuga
        if self.pacman.bounding_box().colliderect(self.blinky.bounding_box()):
            if self.blinky.acao == Acao.ModoFugaouMorte:
                return
        return


    def gerador_itens(self):
        self.fichas_sorteio = ["N"] * self.num_fichas_nada + \
                              ["C"] * self.num_fichas_cherry + \
                              ["S"] * self.num_fichas_strawberry + \
                              ["O"] * self.num_fichas_orange + \
                              ["A"] * self.num_fichas_apple + \
                              ["M"] * self.num_fichas_melon + \
                              ["G"] * self.num_fichas_galaxy_boss + \
                              ["B"] * self.num_fichas_bell

        # embaralha e sorteia uma ficha das disponiveis
        shuffle(self.fichas_sorteio)
        item = choice(self.fichas_sorteio)

        # testo qual item foi sorteado
        if item == 'C': self.item = Cherry(self.posicao_itens)
        elif item == 'S': self.item = Strawberry(self.posicao_itens)
        elif item == 'O': self.item = Orange(self.posicao_itens)
        elif item == 'A': self.item = Apple(self.posicao_itens)
        elif item == 'M': self.item = Melon(self.posicao_itens)
        elif item == 'G': self.item = GalaxyBoss(self.posicao_itens)
        elif item == 'B': self.item = Bell(self.posicao_itens)
        elif item == 'N': self.item = None