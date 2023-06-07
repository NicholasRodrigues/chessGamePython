from const import *
from square import Square
from piece import Piece

from src.pieces.knight import Knight
from src.pieces.bishop import Bishop
from src.pieces.rook import Rook
from src.pieces.queen import Queen
from src.pieces.king import King
from src.pieces.pawn import Pawn


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for column in range(COLS)]
        self._create_board()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create_board(self):
        for row in range(ROWS):
            for column in range(COLS):
                self.squares[row][column] = Square(row, column)

    def _add_pieces(self, color):
        (row_pawn, row_other_pieces) = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for column in range(COLS):
            self.squares[row_pawn][column] = Square(row_pawn, column, Pawn(color))


        # knights
        self.squares[row_other_pieces][1] = Square(row_other_pieces, 1, Knight(color))
        self.squares[row_other_pieces][6] = Square(row_other_pieces, 6, Knight(color))

        # bishops
        self.squares[row_other_pieces][2] = Square(row_other_pieces, 2, Bishop(color))
        self.squares[row_other_pieces][5] = Square(row_other_pieces, 5, Bishop(color))

        # rooks
        self.squares[row_other_pieces][0] = Square(row_other_pieces, 0, Rook(color))
        self.squares[row_other_pieces][7] = Square(row_other_pieces, 7, Rook(color))

        if color == 'black':
            # queen
            self.squares[row_other_pieces][4] = Square(row_other_pieces, 4, Queen(color))

            # king
            self.squares[row_other_pieces][3] = Square(row_other_pieces, 3, King(color))
        else:
            # queen
            self.squares[row_other_pieces][3] = Square(row_other_pieces, 3, Queen(color))

            # king
            self.squares[row_other_pieces][4] = Square(row_other_pieces, 4, King(color))
