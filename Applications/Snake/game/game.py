import pygame
from game.game_display import GameDisplay
from game.game_logic import GameLogic


class Game:
    
    def __init__(self):
        pygame.init()

        self.display = GameDisplay()
        self.logic = GameLogic()
        self.is_game: bool = True
        self.snake_head_x: int = 0
        self.snake_head_y: int = 0
        self.snake: list = self.display.create_snake((self.snake_head_x, self.snake_head_y))
        self.point = None
        self.last_point_position: tuple[int, int] = None
        self.user_points: int = 0

    def run_game(self):
        
        while self.is_game:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # QUIT BUTTON
                    self.is_game = False
                    return False
                else:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_a] and self.logic.direction != "RIGHT":
                        self.logic.direction = "LEFT"
                    elif key[pygame.K_w] and self.logic.direction != "DOWN":
                        self.logic.direction = "UP"
                    elif key[pygame.K_d] and self.logic.direction != "LEFT":
                        self.logic.direction = "RIGHT"
                    elif key[pygame.K_s] and self.logic.direction != "UP":
                        self.logic.direction = "DOWN"
                    elif key[pygame.K_r]: # R BUTTON, RESTART GAME
                        self.is_game = False
                        return True

            self.display.screen.fill((0, 0, 0))
            #self.display.create_board()

            self.snake_head_x, self.snake_head_y = self.logic.move_snake(self.snake, (self.snake_head_x, self.snake_head_y), self.display.SQUARE_X)
            if self.last_point_position is not None:
                self.snake.append(pygame.Rect(self.last_point_position[0], self.last_point_position[1], self.display.SQUARE_X, self.display.SQUARE_X))
                self.last_point_position = None
            self.display.write_snake(self.snake)

            if self.point is None: 
                x, y = self.logic.get_position_for_point(self.snake, self.display.COLUMNS, self.display.SQUARE_X)
                self.point = self.display.create_point((x, y))
            self.display.write_point(self.point)

            if self.point and self.logic.is_touch_point((self.snake_head_x, self.snake_head_y), (self.point.x, self.point.y)):
                self.last_point_position = (self.point.x, self.point.y)
                self.point = None
                self.user_points += 1
                pygame.display.set_caption(f"Snake {self.user_points}/{self.display.COLUMNS ** 2 - 1}")

            if self.logic.is_touch_wall((self.snake_head_x, self.snake_head_y), self.display.SCREEN_WIDTH, self.display.SCREEN_HEIGHT) is True:
                self.is_game = False
                return True

            pygame.display.update() 
            pygame.time.Clock().tick(15)
        
        return True