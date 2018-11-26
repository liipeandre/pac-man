from Libraries import mixer
from enum import Enum

class ControleAudio(object):
    """ Classe que gerencia efeitos sonoros e música do jogo."""
    def __init__(self):
        # diretório da pasta audio
        self.diretorio_base = "Data/Audio/"

        # carregando sons e música
        self.nome_arquivos_audio = ["pacman_beginning.ogg",\
                          "pacman_death.ogg",\
                          "pacman_eatfruit.ogg",\
                          "pacman_eatghost.ogg",\
                          "pacman_extrapac.ogg",\
                          "ghost_frightened.ogg",\
                          "ghost_return_to_home.ogg",\
                          "ghost_siren.ogg"]

        # ordeno a lista para facilitar busca
        self.nome_arquivos_audio.sort()

        self.canais = [None] * len(self.nome_arquivos_audio)
        self.sons = []

        # carregando o audio e sons do jogo
        for arquivo_audio in self.nome_arquivos_audio:
            self.sons.append(mixer.Sound(file=self.diretorio_base + arquivo_audio))


    def tocar_som(self, nome_audio, repetir_num_vezes=-1):
        # apelido a variavel de controle de audio e o indice na lista de canais
        indice = self.nome_arquivos_audio.index(nome_audio)

        # se não toquei ela ainda ou não está tocando
        if self.canais[indice] == None or not self.canais[indice].get_busy():
                    
            # toca a mesma música novamente
            self.canais[indice] = self.sons[indice].play(repetir_num_vezes)


    def parar_som(self, nome_audio):
        # apelido a variavel de controle de audio e o indice na lista de canais
        indice = self.nome_arquivos_audio.index(nome_audio)

        # se toquei ela e está tocando
        if self.canais[indice] != None and self.canais[indice].get_busy():
                    
            # para a música
            self.canais[indice] = self.sons[indice].stop()


    def tocando(self, nome_audio):
        # apelido a variavel de controle de audio e o indice na lista de canais
        indice = self.nome_arquivos_audio.index(nome_audio)

        # retorna se está tocando
        return self.canais[indice] != None and self.canais[indice].get_busy()