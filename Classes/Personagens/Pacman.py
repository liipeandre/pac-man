from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *

class Pacman(object):
    def __init__(self, posicao_personagem: list, jogo):
        # posicoes do personagem na tela, a acao que ele esta fazendo e a velocidade de movimentacao
        self.posicao = posicao_personagem
        self.acao = Acao.Parado
        self.proxima_acao = Acao.Indefinida
        self.velocidade = 1
        self.dimensoes_bounding_box = (16, 16)

        # carrego o sprite sheet inteiro.
        sprite_sheet = image.load("Graphics/sprite_sheet.png")

        # quebro em imagens menores (sprites do personagem, cada retangulo é um sprite, começando do zero)
        dimensoes_sprites = [Rect(3, 90, 14, 14), Rect(20, 90, 12, 14), Rect(35, 90, 9, 14),\
                             Rect(48, 90, 12, 14), Rect(63, 90, 9, 14), Rect(75, 92, 14, 12),\
                             Rect(92, 95, 14, 9), Rect(109, 92, 14, 12), Rect(126, 95, 14, 9),\
                             Rect(3, 112, 16, 7), Rect(22, 113, 16, 6), Rect(41, 114, 16, 5),\
                             Rect(60, 114, 16, 5), Rect(79, 113, 16, 6), Rect(98, 113, 14, 6),\
                             Rect(115, 112, 10, 7), Rect(128, 113, 6, 6), Rect(137, 113, 2, 6),\
                             Rect(142, 109, 12, 10)]

        # defino a sequencia de sprites para cada acao
        sequencia_sprites = [[1, 3, 5, 7],\
                             [5, 6, 5, 0],\
                             [7, 8, 7, 0],\
                             [1, 2, 1, 0],\
                             [3, 4, 3, 0],\
                             [x for x in range(9, 19)]]


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
        jogo.fase_atual.paredes.sort(key=lambda elemento: abs(elemento.posicao[x] - self.posicao[x]) +\
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
            teste = self.colisao(self.proxima_acao, jogo)
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
        # testo todas as paredes ao redor, verificando se houve colisao com alguma delas
        colisao = []
        for parede in jogo.fase_atual.paredes[:limite_busca]:             
                if self.bounding_box().colliderect(parede.bounding_box()): 
                    colisao.append(True)
                
        # desfaço o movimento
        if direcao == Acao.AndarCima:       self.posicao[y] += self.velocidade   
        elif direcao == Acao.AndarBaixo:    self.posicao[y] -= self.velocidade 
        elif direcao == Acao.AndarEsquerda: self.posicao[x] += self.velocidade 
        elif direcao == Acao.AndarDireita:  self.posicao[x] -= self.velocidade 

        return colisao