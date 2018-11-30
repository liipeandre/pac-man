from Classes.Outros.GameComponent import GameComponent, estado, estado2, direcao
from Classes.Personagens.Pacman import Pacman
from Classes.Personagens.Blinky import Blinky
from Classes.Personagens.Pinky import Pinky
from Classes.Personagens.Inky import Inky
from Classes.Personagens.Clyde import Clyde
from Classes.Outros.Objeto import Objeto
from Libraries import time, USEREVENT

class ControleFase(GameComponent):
    """ Realiza o controle da pontuação e das vidas. """
    def __init__(self, posicao: list, controle_fase=None, fase_atual=None):
        # referencia para a fase atual
        self.fase_atual = fase_atual

        # timer do modo fuga e do modo morto
        self.timer_modo_fuga = 6
        self.timer_morto = 3

        # construtor base
        super().__init__(posicao, "Nenhum", None, True)

        # controle de fim de fase
        self.fim_fase = False

        if controle_fase is None:
            # pontuacao e vidas da fase.
            self.pontuacao = 0
            self.vidas = 3
            self.multiplicador = 1

        else:
            # pontuacao e vidas da fase.
            self.pontuacao = controle_fase.pontuacao
            self.vidas = controle_fase.vidas
            self.multiplicador = controle_fase.multiplicador



    def sistema_itens_pontuacao(self, elementos_fase):
        # apelido dos eixos 
        x, y = 0, 1

        # ordena os pacdots pela proximidade
        elementos_fase.pacdots.sort(key=lambda elemento: abs(elemento.movimento.posicao[x] - self.movimento.posicao[x]) +\
                                                                      abs(elemento.movimento.posicao[y] - self.movimento.posicao[y]))

        # verifica se pacman colidiu com algum objeto (itens, pacdots e powerpills)
        # se colidiu, incrementa a pontuacao e exclui o item
        # copy() serve para iterar uma cópia da lista, pois não posso iterar e alterar a própria lista
        if elementos_fase.item is not None and elementos_fase.pacman.bounding_box().colliderect(elementos_fase.item.bounding_box()):

            # incrementa pontuacao
            self.pontuacao += elementos_fase.item.pontuacao

            # exclui o item
            elementos_fase.item = None

            # apelido a variavel de controle de audio e o indice na lista de canais
            elementos_fase.fase_atual.controle_audio.tocar_som("pacman_eatfruit.ogg", 1)

        for pacdot in elementos_fase.pacdots.copy():

            if elementos_fase.pacman.bounding_box().colliderect(pacdot.bounding_box()):

                # incrementa pontuacao
                self.pontuacao += pacdot.pontuacao

                # exclui a pacdot
                elementos_fase.pacdots.remove(pacdot)              

                # sai do laço
                break

        # se o pacman colidiu com uma powerpill, incrementa a pontuacao e muda o estado dos fantasmas
        for powerpill in elementos_fase.powerpills.copy():
            if elementos_fase.pacman.bounding_box().colliderect(powerpill.bounding_box()):

                # incrementa pontuacao
                self.pontuacao += powerpill.pontuacao

                # muda o estado dos fantasmas
                for fantasma in [elementos_fase.blinky, elementos_fase.pinky, elementos_fase.inky, elementos_fase.clyde]:
                    fantasma.movimento.estado2 = estado2.modo_fuga

                # seta o evento de transformar os fantasmas ao normal, daqui alguns segundos
                mudar_fantasmas_normal = USEREVENT + 2
                time.set_timer(mudar_fantasmas_normal, self.timer_modo_fuga * 1000)    # x1000 (milisegundos)

                # exclui a powerpill
                elementos_fase.powerpills.remove(powerpill)

                # toca o audio
                elementos_fase.fase_atual.controle_audio.tocar_som("ghost_frightened.ogg")

                # sai do laço
                break

        # se acabou os pacdots, insere a chave para passar de fase
        if not elementos_fase.pacdots and elementos_fase.chave is None:
            elementos_fase.chave = Objeto(elementos_fase.posicao_chave, "key")

        # se pacman colidir com uma chave, ele passa de fase e incrementa pontuacao
        if elementos_fase.chave is not None and elementos_fase.pacman.bounding_box().colliderect(elementos_fase.chave.bounding_box()):
            self.pontuacao += elementos_fase.chave.pontuacao
            self.fim_fase = True
            elementos_fase.chave = None

            # para os demais audios
            elementos_fase.fase_atual.controle_audio.parar_som("ghost_frightened.ogg")
            elementos_fase.fase_atual.controle_audio.parar_som("ghost_siren.ogg")
            elementos_fase.fase_atual.controle_audio.parar_som("ghost_return_to_home.ogg")

            # toca o audio
            elementos_fase.fase_atual.controle_audio.tocar_som("pacman_eatfruit.ogg", 0)

            # pausa o jogo por alguns segundos
            time.wait(2000)


        # se pontuacao for igual a 20000 pontos, ganha uma vida extra
        if self.pontuacao == 20000 * self.multiplicador:
            self.vidas += 1
            self.multiplicador += 1

            # toca o audio
            elementos_fase.fase_atual.controle_audio.tocar_som("pacman_extrapac.ogg", 0)


    def sistema_colisao_fantasmas(self, elementos_fase):
        # se os fantasmas estiverem no centro da casa dos fantasmas, mudo o estado dele para vivo
        for fantasma in [elementos_fase.blinky, elementos_fase.pinky, elementos_fase.inky, elementos_fase.clyde]:
            if fantasma.movimento.estado2 == estado2.morto and fantasma.movimento.posicao == elementos_fase.casa_fantasmas.center:
                fantasma.movimento.estado2 = estado2.vivo

        # testa se pacman colidiu com cada fantasma, se ele nao estiver morto ou morrendo.
        if elementos_fase.pacman.movimento.estado2 not in [estado2.morrendo, estado2.morto]:
            # se houve colisao
            for fantasma in [elementos_fase.blinky, elementos_fase.pinky, elementos_fase.inky, elementos_fase.clyde]:
                if elementos_fase.pacman.bounding_box().colliderect(fantasma.bounding_box()):
                    # se o fantasma estiver em modo fuga, come ele, incrementa pontuacao e muda o estado dele para morto
                    if fantasma.movimento.estado2 == estado2.modo_fuga:
                        self.pontuacao += fantasma.pontuacao
                        fantasma.movimento.estado2 = estado2.morto
                        # adicoina o evento de reviver os fantasmas daqui alguns segundos.
                        mudar_fantasmas_morto_normal = USEREVENT + 3
                        time.set_timer(mudar_fantasmas_morto_normal, self.timer_morto * 1000)  # x1000 (milisegundos)

                    # se ele nao estiver morto, pacman morre
                    elif fantasma.movimento.estado2 != estado2.morto:
                        elementos_fase.pacman.movimento.estado2 = estado2.morrendo
                        time.wait(500)

            # se pacman estiver morrendo, toca a música de morte do pacman
            if elementos_fase.pacman.movimento.estado2 == estado2.morrendo:
                # para os demais audios
                elementos_fase.fase_atual.controle_audio.parar_som("ghost_frightened.ogg")
                elementos_fase.fase_atual.controle_audio.parar_som("ghost_siren.ogg")
                elementos_fase.fase_atual.controle_audio.parar_som("ghost_return_to_home.ogg")

                # toca a musica de morte
                self.fase_atual.controle_audio.tocar_som("pacman_death.ogg", 0)

            for fantasma in [elementos_fase.blinky, elementos_fase.pinky, elementos_fase.inky, elementos_fase.clyde]:
                # se algum fantasma estiver morto, toca a música de morte dos fantasmas
                if fantasma.movimento.estado2 == estado2.morto:
                    self.fase_atual.controle_audio.tocar_som("ghost_return_to_home.ogg")
                    break

            # se todos os fantasmas estao normais toca a musica de perseguição
            todos_fantasmas = True
            for fantasma in [elementos_fase.blinky, elementos_fase.pinky, elementos_fase.inky, elementos_fase.clyde]:
                if fantasma.movimento.estado2 != estado2.vivo:
                    todos_fantasmas = False

            if todos_fantasmas and elementos_fase.pacman.movimento.estado2 == estado2.vivo:
                self.fase_atual.controle_audio.tocar_som("ghost_siren.ogg")
                self.fase_atual.controle_audio.parar_som("ghost_return_to_home.ogg")

        if elementos_fase.pacman.movimento.estado2 == estado2.morto:
            self.vidas -= 1


    def atualiza_sprite_frame(self, sprite_objeto):
        # apelido dos eixos
        x, y = 0, 1

        if type(sprite_objeto.game_component) is Pacman:
            # se morrendo, realiza a animação de morte
            if sprite_objeto.game_component.movimento.estado2 == estado2.morrendo:
                if sprite_objeto.game_component.sprite.sprite_frame[x] == 10:
                    sprite_objeto.game_component.sprite.sprite_frame = [9, 4]
                    sprite_objeto.game_component.movimento.estado2 = estado2.morto
                    time.wait(500)
                else:
                    sprite_objeto.game_component.sprite.sprite_frame = [sprite_objeto.game_component.sprite.sprite_frame[x]+1, 4]
                    time.wait(150)


            # se parado, fica travado em sprite frame específico
            elif sprite_objeto.game_component.movimento.estado == estado.parado:
                sprite_objeto.game_component.sprite.sprite_frame = [1, sprite_objeto.game_component.movimento.direcao_atual]

            # se andando, itera uma linha do sprite sheet, com os sprite frames da direcao escolhida.
            elif sprite_objeto.game_component.movimento.estado == estado.andando:
                if sprite_objeto.game_component.sprite.sprite_frame[x] == 2:
                    sprite_objeto.game_component.sprite.sprite_frame = [0, sprite_objeto.game_component.movimento.direcao_atual]
                else:
                    sprite_objeto.game_component.sprite.sprite_frame = [sprite_objeto.game_component.sprite.sprite_frame[x]+1, sprite_objeto.game_component.movimento.direcao_atual]
            return

        if type(sprite_objeto.game_component) in [Blinky, Pinky, Inky, Clyde]:
            # se morreu, realiza a animação de morte
            if sprite_objeto.game_component.movimento.estado2 == estado2.morto:
                if sprite_objeto.game_component.movimento.direcao_atual == direcao.cima:
                    sprite_objeto.game_component.sprite.sprite_frame = [2, 5]

                elif sprite_objeto.game_component.movimento.direcao_atual == direcao.baixo:
                    sprite_objeto.game_component.sprite.sprite_frame = [3, 5]

                elif sprite_objeto.game_component.movimento.direcao_atual == direcao.esquerda:
                    sprite_objeto.game_component.sprite.sprite_frame = [1, 5]

                elif sprite_objeto.game_component.movimento.direcao_atual == direcao.direita:
                    sprite_objeto.game_component.sprite.sprite_frame = [0, 5]

            # se modo fuga (quando pacman come uma powerpill), itera uma linha do sprite sheet, com os sprite frames.
            elif sprite_objeto.game_component.movimento.estado2 == estado2.modo_fuga:
                if sprite_objeto.game_component.sprite.sprite_frame[x] == 3:
                    sprite_objeto.game_component.sprite.sprite_frame = [0, 4]
                else:
                    sprite_objeto.game_component.sprite.sprite_frame = [sprite_objeto.game_component.sprite.sprite_frame[x]+1, 4]

            # se parado sem modo_fuga, fica travado em sprite frame específico
            elif sprite_objeto.game_component.movimento.estado == estado.parado and \
                sprite_objeto.game_component.movimento.estado2 == estado2.vivo:
                if sprite_objeto.game_component.movimento.estado2 != estado2.modo_fuga:
                    sprite_objeto.game_component.sprite.sprite_frame = [0, sprite_objeto.game_component.movimento.direcao_atual]

            # se parado com modo_fuga, fica travado em sprite frame específico
            elif sprite_objeto.game_component.movimento.estado == estado.parado and \
                sprite_objeto.game_component.movimento.estado2 == estado2.modo_fuga:
                if sprite_objeto.game_component.movimento.direcao_atual == direcao.cima:
                    sprite_objeto.game_component.sprite.sprite_frame = [2, 5]

                elif sprite_objeto.game_component.movimento.direcao_atual == direcao.baixo:
                    sprite_objeto.game_component.sprite.sprite_frame = [3, 5]

                elif sprite_objeto.game_component.movimento.direcao_atual == direcao.esquerda:
                    sprite_objeto.game_component.sprite.sprite_frame = [1, 5]

                elif sprite_objeto.game_component.movimento.direcao_atual == direcao.direita:
                    sprite_objeto.game_component.sprite.sprite_frame = [0, 5]

            # se andando, itera uma linha do sprite sheet, com os sprite frames da direcao escolhida.
            elif sprite_objeto.game_component.movimento.estado == estado.andando and \
                sprite_objeto.game_component.movimento.estado2 == estado2.vivo:
                if sprite_objeto.game_component.sprite.sprite_frame[x] == 1:
                    sprite_objeto.game_component.sprite.sprite_frame = [0, sprite_objeto.game_component.movimento.direcao_atual]
                else:
                    sprite_objeto.game_component.sprite.sprite_frame = [sprite_objeto.game_component.sprite.sprite_frame[x]+1, sprite_objeto.game_component.movimento.direcao_atual]


    def resetar_posicoes_personagens(self, elementos_fase):
        elementos_fase.pacman.resetar(elementos_fase.posicao_inicial_pacman)
        elementos_fase.blinky.resetar(elementos_fase.posicao_inicial_blinky)
        elementos_fase.pinky.resetar(elementos_fase.posicao_inicial_pinky)
        elementos_fase.inky.resetar(elementos_fase.posicao_inicial_inky)
        elementos_fase.clyde.resetar(elementos_fase.posicao_inicial_clyde)