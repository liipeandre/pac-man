from Libraries import mixer

class Sons(object):
    """ Classe que gerencia efeitos sonoros e música do jogo."""
    def __init__(self):
        # diretório da pasta audio
        self.diretorio_base = "Data/Audio/"

        # carregando sons e música
        self.pacman_beginning = mixer.Sound(file=self.diretorio_base + "pacman_beginning.ogg")
        self.pacman_chomp = mixer.Sound(file=self.diretorio_base + "pacman_chomp.ogg")
        self.pacman_death = mixer.Sound(file=self.diretorio_base + "pacman_death.ogg")
        self.pacman_eatfruit = mixer.Sound(file=self.diretorio_base + "pacman_eatfruit.ogg")
        self.pacman_eatghost = mixer.Sound(file=self.diretorio_base + "pacman_eatghost.ogg")
        self.pacman_extrapac = mixer.Sound(file=self.diretorio_base + "pacman_extrapac.ogg")
        self.ghost_frightened = mixer.Sound(file=self.diretorio_base + "ghost_frightened.ogg")
        self.ghost_return_to_home = mixer.Sound(file=self.diretorio_base + "ghost_return_to_home.ogg")
        self.ghost_siren = mixer.Sound(file=self.diretorio_base + "ghost_siren.ogg")