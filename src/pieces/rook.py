from src.piece import Piece


class Rook(Piece):

    def __init__(self, color=None):
        super().__init__(name='rook', color=color, value=5.0, texture=None, texture_rectangle=None)
