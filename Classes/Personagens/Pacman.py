from Libraries import *
from Classes.Outros.GameComponent import GameComponent
from Classes.Outros.Movimento import *

class Pacman(GameComponent):
    """Personagem do jogo, controlado pelo jogador."""
    def __init__(self, posicao: list):
        # construtor base
        self.gravar = False
        super().__init__(posicao, "Pac-man.bmp")

    def bounding_box(self):
        return Rect(self.movimento.posicao, self.sprite.sprite_size)

    def escolher_acao(self):
        # capturo as teclas presionadas
        event.pump()
        return key.get_pressed()

    def move(self, elementos_fase):        
        # ignoro qualquer acao se ja estiver morto/morrendo
        if self.movimento.estado2 != estado2.morrendo:

            # define a próxima acao
            teclas = self.escolher_acao()

            # apelido dos eixos 
            x, y = 0, 1

            # ordena as paredes pela proximidade
            elementos_fase.paredes.sort(key=lambda elemento: abs(elemento.movimento.posicao[x] - self.movimento.posicao[x]) +\
                                                                          abs(elemento.movimento.posicao[y] - self.movimento.posicao[y]))     
            
            # guardo a acao anterior
            direcao_anterior = self.movimento.direcao_atual

            if teclas[K_SPACE]:
                self.gravar = True

            # se alguma tecla foi pressionada agora, proxima acao será ir na direcao da tecla.
            if teclas[K_UP]:
                self.movimento.estado = estado.andando
                self.movimento.proxima_direcao = direcao.cima

            if teclas[K_DOWN]:
                self.movimento.estado = estado.andando
                self.movimento.proxima_direcao = direcao.baixo

            if teclas[K_LEFT]:
                self.movimento.estado = estado.andando
                self.movimento.proxima_direcao = direcao.esquerda

            if teclas[K_RIGHT]:
                self.movimento.estado = estado.andando
                self.movimento.proxima_direcao = direcao.direita
            
            # defino o número de passos para a ação acontecer
            # ao invés de fazer o movimento de forma indivisivel, divide-se o andar em passos de 1 pixel por vez, verificando se houve colisao
            passos = 0
            
            while passos < self.movimento.velocidade:
                
                # testo se é possível realizar a próxima acao agora
                if not self.colisao(self.movimento.proxima_direcao, elementos_fase):
                    if self.movimento.proxima_direcao == direcao.cima:
                        self.movimento.posicao[y] -= 1
                        self.movimento.direcao_atual = self.movimento.proxima_direcao
                        self.proxima_direcao = direcao.indefinida

                    elif self.movimento.proxima_direcao == direcao.baixo:
                        self.movimento.posicao[y] += 1
                        self.movimento.direcao_atual = self.movimento.proxima_direcao
                        self.proxima_direcao = direcao.indefinida

                    elif self.movimento.proxima_direcao == direcao.esquerda:
                        self.movimento.posicao[x] -= 1
                        self.movimento.direcao_atual = self.movimento.proxima_direcao
                        self.proxima_direcao = direcao.indefinida

                    elif self.movimento.proxima_direcao == direcao.direita:
                        self.movimento.posicao[x] += 1
                        self.movimento.direcao_atual = self.movimento.proxima_direcao
                        self.proxima_direcao = direcao.indefinida
            
                    # se algum teste acima foi valido, reseto a animação
                    if direcao_anterior != self.movimento.direcao_atual:
                        self.sprite.sprite_frame = [0, self.movimento.direcao_atual]

                # senao, realiza a mesma acao de antes, se não hove colisao com a parede
                elif not self.colisao(direcao_anterior, elementos_fase):
                    if direcao_anterior == direcao.cima:
                        self.movimento.posicao[y] -= 1
                        self.movimento.direcao_atual = direcao_anterior

                    elif direcao_anterior == direcao.baixo:
                        self.movimento.posicao[y] += 1
                        self.movimento.direcao_atual = direcao_anterior

                    elif direcao_anterior == direcao.esquerda:
                        self.movimento.posicao[x] -= 1
                        self.movimento.direcao_atual = direcao_anterior

                    elif direcao_anterior == direcao.direita:
                        self.movimento.posicao[x] += 1
                        self.movimento.direcao_atual = direcao_anterior
            
                # senao para o personagem
                else:
                    self.movimento.estado = estado.parado
                    break
                passos += 1


    def colisao(self, direcao: direcao, elementos_fase):
        # se a proxima acao for indefinida, retorno que houve colisao para não acontecer nada
        if direcao not in [direcao.cima, direcao.baixo, direcao.esquerda, direcao.direita]:
            return True
        
        # apelido dos eixos 
        x, y = 0, 1

        # realizo o movimento
        if direcao == direcao.cima:       self.movimento.posicao[y] -= 1
        elif direcao == direcao.baixo:    self.movimento.posicao[y] += 1
        elif direcao == direcao.esquerda: self.movimento.posicao[x] -= 1
        elif direcao == direcao.direita:  self.movimento.posicao[x] += 1
        
        # defino o limite de busca
        limite_busca = 4

        # testo se há colisao
        # testo todas as paredes ao redor, verificando se houve colisao com alguma delas
        colisao = []
        for parede in elementos_fase.paredes[:limite_busca]:             
                if self.bounding_box().colliderect(parede.bounding_box()): 
                    colisao.append(True)
                
        # desfaço o movimento
        if direcao == direcao.cima:       self.movimento.posicao[y] += 1   
        elif direcao == direcao.baixo:    self.movimento.posicao[y] -= 1 
        elif direcao == direcao.esquerda: self.movimento.posicao[x] += 1
        elif direcao == direcao.direita:  self.movimento.posicao[x] -= 1

        return colisao