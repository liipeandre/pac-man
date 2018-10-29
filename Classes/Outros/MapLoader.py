from Classes.Outros.Objeto import Objeto
from Classes.Personagens.Pacman import Pacman
from Classes.Personagens.Blinky import Blinky
from Classes.Personagens.Pinky import Pinky
from Classes.Personagens.Inky import Inky
from Classes.Personagens.Clyde import Clyde


class MapLoader(object):
    """ Carrega as fases a partir do arquivo."""

    def __init__(self, nome_fase:str, elementos_fase):
        # apelido dos eixos
        x, y = 0, 1
        
        # defino o sprite size e tamanho do mapa (mesmo valor daquele definido em sprite).
        sprite_size = (16, 14)
        map_size    = (31, 28) 

        # carrego o mapa a partir do arquivo
        with open("Data/Maps/" + nome_fase + ".txt", "r") as arquivo:
            
            # leio todas as linhas do arquivo
            mapa = arquivo.readlines()

            # percorro cada elemento de cada linha e coluna
            for i in range(map_size[x]):
                for j in range(map_size[y]):

                    # para cada simbolo, adiciono o elemento no jogo.
                    # pacman e fantasmas
                    if   mapa[i][j] == 'A': 
                        elementos_fase.pacman = Pacman([sprite_size[x] * j, sprite_size[y] * i])

                    elif mapa[i][j] == 'B': 
                        elementos_fase.blinky = Blinky([sprite_size[x] * j, sprite_size[y] * i])

                    elif mapa[i][j] == 'C': 
                        elementos_fase.pinky  = Pinky([sprite_size[x] * j, sprite_size[y] * i])
                        elementos_fase.casa_fantasmas = (sprite_size[x] * j, sprite_size[y] * i)

                    elif mapa[i][j] == 'D': 
                        elementos_fase.inky = Inky([sprite_size[x] * j, sprite_size[y] * i])

                    elif mapa[i][j] == 'E': 
                        elementos_fase.clyde = Clyde([sprite_size[x] * j, sprite_size[y] * i])

                    # parede
                    elif mapa[i][j] == '1' or mapa[i][j] == 'S': 
                        elementos_fase.paredes.append(Objeto([sprite_size[x] * j, sprite_size[y] * i], "wall"))

                    # powerpill
                    elif mapa[i][j] == 'P':
                        elementos_fase.powerpills.append(Objeto([sprite_size[x] * j, sprite_size[y] * i], "powerpill"))

                    # pacdot
                    elif mapa[i][j] == ' ':
                        elementos_fase.pacdots.append(Objeto([sprite_size[x] * j, sprite_size[y] * i], "pacdot"))

                    # chave (quando disponivel)
                    elif mapa[i][j] == 'K':
                        elementos_fase.posicao_chave = (sprite_size[x] * j, sprite_size[y] * i)

                    # itens (quando disponiveis)
                    elif mapa[i][j] == 'I':
                        elementos_fase.posicao_itens = (sprite_size[x] * j, sprite_size[y] * i)