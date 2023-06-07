from src.piece import Piece


class King(Piece):

    def __init__(self, color=None):
        super().__init__(name='king', color=color, value=10000.0, texture=None, texture_rectangle=None)
