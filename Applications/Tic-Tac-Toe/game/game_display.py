import pygame
from . import SCREEN_HEIGHT, SCREEN_WIDTH
from game.game_logic import GameLogic


class GameDisplay:

    def __init__(self):
        pygame.init()

        self.SCREEN_HEIGHT: int = SCREEN_HEIGHT
        self.SCREEN_WIDTH: int = SCREEN_WIDTH
        self.SQUARE_SIZE: int = self.SCREEN_WIDTH // 3
        self.is_running: bool = True

        self.screen = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
        
        pygame.display.set_caption("Tic Tac Toe")
        self.screen.fill((255, 255, 255))

        # creating board
        self.create_board()

    def reset_board(self):
        self.screen.fill((255, 255, 255))
        self.create_board()
        pygame.display.update()

    def create_board(self):
        Y_MAX: int = self.SCREEN_HEIGHT // 3
        X_MAX: int = self.SCREEN_WIDTH // 3

        for i in range(1, 3):
            Y_COUNT: int = Y_MAX * i
            X_COUNT: int = X_MAX * i
            pygame.draw.line(self.screen, (0, 0, 0), (0, Y_COUNT), (self.SCREEN_WIDTH, Y_COUNT), 10)
            pygame.draw.line(self.screen, (0, 0, 0), (X_COUNT, 0), (X_COUNT, self.SCREEN_HEIGHT), 10)
        
        pygame.display.update()

    def draw_o(self, position: tuple[int, int]):
        CENTER: tuple[int, int] = (position[0] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2, position[1] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2)
        SIZE: int = self.SQUARE_SIZE
        pygame.draw.circle(self.screen, (0, 0, 0), CENTER, SIZE // 2, 5)

    def draw_x(self, position: tuple[int, int]):
        CENTER: tuple[int, int] = (position[0] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2, position[1] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2)
        HALF_SIZE: int = self.SQUARE_SIZE // 2
        pygame.draw.line(self.screen, (0, 0, 0), (CENTER[0] - HALF_SIZE, CENTER[1] - HALF_SIZE), (CENTER[0] + HALF_SIZE, CENTER[1] + HALF_SIZE), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (CENTER[0] + HALF_SIZE, CENTER[1] - HALF_SIZE), (CENTER[0] - HALF_SIZE, CENTER[1] + HALF_SIZE), 5)

    # get square position
    def get_square_position(self, pos: tuple[int, int]) -> tuple[int]:
        return pos[0] // self.SQUARE_SIZE, pos[1] // self.SQUARE_SIZE