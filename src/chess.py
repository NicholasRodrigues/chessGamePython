import pygame as pygame


class ChessGame:
    def __init__(self):
        self.board = Board()
        self.current_player = "white"

    def verify_check_mate(self):
        return self.board.is_check_mate()

    def play(self):
        while not self.verificar_xeque_mate():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return