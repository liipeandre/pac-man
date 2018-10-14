from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *

class Blinky(object):
    def __init__(self, posicao_personagem: tuple, jogo):
        # posicoes do personagem na tela e a acao que ele esta fazendo
        self.posicao = posicao_personagem
        self.acao = Acao.Parado
        self.proxima_acao = Acao.Indefinida
        self.velocidade = 1
        self.dimensoes_bounding_box = (16, 16)
        
        # carrego o sprite sheet inteiro.
        sprite_sheet = image.load("Graphics/sprite_sheet.png")

        # quebro em imagens menores (sprites do personagem, cada retangulo é um sprite, começando do zero)
        dimensoes_sprites = [Rect(3, 125, 14, 13), Rect(20, 125, 14, 13), Rect(37, 125, 14, 13),\
                             Rect(54, 125, 14, 13), Rect(71, 125, 14, 13), Rect(88, 125, 14, 13),\
                             Rect(105, 125, 14, 13), Rect(122, 125, 14, 13), Rect(3, 198, 14, 13),\
                             Rect(20, 198, 14, 13), Rect(37, 198, 14, 13), Rect(54, 198, 14, 13),\
                             Rect(71, 203, 11, 4), Rect(88, 203, 11, 4), Rect(105, 202, 10, 5),\
                             Rect(122, 202, 10, 5)]

        # defino a sequencia de sprites para cada acao
        sequencia_sprites = [[4, 6, 0, 3],\
                             [4, 5],\
                             [6, 7],\
                             [0, 1],\
                             [2, 3],\
                             [8, 10, 9, 11],\
                             [14],\
                             [15],\
                             [12],\
                             [13]]

        # armazeno a animação do personagem
        self.animacao = Animacao(dimensoes_sprites, sequencia_sprites)

    def draw(self, tela):
        # desenho a animação, dado o sprite atual e as dimensoes já armazenadas.
        self.animacao.draw(tela, self)

    def bounding_box(self):
        # apelido dos eixos 
        x, y = 0, 1
        return Rect(self.posicao[x], self.posicao[y], self.dimensoes_bounding_box[x], self.dimensoes_bounding_box[y])

    def move(self, teclas, jogo):
        # apelido dos eixos 
        x, y = 0, 1
        
        # ordena as paredes pela proximidade
        jogo.fases[jogo.fase_atual].paredes.sort(key=lambda elemento: abs(elemento.posicao[x] - self.posicao[x]) +\
                                                                      abs(elemento.posicao[y] - self.posicao[y]))     
  
        # guardo a acao anterior
        acao_anterior = self.acao

        # se alguma tecla foi pressionada agora, proxima acao será ir na direcao da tecla.  
        if teclas[K_UP]:
            self.proxima_acao = Acao.AndarCima

        if teclas[K_DOWN]:
            self.proxima_acao = Acao.AndarBaixo

        if teclas[K_LEFT]:
            self.proxima_acao = Acao.AndarEsquerda

        if teclas[K_RIGHT]:
            self.proxima_acao = Acao.AndarDireita

        # testo se é possível realizar a próxima acao agora
        if not self.colisao(self.proxima_acao, jogo):
            if self.proxima_acao == Acao.AndarCima:
                self.posicao[y] -= self.velocidade
                self.acao = self.proxima_acao
                self.proxima_acao = Acao.Indefinida

            elif self.proxima_acao == Acao.AndarBaixo:
                self.posicao[y] += self.velocidade
                self.acao = self.proxima_acao
                self.proxima_acao = Acao.Indefinida

            elif self.proxima_acao == Acao.AndarEsquerda:
                self.posicao[x] -= self.velocidade
                self.acao = self.proxima_acao
                self.proxima_acao = Acao.Indefinida

            elif self.proxima_acao == Acao.AndarDireita:
                self.posicao[x] += self.velocidade
                self.acao = self.proxima_acao
                self.proxima_acao = Acao.Indefinida
            
            if acao_anterior != self.acao:
                self.animacao.sprite_atual = 0

        # senao, realiza a mesma acao de antes, se não hove colisao com a parede
        elif not self.colisao(acao_anterior, jogo):
            if acao_anterior == Acao.AndarCima:
                self.posicao[y] -= self.velocidade
                self.acao = acao_anterior

            elif acao_anterior == Acao.AndarBaixo:
                self.posicao[y] += self.velocidade
                self.acao = acao_anterior

            elif acao_anterior == Acao.AndarEsquerda:
                self.posicao[x] -= self.velocidade
                self.acao = acao_anterior

            elif acao_anterior == Acao.AndarDireita:
                self.posicao[x] += self.velocidade
                self.acao = acao_anterior
            
        # senao para o personagem
        else:
            if self.acao == Acao.AndarCima:
                self.animacao.sprite_atual = 2
            elif self.acao == Acao.AndarBaixo:
                self.animacao.sprite_atual = 3
            elif self.acao == Acao.AndarEsquerda:
                self.animacao.sprite_atual = 1
            elif self.acao == Acao.AndarDireita:
                self.animacao.sprite_atual = 0
            self.acao = Acao.Parado


    def colisao(self, direcao:Acao, jogo):
        # se a proxima acao for indefinida, retorno que houve colisao para não acontecer nada
        if direcao not in [Acao.AndarCima, Acao.AndarBaixo, Acao.AndarEsquerda, Acao.AndarDireita]:
            return True
        
        # apelido dos eixos 
        x, y = 0, 1

        # realizo o movimento
        if direcao == Acao.AndarCima:       self.posicao[y] -= self.velocidade   
        elif direcao == Acao.AndarBaixo:    self.posicao[y] += self.velocidade 
        elif direcao == Acao.AndarEsquerda: self.posicao[x] -= self.velocidade 
        elif direcao == Acao.AndarDireita:  self.posicao[x] += self.velocidade 
        
        # defino o limite de busca
        limite_busca = 4

        # testo se há colisao
        colisao = []
        for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            
                bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  
                if bounding_box_self.colliderect(bounding_box_objeto): 
                    colisao.append(True)
                
        # desfaço o movimento
        if direcao == Acao.AndarCima:       self.posicao[y] += self.velocidade   
        elif direcao == Acao.AndarBaixo:    self.posicao[y] -= self.velocidade 
        elif direcao == Acao.AndarEsquerda: self.posicao[x] += self.velocidade 
        elif direcao == Acao.AndarDireita:  self.posicao[x] -= self.velocidade 

        return colisao