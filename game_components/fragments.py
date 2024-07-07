import pygame
import random

class Fragments:
    def __init__(self):
        self.pieces = []
        self.fragment_time = 0
        self.is_active = False

    def create_pieces(self, player_x, player_y):
        self.pieces = []
        for _ in range(20):
            piece_x = player_x + random.randint(-10, 10)
            piece_y = player_y + random.randint(-10, 10)
            piece_dx = random.choice([-1, 1]) * random.random() * 5
            piece_dy = random.choice([-1, 1]) * random.random() * 5
            self.pieces.append([piece_x, piece_y, piece_dx, piece_dy])
        self.fragment_time = pygame.time.get_ticks()
        self.is_active = True

    def update_and_draw(self, screen):
        player_color = (255, 0, 0)
        for piece in self.pieces:
            piece[0] += piece[2]
            piece[1] += piece[3]
            pygame.draw.rect(screen, player_color, (piece[0], piece[1], 5, 5))

        if pygame.time.get_ticks() - self.fragment_time > 1000:
            self.pieces = []
            self.is_active = False
