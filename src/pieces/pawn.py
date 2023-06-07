from src.piece import Piece


class Pawn(Piece):

    def __init__(self, color=None):
        self.dir = -1 if color == 'white' else 1
        super().__init__(name='pawn', color=color, value=1.0, texture=None, texture_rectangle=None)
