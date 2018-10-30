from Libraries import Rect, image, font
from Classes.Outros.Movimento import *

class Sprite(object):
    """ Classe que mantém os elementos pertencentes a parte de animação e desenho. Possui 2 construtores.
        
        - Para objetos móveis: recebe o sprite sheet e o component a qual ele pertence.
        - Para objetos fixos: recebe em adição ao anterior, o sprite_frame de animação (fixo).
    """
    # tamanho do sprite a ser exibido em tela
    sprite_size = (16, 14)

    def __init__(self, game_component, sprite_sheet_file: str, sprite_frame=None, desenha_pontuacao=False):
        # referencia para o component, que contem o sprite (composicao - POO)
        self.game_component = game_component
        print(type(self.game_component))

        # define se será desenhado a pontuacao (padrão é igual a falso)
        self.desenha_pontuacao = desenha_pontuacao

        # se sprite móvel
        if sprite_frame is None:
            
            # frame atual, usado na animacao (eixos x e y)
            self.sprite_frame = [0, 0]

            if not desenha_pontuacao:

                # sprite sheet do personagem
                self.sprite_sheet = image.load("Data/Graphics/" + sprite_sheet_file)

        # senao, leio o sprite sheet e o sprite frame fixo
        else:

            # frame atual, usado na animacao (eixos x e y)
            self.sprite_frame = sprite_frame

            # sprite sheet do personagem
            self.sprite_sheet = image.load("Data/Graphics/" + sprite_sheet_file)

    def draw(self, tela):
        # apelido dos eixos
        x, y = 0, 1

        if self.desenha_pontuacao:

            # defino a fonte e o tamanho da fonte
            cor = (255, 255, 255)
            antialiasing = True
            gerador_texto = font.SysFont('Comic Sans MS', 18)

            # renderizo os textos em tela
            texto1 = gerador_texto.render("Pontuação: " + str(self.game_component.pontuacao), antialiasing, cor)
            texto2 = gerador_texto.render("Vidas: " + str(self.game_component.vidas), antialiasing, cor)

            # desenho o texto na tela
            tela.blit(texto1, [self.game_component.movimento.posicao[x], self.game_component.movimento.posicao[y], 30, 30])
            tela.blit(texto2, [self.game_component.movimento.posicao[x], self.game_component.movimento.posicao[y] + 30, 30, 30])

        else:
            # dimensoes do sprite a ser desenhado
            dimensoes_sprite = Rect(self.sprite_frame[x] * self.sprite_size[x],\
                                    self.sprite_frame[y] * self.sprite_size[y],\
                                    self.sprite_size[x],\
                                    self.sprite_size[y])


            # desenha o objeto em tela
            tela.blit(self.sprite_sheet,\
                      self.game_component.movimento.posicao,\
                      dimensoes_sprite)


    def resetar_animacao(self):
        if type(self.game_component) == Pacman:
            if self.game_component.movimento.direcao_atual == direcao.cima:
                return