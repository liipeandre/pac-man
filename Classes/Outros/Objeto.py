from Classes.Outros.GameComponent import *

class Objeto(object, GameComponent):
    """Classe que representa os elementos fixos do jogo (itens e a parede)."""
    def __init__(self, posicao: list, tipo_item: str):

        # cria o item e/ou parede, conforme o tipo passado.
        # chama o construtor base, passando parâmetros exclusivo para cada tipo de objeto.
        if tipo_item == "cherry":
            self.pontuacao = 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 0))
        
        elif tipo_item == "strawberry": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 1))

        elif tipo_item == "orange": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 2))

        elif tipo_item == "apple": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 3))

        elif tipo_item == "melon": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 4))

        elif tipo_item == "galaxy boss": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 5))

        elif tipo_item == "bell": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 6))

        elif tipo_item == "key": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 7))

        elif tipo_item == "pacdot": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 8))

        elif tipo_item == "powerpill": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 9))

        elif tipo_item == "wall": 
            super(GameComponent, self).__init__(posicao, "Items.bmp", (0, 10))


    def bounding_box(self):
        return Rect(self.movimento.posicao, self.sprite.sprite_size)