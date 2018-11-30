from Libraries import *
from Classes.Outros.GameComponent import GameComponent
from Classes.Outros.Movimento import *

class Clyde(GameComponent):
    """inimigo do jogo, controlado pela IA."""
    def __init__(self, posicao: list):
        # construtor base
        self.pontuacao = 1000
        super().__init__(posicao, "Clyde.bmp")

    def bounding_box(self):
        return Rect(self.movimento.posicao, self.sprite.sprite_size)

    def dentro_casa_fantasmas(self, elementos_fase, posicao_futura=None, direcao_atual=None):
        # apelido dos eixos
        x, y = 0, 1

        if posicao_futura is None and direcao_atual is None:
            return self.bounding_box().colliderect(elementos_fase.casa_fantasmas)

        elif posicao_futura is None and direcao_atual is not None:
            if direcao_atual == direcao.cima:
                return Rect((self.movimento.posicao[x], self.movimento.posicao[y] - 1), (16, 14)).colliderect(
                    elementos_fase.casa_fantasmas)

            elif direcao_atual == direcao.baixo:
                return Rect((self.movimento.posicao[x], self.movimento.posicao[y] + 1), (16, 14)).colliderect(
                    elementos_fase.casa_fantasmas)

            elif direcao_atual == direcao.esquerda:
                return Rect((self.movimento.posicao[x] - 1, self.movimento.posicao[y]), (16, 14)).colliderect(
                    elementos_fase.casa_fantasmas)

            elif direcao_atual == direcao.direita:
                return Rect((self.movimento.posicao[x] + 1, self.movimento.posicao[y]), (16, 14)).colliderect(
                    elementos_fase.casa_fantasmas)

        else:
            return Rect(posicao_futura, (16, 14)).colliderect(elementos_fase.casa_fantasmas)

    def escolher_acao(self, elementos_fase):
        # apelido dos eixos
        x, y = 0, 1

        # crio o array de teclas
        teclas = [0] * len(key.get_pressed())

        # IA decide qual direcao deverá ir.
        proxima_direcao = self.ai(elementos_fase)

        # pressiona a tecla conforme a direcao retornada
        if proxima_direcao == direcao.cima:
            teclas[K_8] = 1
        elif proxima_direcao == direcao.baixo:
            teclas[K_5] = 1
        elif proxima_direcao == direcao.esquerda:
            teclas[K_4] = 1
        elif proxima_direcao == direcao.direita:
            teclas[K_6] = 1

        # retorno as teclas
        return teclas


    def ai(self, elementos_fase):
        # apelido dos eixos
        x, y = 0, 1

        # se dentro da casa dos fantasmas, sai dela
        if self.dentro_casa_fantasmas(elementos_fase):

            # crio a posicao futura em todas as direcoes
            acoes = [{"posicao": [self.movimento.posicao[x], self.movimento.posicao[y] - 1],
                      "distancia": None,
                      "distancia_x": None,
                      "distancia_y": None,
                      "direcao": direcao.cima},

                     {"posicao": [self.movimento.posicao[x], self.movimento.posicao[y] + 1],
                      "distancia": None,
                      "distancia_x": None,
                      "distancia_y": None,
                      "direcao": direcao.baixo},

                     {"posicao": [self.movimento.posicao[x] - 1, self.movimento.posicao[y]],
                      "distancia": None,
                      "distancia_x": None,
                      "distancia_y": None,
                      "direcao": direcao.esquerda},

                     {"posicao": [self.movimento.posicao[x] + 1, self.movimento.posicao[y]],
                      "distancia": None,
                      "distancia_x": None,
                      "distancia_y": None,
                      "direcao": direcao.direita}]

            # removo a acao oposta a atual
            acoes = [x for x in acoes if
                     x["direcao"] != direcao.cima and self.movimento.proxima_direcao == direcao.baixo or
                     x["direcao"] != direcao.baixo and self.movimento.proxima_direcao == direcao.cima or
                     x["direcao"] != direcao.esquerda and self.movimento.proxima_direcao == direcao.direita or
                     x["direcao"] != direcao.direita and self.movimento.proxima_direcao == direcao.esquerda and
                     not self.colisao(x["direcao"], elementos_fase)]

            # calculo a distancia de manhattan entre as posicoes futuras do fantasma e a porta
            for acao in acoes:
                resultado_x, resultado_y = subtract(acao["posicao"], (elementos_fase.casa_fantasmas.centerx, elementos_fase.casa_fantasmas.centery - (self.sprite.sprite_size[x] * 4)))
                acao["distancia"] = abs(resultado_x) + abs(resultado_y)
                acao["distancia_x"] = resultado_x
                acao["distancia_y"] = resultado_y

            # ordeno pela distancia
            acoes.sort(key=lambda x: x["distancia"])

            # retorno a melhor solucao que seja valida
            for acao in acoes:
                if not self.colisao(acao["direcao"], elementos_fase):
                    return acao["direcao"]

        # senao se move no mapa
        else:
            direcao_escolhida = None
            if self.movimento.direcao_atual == direcao.cima:
                direcao_escolhida = choice([direcao.esquerda, direcao.direita])

            if self.movimento.direcao_atual == direcao.baixo:
                direcao_escolhida = choice([direcao.esquerda, direcao.direita])

            if self.movimento.direcao_atual == direcao.esquerda:
                direcao_escolhida = choice([direcao.cima, direcao.baixo])

            if self.movimento.direcao_atual == direcao.direita:
                direcao_escolhida = choice([direcao.cima, direcao.baixo])

            if not self.colisao(direcao_escolhida, elementos_fase) and not self.dentro_casa_fantasmas(elementos_fase, direcao_atual=direcao_escolhida):
                return direcao_escolhida


    def move(self, elementos_fase):

        # define a próxima acao
        teclas = self.escolher_acao(elementos_fase)

        # apelido dos eixos 
        x, y = 0, 1

        # ordena as paredes pela proximidade
        elementos_fase.paredes.sort(key=lambda elemento: abs(elemento.movimento.posicao[x] - self.movimento.posicao[x]) +\
                                                                        abs(elemento.movimento.posicao[y] - self.movimento.posicao[y]))     
            
        # guardo a acao anterior
        direcao_anterior = self.movimento.direcao_atual

        # se alguma tecla foi pressionada agora, proxima acao será ir na direcao da tecla.  
        if teclas[K_8]:
            self.movimento.estado = estado.andando
            self.movimento.proxima_direcao = direcao.cima

        if teclas[K_5]:
            self.movimento.estado = estado.andando
            self.movimento.proxima_direcao = direcao.baixo

        if teclas[K_4]:
            self.movimento.estado = estado.andando
            self.movimento.proxima_direcao = direcao.esquerda

        if teclas[K_6]:
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


    def colisao(self, direcao: direcao, elementos_fase, posicao=None):
        if posicao is None:
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
            limite_busca = 10

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

        else:
            # se a proxima acao for indefinida, retorno que houve colisao para não acontecer nada
            if direcao not in [direcao.cima, direcao.baixo, direcao.esquerda, direcao.direita]:
                return True

            # apelido dos eixos
            x, y = 0, 1

            # realizo o movimento
            if direcao == direcao.cima:       posicao[y] -= 1
            elif direcao == direcao.baixo:    posicao[y] += 1
            elif direcao == direcao.esquerda: posicao[x] -= 1
            elif direcao == direcao.direita:  posicao[x] += 1

            # defino o limite de busca
            limite_busca = 10

            # testo se há colisao
            # testo todas as paredes ao redor, verificando se houve colisao com alguma delas
            colisao = []
            for parede in elementos_fase.paredes[:limite_busca]:
                if Rect(posicao,(16,14)).colliderect(parede.bounding_box()):
                    colisao.append(True)

            # desfaço o movimento
            if direcao == direcao.cima:       posicao[y] += 1
            elif direcao == direcao.baixo:    posicao[y] -= 1
            elif direcao == direcao.esquerda: posicao[x] += 1
            elif direcao == direcao.direita:  posicao[x] -= 1
            return colisao