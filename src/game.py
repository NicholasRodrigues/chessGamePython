import pygame

from const import *
from board import Board
from src.dragger import Dragger


class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    # Show methods

    def show_bg(self, surface):
        for row in range(ROWS):
            for column in range(COLS):
                rect = (column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                if (row + column) % 2 == 0:
                    light_green_color = (234, 235, 200)

                    pygame.draw.rect(surface, light_green_color, rect)
                else:
                    dark_green_color = (118, 150, 86)

                    pygame.draw.rect(surface, dark_green_color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for column in range(COLS):
                # There is a piece?
                if self.board.squares[row][column].has_piece():
                    piece = self.board.squares[row][column].piece

                    # all pieces except dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2
                        piece.texture_rectangle = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rectangle)