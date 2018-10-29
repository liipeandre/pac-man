from Libraries import Rect, event, key, K_UP, K_DOWN, K_LEFT, K_RIGHT
from Classes.Outros.GameComponent import GameComponent
from Classes.Outros.Movimento import *
from Classes.Outros.Sprite import Sprite

class Pacman(GameComponent):
    """Personagem do jogo, controlado pelo jogador."""
    def __init__(self, posicao: list):
        # construtor base
        super().__init__(posicao, "Pac-man.bmp")

    def bounding_box(self):
        return Rect(self.movimento.posicao, self.sprite.sprite_size)

    def move(self, elementos_fase):
        # capturo as teclas presionadas
        event.pump()
        teclas = key.get_pressed()

        # apelido dos eixos 
        x, y = 0, 1

        # ordena as paredes pela proximidade
        elementos_fase.paredes.sort(key=lambda elemento: abs(elemento.movimento.posicao[x] - self.movimento.posicao[x]) +\
                                                                      abs(elemento.movimento.posicao[y] - self.movimento.posicao[y]))     

        # guardo a acao anterior
        direcao_anterior = self.movimento.direcao_atual

        # se alguma tecla foi pressionada agora, proxima acao será ir na direcao da tecla.  
        if teclas[K_UP]:
            self.movimento.proxima_direcao = direcao.cima

        if teclas[K_DOWN]:
            self.movimento.proxima_direcao = direcao.baixo

        if teclas[K_LEFT]:
            self.movimento.proxima_direcao = direcao.esquerda

        if teclas[K_RIGHT]:
            self.movimento.proxima_direcao = direcao.direita

        # testo se é possível realizar a próxima acao agora
        if not self.colisao(self.movimento.proxima_direcao, elementos_fase):
            if self.movimento.proxima_direcao == direcao.cima:
                self.movimento.posicao[y] -= self.movimento.velocidade
                self.movimento.direcao_atual = self.movimento.proxima_direcao
                self.proxima_direcao = direcao.indefinida

            elif self.movimento.proxima_direcao == direcao.baixo:
                self.movimento.posicao[y] += self.movimento.velocidade
                self.movimento.direcao_atual = self.movimento.proxima_direcao
                self.proxima_direcao = direcao.indefinida

            elif self.movimento.proxima_direcao == direcao.esquerda:
                self.movimento.posicao[x] -= self.movimento.velocidade
                self.movimento.direcao_atual = self.movimento.proxima_direcao
                self.proxima_direcao = direcao.indefinida

            elif self.movimento.proxima_direcao == direcao.direita:
                self.movimento.posicao[x] += self.movimento.velocidade
                self.movimento.direcao_atual = self.movimento.proxima_direcao
                self.proxima_direcao = direcao.indefinida
            
            # se algum teste acima foi valido, reseto a animação
            if direcao_anterior != self.movimento.direcao_atual:
                self.sprite.sprite_frame = [0, self.movimento.direcao_atual]

        # senao, realiza a mesma acao de antes, se não hove colisao com a parede
        elif not self.colisao(direcao_anterior, elementos_fase):
            if direcao_anterior == direcao.cima:
                self.movimento.posicao[y] -= self.movimento.velocidade
                self.movimento.direcao_atual = direcao_anterior

            elif direcao_anterior == direcao.baixo:
                self.movimento.posicao[y] += self.movimento.velocidade
                self.movimento.direcao_atual = direcao_anterior

            elif direcao_anterior == direcao.esquerda:
                self.movimento.posicao[x] -= self.movimento.velocidade
                self.movimento.direcao_atual = direcao_anterior

            elif direcao_anterior == direcao.direita:
                self.movimento.posicao[x] += self.movimento.velocidade
                self.movimento.direcao_atual = direcao_anterior
            
        # senao para o personagem
        else:
            if self.movimento.direcao_atual == direcao.cima:
                self.sprite.sprite_frame = [0, direcao.cima]

            elif self.movimento.direcao_atual == direcao.baixo:
                self.sprite.sprite_frame = [0, direcao.baixo]

            elif self.movimento.direcao_atual == direcao.esquerda:
                self.sprite.sprite_frame = [0, direcao.esquerda]

            elif self.movimento.direcao_atual == direcao.direita:
                self.sprite.sprite_frame = [0, direcao.direita]

            self.movimento.estado = estado.parado


    def colisao(self, direcao: direcao, elementos_fase):
        # se a proxima acao for indefinida, retorno que houve colisao para não acontecer nada
        if direcao not in [direcao.cima, direcao.baixo, direcao.esquerda, direcao.direita]:
            return True
        
        # apelido dos eixos 
        x, y = 0, 1

        # realizo o movimento
        if direcao == direcao.cima:       self.movimento.posicao[y] -= self.movimento.velocidade   
        elif direcao == direcao.baixo:    self.movimento.posicao[y] += self.movimento.velocidade 
        elif direcao == direcao.esquerda: self.movimento.posicao[x] -= self.movimento.velocidade 
        elif direcao == direcao.direita:  self.movimento.posicao[x] += self.movimento.velocidade 
        
        # defino o limite de busca
        limite_busca = 4

        # testo se há colisao
        # testo todas as paredes ao redor, verificando se houve colisao com alguma delas
        colisao = []
        for parede in elementos_fase.paredes[:limite_busca]:             
                if self.bounding_box().colliderect(parede.bounding_box()): 
                    colisao.append(True)
                
        # desfaço o movimento
        if direcao == direcao.cima:       self.movimento.posicao[y] += self.movimento.velocidade   
        elif direcao == direcao.baixo:    self.movimento.posicao[y] -= self.movimento.velocidade 
        elif direcao == direcao.esquerda: self.movimento.posicao[x] += self.movimento.velocidade 
        elif direcao == direcao.direita:  self.movimento.posicao[x] -= self.movimento.velocidade 

        return colisao