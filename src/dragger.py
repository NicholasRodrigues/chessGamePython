import pygame

from const import *


class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_column = 0

    # blit method
    def update_blit(self, screen):
        # texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # img
        img = pygame.image.load(texture)
        # rectangle
        img_center = self.mouseX, self.mouseY
        self.piece.texture_rectangle = img.get_rect(center=img_center)
        # blit
        screen.blit(img, self.piece.texture_rectangle)

    # update methods
    def update_mouse(self, position):
        self.mouseX, self.mouseY = position

    def save_initial(self, position):
        self.initial_row = position[1] // SQUARE_SIZE
        self.initial_column = position[0] // SQUARE_SIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
