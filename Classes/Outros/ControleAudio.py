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