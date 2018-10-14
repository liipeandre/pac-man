from pygame import *
from Classes.Personagens.Pacman import *
from Classes.Personagens.Blinky import *
from Classes.Personagens.Pinky import *
from Classes.Personagens.Inky import *
from Classes.Personagens.Clyde import *
from Classes.Tiles.Parede import *

class Fase():
    def __init__(self, nome_fase:str, jogo):
        # listas de elementos do jogo
        # pontuacao da fase
        self.pontuacao_fase = 0

        # personagens
        self.pacman = None
        self.blinky = None
        self.pinky = None
        self.inky = None
        self.clyde = None

        # itens, paredes do mapa
        self.paredes = []
        self.lista_itens = []
        
        # espacamento entre 2 elementos do jogo
        self.tamanho_quadro = 16

        # carrego o mapa a partir do arquivo
        with open("Maps/" + nome_fase + ".txt", "r") as arquivo:
            self.mapa = arquivo.readlines()
            for i in range(len(self.mapa)):
                for j in range(len(self.mapa[i])):
                    if self.mapa[i][j] == 'A': 
                        self.pacman = Pacman([self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif self.mapa[i][j] == 'B': 
                        self.blinky = Blinky([self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif self.mapa[i][j] == 'C': 
                        self.pinky = Pinky([self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif self.mapa[i][j] == 'D': 
                        self.inky = Inky([self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif self.mapa[i][j] == 'E': 
                        self.clyde = Clyde([self.tamanho_quadro * j, self.tamanho_quadro * i], jogo)
                    elif self.mapa[i][j] == '1': 
                        self.paredes.append(Parede([self.tamanho_quadro * j, self.tamanho_quadro * i], jogo, self))
                    elif self.mapa[i][j] == ' ':
                        j += 2


    def draw(self, jogo):
        # desenha os elementos do jogo em tela
        self.pacman.draw(jogo.tela)
        self.blinky.draw(jogo.tela)
        self.pinky.draw(jogo.tela)
        self.inky.draw(jogo.tela)
        self.clyde.draw(jogo.tela)
        for parede in self.paredes: parede.draw(jogo.tela)


    def sistema_pontuacao(self):
        # verifica se pacman colidiu com algum item
        for item in self.lista_itens:
            if self.pacman.colisao(item):
                self.pontuacao += self.item.pontuacao 

    def controle_colisao(self):
        # se pacman encostar em um dos fantasmas, verifica se eles estao em modo de fuga            
        