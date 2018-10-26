from Classes.Outros.GameComponent import *

class Sprite(object):
    """ Classe que mantém os elementos pertencentes a parte de animação e desenho. Possui 2 construtores.
        
        - Para objetos móveis: recebe o sprite sheet e o component a qual ele pertence.
        - Para objetos fixos: recebe em adição ao anterior, o sprite_frame de animação (fixo).
    """
    # tamanho do sprite a ser exibido em tela
    sprite_size = (16, 14)

    def __init__(self, game_component: GameComponent, sprite_sheet_file: str, desenha_pontuacao=False):
        # referencia para o component, que contem o sprite (composicao - POO)
        self.game_component = game_component

        # define se será desenhado a pontuacao (padrão é igual a falso)
        self.desenha_pontuacao = desenha_pontuacao

        # se nao devo imprimir a pontuacao, realizo a acoes de ler o sprite.
        if not desenha_pontuacao:
            
            # frame atual, usado na animacao (eixos x e y)
            self.sprite_frame = [0, 0]

            # sprite sheet do personagem
            self.sprite_sheet = image.load("Data/Graphics/" + sprite_sheet_file)


    def __init__(self, game_component: GameComponent, sprite_sheet_file: str, sprite_frame: tuple, desenha_pontuacao=False):
        # referencia para o componente, que contem o sprite (composicao - POO)
        self.game_component = game_component

        # define se será desenhado a pontuacao (padrão é igual a falso)
        self.desenha_pontuacao = desenha_pontuacao

        # se nao devo imprimir a pontuacao, realizo a acoes de ler o sprite.
        if not desenha_pontuacao:

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
            texto1 = gerador_texto.render("Pontuação: " + str(self.pontuacao), antialiasing, cor)
            texto2 = gerador_texto.render("Vidas: " + str(self.vidas), antialiasing, cor)

            # desenho o texto na tela
            tela.blit(texto1, [self.posicao[x], self.posicao[y], 30, 30])
            tela.blit(texto2, [self.posicao[x], self.posicao[y] + 30, 30, 30])

        else:
            # dimensoes do sprite a ser desenhado
            dimensoes_sprite = Rect(self.sprite_frame[x] * sprite_size[x],\
                                    self.sprite_frame[y] * sprite_size[y],\
                                    self.sprite_size[x],\
                                    self.sprite_size[y])


            # desenha o objeto em tela
            tela.blit(self.sprite_sheet,\
                      self.game_componente.movimento.posicao,\
                      dimensoes_sprite)