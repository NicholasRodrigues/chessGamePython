import os


class Piece:
    def __init__(self, name, color, value, texture, texture_rectangle=None):
        self.name = name
        self.color = color
        self.valid_moves = []
        self.moved = False
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.texture = texture
        self.set_texture()
        self.texture_rectangle = texture_rectangle

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )

    def add_valid_moves(self, move):
        self.valid_moves.append(move)
