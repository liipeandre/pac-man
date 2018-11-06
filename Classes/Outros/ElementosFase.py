class ElementosFase(object):
    """ Mantém os elementos da fase (itens, personagens, etc.)."""
    def __init__(self, fase_atual):
        # referencia para a fase atual
        self.fase_atual = fase_atual

        # personagens
        self.pacman = None
        self.blinky = None
        self.pinky = None
        self.inky = None
        self.clyde = None

        # itens, paredes do mapa
        self.item = None
        self.chave = None
        self.paredes = []
        self.pacdots = []
        self.powerpills = []

        # posicoes onde aparecerao os itens, a chave e a casa dos fantasmas e as posicoes iniciais do personagens, dentro do jogo
        self.casa_fantasmas = None
        self.posicao_inicial_pacman = None
        self.posicao_inicial_blinky = None
        self.posicao_inicial_pinky = None
        self.posicao_inicial_inky = None
        self.posicao_inicial_clyde = None
        self.posicao_itens = None
        self.posicao_chave = None