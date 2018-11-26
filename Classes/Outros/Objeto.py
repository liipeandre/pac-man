from Libraries import Rect
from Classes.Outros.GameComponent import GameComponent

class Objeto(GameComponent):
    """Classe que representa os elementos fixos do jogo (itens e a parede)."""
    def __init__(self, posicao: list, tipo_item: str):
        # adiciona o tipo do item
        self.item = tipo_item

        # cria o item e/ou parede, conforme o tipo passado.
        # chama o construtor base, passando parâmetros exclusivo para cada tipo de objeto.
        if tipo_item == "cherry":
            self.pontuacao = 100
            super().__init__(posicao, "Items.bmp", (0, 0))
        
        elif tipo_item == "strawberry":
            self.pontuacao = 300
            super().__init__(posicao, "Items.bmp", (1, 0))

        elif tipo_item == "orange": 
            self.pontuacao = 500
            super().__init__(posicao, "Items.bmp", (2, 0))

        elif tipo_item == "apple": 
            self.pontuacao = 700
            super().__init__(posicao, "Items.bmp", (3, 0))

        elif tipo_item == "melon": 
            self.pontuacao = 1000
            super().__init__(posicao, "Items.bmp", (4, 0))

        elif tipo_item == "galaxy boss": 
            self.pontuacao = 2000
            super().__init__(posicao, "Items.bmp", (5, 0))

        elif tipo_item == "bell":
            self.pontuacao = 3000
            super().__init__(posicao, "Items.bmp", (6, 0))

        elif tipo_item == "key": 
            self.pontuacao = 5000
            super().__init__(posicao, "Items.bmp", (7, 0))

        elif tipo_item == "pacdot": 
            self.pontuacao = 10
            super().__init__(posicao, "Items.bmp", (8, 0))

        elif tipo_item == "powerpill": 
            self.pontuacao = 50
            super().__init__(posicao, "Items.bmp", (9, 0))

        elif tipo_item == "wall": 
            super().__init__(posicao, "Items.bmp", (10, 0))

    def __str__(self):
        return f"{str(self.movimento.posicao[0])};{str(self.movimento.posicao[1])};{str(self.sprite.sprite_size[0])};{str(self.sprite.sprite_size[1])}"

    def tolist(self):
        return [self.movimento.posicao[0], self.movimento.posicao[1], self.sprite.sprite_size[0], self.sprite.sprite_size[1]]

    def bounding_box(self):
        return Rect(self.movimento.posicao, self.sprite.sprite_size)