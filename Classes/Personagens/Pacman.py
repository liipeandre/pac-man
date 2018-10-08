from Classes.Outros.Animacao import *
from pygame import *
from Classes.Game import *
from Classes.Tiles.Parede import *

class Pacman(object):
    def __init__(self, posicao_personagem: list, jogo):
        # posicoes do personagem na tela, a acao que ele esta fazendo e a velocidade de movimentacao
        self.posicao = posicao_personagem
        self.acao = Acao.Parado
        self.velocidade = 1
        self.dimensoes_bounding_box = (14, 14)

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

    def gera_bounding_box(self, objeto):
        # apelido dos eixos 
        x, y = 0, 1

        # gero as duas bounding boxes (um retangulo), uma de cada objeto
        bounding_box_self = Rect(self.posicao[x], self.posicao[y], self.dimensoes_bounding_box[x], self.dimensoes_bounding_box[y])
        bounding_box_objeto = Rect(objeto.posicao[x], objeto.posicao[y], objeto.dimensoes_bounding_box[x], objeto.dimensoes_bounding_box[y])
        
        # retorna as duas bounding boxes.
        return bounding_box_self, bounding_box_objeto


    def move(self, teclas, jogo):
        # apelido dos eixos 
        x, y = 0, 1
        
        # ordena as paredes pela proximidade
        jogo.fases[jogo.fase_atual].paredes.sort(key=lambda elemento: abs(elemento.posicao[x] - jogo.fases[jogo.fase_atual].pacman.posicao[x]) +\
                                                                      abs(elemento.posicao[y] - jogo.fases[jogo.fase_atual].pacman.posicao[y]))
        # defino um limite de busca
        limite_busca = 7

        if teclas[K_UP]:                                                                 # se a tecla foi pressionada
            self.posicao[y] -= self.velocidade                                           # faço o movimento para depois validar se o movimento eh valido
            for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            # testa se o personagem colidiu com a parede.
                bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  # gero as bounding boxes
                
                if bounding_box_self.colliderect(bounding_box_objeto):                   # se colidiu com a parede, o movimento eh inválido, 
                    self.posicao[y] += self.velocidade                                   # logo devo desfaze-la
                    self.acao = Acao.Parado
                    self.animacao.sprite_atual = 0                                       # coloco o sprite atual de acordo com a direcao de movimento
                else:
                    self.acao = Acao.AndarCima
         
        elif teclas[K_DOWN]:                                                             # se a tecla foi pressionada
            self.posicao[y] += self.velocidade                                           # faço o movimento para depois validar se o movimento eh valido
            for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            # testa se o personagem colidiu com a parede.
                bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  # gero as bounding boxes
                
                if bounding_box_self.colliderect(bounding_box_objeto):                   # se colidiu com a parede, o movimento eh inválido, 
                    self.posicao[y] -= self.velocidade                                   # logo devo desfaze-la
                    self.acao = Acao.Parado
                    self.animacao.sprite_atual = 0                                       # coloco o sprite atual de acordo com a direcao de movimento
                else:
                    self.acao = Acao.AndarBaixo

        elif teclas[K_LEFT]:                                                             # se a tecla foi pressionada
            self.posicao[x] -= self.velocidade                                           # faço o movimento para depois validar se o movimento eh valido
            for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            # testa se o personagem colidiu com a parede.
                bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  # gero as bounding boxes
                
                if bounding_box_self.colliderect(bounding_box_objeto):                   # se colidiu com a parede, o movimento eh inválido, 
                    self.posicao[x] += self.velocidade                                   # logo devo desfaze-la
                    self.acao = Acao.Parado
                    self.animacao.sprite_atual = 0                                       # coloco o sprite atual de acordo com a direcao de movimento
                else:
                    self.acao = Acao.AndarEsquerda

        elif teclas[K_RIGHT]:                                                            # se a tecla foi pressionada
            self.posicao[x] += self.velocidade                                           # faço o movimento para depois validar se o movimento eh valido
            for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            # testa se o personagem colidiu com a parede.
                bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  # gero as bounding boxes
                
                if bounding_box_self.colliderect(bounding_box_objeto):                   # se colidiu com a parede, o movimento eh inválido, 
                    self.posicao[x] -= self.velocidade                                   # logo devo desfaze-la
                    self.acao = Acao.Parado
                    self.animacao.sprite_atual = 0                                       # coloco o sprite atual de acordo com a direcao de movimento
                else:
                    self.acao = Acao.AndarDireita

        else:  # se nenhuma tecla foi pressionada, continua a última acao feita.
            if int(self.acao) == int(Acao.AndarCima):                                   
                self.posicao[y] -= self.velocidade                                           # faço o movimento para depois validar se o movimento eh valido
                for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            # testa se o personagem colidiu com a parede.
                    bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  # gero as bounding boxes
                
                    if bounding_box_self.colliderect(bounding_box_objeto):                   # se colidiu com a parede, o movimento eh inválido, 
                        self.posicao[y] += self.velocidade                                   # logo devo desfaze-la
                        self.acao = Acao.Parado
                        self.animacao.sprite_atual = 0                                       # coloco o sprite atual de acordo com a direcao de movimento
                    else:
                        self.acao = Acao.AndarCima

            elif int(self.acao) == int(Acao.AndarBaixo):                                 
                self.posicao[y] += self.velocidade                                           # faço o movimento para depois validar se o movimento eh valido
                for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            # testa se o personagem colidiu com a parede.
                    bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  # gero as bounding boxes
                
                    if bounding_box_self.colliderect(bounding_box_objeto):                   # se colidiu com a parede, o movimento eh inválido, 
                        self.posicao[y] -= self.velocidade                                   # logo devo desfaze-la
                        self.acao = Acao.Parado
                        self.animacao.sprite_atual = 0                                       # coloco o sprite atual de acordo com a direcao de movimento
                    else:
                        self.acao = Acao.AndarBaixo



            elif int(self.acao) == int(Acao.AndarEsquerda):                              
                self.posicao[x] -= self.velocidade                                           # faço o movimento para depois validar se o movimento eh valido
                for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            # testa se o personagem colidiu com a parede.
                    bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  # gero as bounding boxes
                
                    if bounding_box_self.colliderect(bounding_box_objeto):                   # se colidiu com a parede, o movimento eh inválido, 
                        self.posicao[x] += self.velocidade                                   # logo devo desfaze-la
                        self.acao = Acao.Parado
                        self.animacao.sprite_atual = 0
                    else:
                        self.acao = Acao.AndarEsquerda

            elif int(self.acao) == int(Acao.AndarDireita):                               
                self.posicao[x] += self.velocidade                                           # faço o movimento para depois validar se o movimento eh valido
                for parede in jogo.fases[jogo.fase_atual].paredes[:limite_busca]:            # testa se o personagem colidiu com a parede.
                    bounding_box_self, bounding_box_objeto = self.gera_bounding_box(parede)  # gero as bounding boxes
                
                    if bounding_box_self.colliderect(bounding_box_objeto):                   # se colidiu com a parede, o movimento eh inválido, 
                        self.posicao[x] -= self.velocidade                                   # logo devo desfaze-la
                        self.acao = Acao.Parado
                        self.animacao.sprite_atual = 0
                    else:
                        self.acao = Acao.AndarDireita