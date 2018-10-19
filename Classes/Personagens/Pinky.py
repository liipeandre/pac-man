from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *

class Pinky(object):
    def __init__(self, posicao_personagem: tuple, jogo):
        # defino a pontuacao do item
        self.pontuacao = 5000

        # posicoes do personagem na tela e a acao que ele esta fazendo
        self.posicao = posicao_personagem
        self.acao = Acao.Parado
        self.velocidade = 0.5

        # carrego o sprite sheet inteiro.
        sprite_sheet = image.load("Graphics/sprite_sheet.png")

        # quebro em imagens menores (sprites do personagens, cada retangulo � um sprite, come�ando do zero)
        dimensoes_sprites = [Rect(3, 144, 14, 13), Rect(20, 144, 14, 13), Rect(37, 144, 14, 13),\
                             Rect(54, 144, 14, 13), Rect(71, 144, 14, 13), Rect(88, 144, 14, 13),\
                             Rect(105, 144, 14, 13), Rect(122, 144, 14, 13), Rect(3, 198, 14, 13),\
                             Rect(20, 198, 14, 13), Rect(37, 198, 14, 13), Rect(54, 198, 14, 13),\
                             Rect(71, 203, 11, 4), Rect(88, 203, 11, 4), Rect(105, 202, 10, 5),\
                             Rect(122, 202, 10, 5)]

        # defino a sequencia de sprites para cada acao
        sequencia_sprites = [[0],\
                             [4, 5],\
                             [6, 7],\
                             [0, 1],\
                             [2, 3],\
                             [8, 10, 9, 11],\
                             [14],\
                             [15],\
                             [12],\
                             [13]]

        # armazeno a animacao do personagem
        self.animacao = Animacao(dimensoes_sprites, sequencia_sprites)

    def draw(self, tela):
        # desenho a anima��o, dado o sprite atual e as dimensoes j� armazenadas.
        self.animacao.draw(tela, self)

    def bounding_box(self):
        # apelido dos eixos 
        x, y = 0, 1
        return Rect(self.posicao[x], self.posicao[y], self.dimensoes_bounding_box[x], self.dimensoes_bounding_box[y])

    def move(self, teclas):
        # verifico as teclas de movimentacao do pinky
        '''if teclas[K_UP]:
            self.posicao[1] -= self.velocidade
            self.acao = Acao.AndarCima

        elif teclas[K_DOWN]:
            self.posicao[1] += self.velocidade
            self.acao = Acao.AndarBaixo

        elif teclas[K_LEFT]:
            self.posicao[0] -= self.velocidade
            self.acao = Acao.AndarEsquerda

        elif teclas[K_RIGHT]:
            self.posicao[0] += self.velocidade
            self.acao = Acao.AndarDireita

        else:
            if   int(self.acao) == int(Acao.AndarCima):     self.posicao[1] -= self.velocidade
            elif int(self.acao) == int(Acao.AndarBaixo):    self.posicao[1] += self.velocidade
            elif int(self.acao) == int(Acao.AndarEsquerda): self.posicao[0] -= self.velocidade
            elif int(self.acao) == int(Acao.AndarDireita):  self.posicao[0] += self.velocidade'''