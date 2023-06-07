from src.piece import Piece


class Bishop(Piece):

    def __init__(self, color=None):
        super().__init__(name='bishop', color=color, value=3.001, texture=None, texture_rectangle=None)
