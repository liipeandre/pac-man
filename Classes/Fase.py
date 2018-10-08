from pygame import *
from Classes.Personagens.Pacman import *
from Classes.Personagens.Blinky import *
from Classes.Personagens.Pinky import *
from Classes.Personagens.Inky import *
from Classes.Personagens.Clyde import *
from Classes.Tiles.Wall import *

class Fase():
    def __init__(self, nome_fase:str, jogo):
        self.pacman = None
        self.blinky = None
        self.pinky = None
        self.inky = None
        self.clyde = None
        self.paredes = []
        self.lista_itens = []

        with open("Maps/" + nome_fase + ".txt", "r") as arquivo:
            self.mapa = arquivo.readlines()
            for i in range(len(self.mapa)):
                for j in range(len(self.mapa[i])):
                    if self.mapa[i][j] == 'A': 
                        self.pacman = Pacman([16 * j, 16 * i], jogo)
                    elif self.mapa[i][j] == 'B': 
                        self.blinky = Blinky([16 * j, 16 * i], jogo)
                    elif self.mapa[i][j] == 'C': 
                        self.pinky = Pinky([16 * j, 16 * i], jogo)
                    elif self.mapa[i][j] == 'D': 
                        self.inky = Inky([16 * j, 16 * i], jogo)
                    elif self.mapa[i][j] == 'E': 
                        self.clyde = Clyde([16 * j, 16 * i], jogo)
                    elif self.mapa[i][j] == '1': 
                        self.paredes.append(Parede([16 * j, 16 * i], jogo))


    def draw(self, jogo):
        self.pacman.draw(jogo.tela)
        self.blinky.draw(jogo.tela)
        self.pinky.draw(jogo.tela)
        self.inky.draw(jogo.tela)
        self.clyde.draw(jogo.tela)
        for parede in self.paredes: parede.draw(jogo.tela)