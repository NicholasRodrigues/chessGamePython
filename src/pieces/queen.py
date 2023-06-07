from src.piece import Piece


class Queen(Piece):

    def __init__(self, color=None):
        super().__init__(name='queen', color=color, value=9.0, texture=None, texture_rectangle=None)
