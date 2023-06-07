from src.piece import Piece


class Knight(Piece):

    def __init__(self, color=None):
        super().__init__(name='knight', color=color, value=3.0, texture=None, texture_rectangle=None)
