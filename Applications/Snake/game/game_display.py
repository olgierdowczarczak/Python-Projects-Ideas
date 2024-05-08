import pygame
from . import *


class GameDisplay:
    
    def __init__(self):

        self.SCREEN_HEIGHT: int = HEIGHT
        self.SCREEN_WIDTH: int = WIDTH
        self.SQUARE_X: int = 50
        self.COLUMNS: int = self.SCREEN_WIDTH // self.SQUARE_X
        self.SQUARE_SIZE: int = self.SCREEN_WIDTH // self.COLUMNS
        self.screen = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
        
        pygame.display.set_caption(f"Snake 0/{self.COLUMNS ** 2 - 1}")
    
    def create_board(self):
        place: int = 0
        for i in range(1, self.COLUMNS + 1):
            place = i * self.SQUARE_X
            pygame.draw.line(self.screen, (255, 255, 255), (place, 0), (place, self.SCREEN_HEIGHT), 1)
            pygame.draw.line(self.screen, (255, 255, 255), (0, place), (self.SCREEN_WIDTH, place), 1)

    def create_snake(self, position: tuple[int, int]) -> list:
        snake:list = []
        snake.append(pygame.Rect(position[0], position[1], self.SQUARE_X, self.SQUARE_X))
        return snake

    def create_point(self, position: tuple[int, int]):
        return pygame.Rect(position[0], position[1], self.SQUARE_X, self.SQUARE_X)

    def write_snake(self, snake_body: list):
        for body in snake_body:
            pygame.draw.rect(self.screen, (0, 255, 0), body)

    def write_point(self, point):
        pygame.draw.rect(self.screen, (0, 0, 255), point)