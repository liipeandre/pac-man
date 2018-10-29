from Classes.Outros.GameComponent import *

class Objeto(object, GameComponent):
    """Classe que representa os elementos fixos do jogo (itens e a parede)."""
    def __init__(self, posicao: list, tipo_item: str):

        # cria o item e/ou parede, conforme o tipo passado.
        # chama o construtor base, passando parâmetros exclusivo para cada tipo de objeto.
        if tipo_item == "cherry":
            self.pontuacao = 100
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 0))
        
        elif tipo_item == "strawberry":
            self.pontuacao = 300
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 1))

        elif tipo_item == "orange":
            self.pontuacao = 500
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 2))

        elif tipo_item == "apple":
            self.pontuacao = 700
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 3))

        elif tipo_item == "melon":
            self.pontuacao = 1000
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 4))

        elif tipo_item == "galaxy boss":
            self.pontuacao = 2000
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 5))

        elif tipo_item == "bell":
            self.pontuacao = 3000
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 6))

        elif tipo_item == "key":
            self.pontuacao = 5000
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 7))

        elif tipo_item == "pacdot":
            self.pontuacao = 10
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 8))

        elif tipo_item == "powerpill":
            self.pontuacao = 50
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 9))

        elif tipo_item == "wall": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 10))


    def bounding_box(self):
        return Rect(self.movimento.posicao, self.sprite.sprite_size)