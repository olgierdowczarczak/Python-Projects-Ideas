import pygame
import random


class GameLogic:
    
    def __init__(self):
        self.direction: str = "RIGHT"

    def move_snake(self, snake_body: list, head_position: tuple[int, int], move: int):
        move_x: int = 0
        move_y: int = 0

        if self.direction == "RIGHT":
            move_x += move
        elif self.direction == "UP":
            move_y -= move
        elif self.direction == "LEFT":
            move_x -= move
        elif self.direction == "DOWN":
            move_y += move

        last_x: int = 0
        last_y: int = 0
        for i in range(len(snake_body) - 1, 0, -1):
            last_x = snake_body[i - 1].x
            last_y = snake_body[i - 1].y
            snake_body[i].x = last_x
            snake_body[i].y = last_y
            
        snake_body[0].x += move_x
        snake_body[0].y += move_y

        return head_position[0] + move_x, head_position[1] + move_y

    def is_touch_wall(self, head_position: tuple[int, int], max_width: int, max_hight: int):
        return True if head_position[0] < 0 or head_position[0] > max_width or head_position[1] < 0 or head_position[1] > max_hight else False

    def is_touch_point(self, head_position: tuple[int, int], point_position: tuple[int, int]):
        return True if head_position[0] == point_position[0] and head_position[1] == point_position[1] else False

    def get_position_for_point(self, snake_body: list, board_cols: int, move: int) -> tuple:
        if len(snake_body) == board_cols ** 2:
            return -50, -50

        blocked_points: list = []
        for body in snake_body:
            blocked_points.append([body.x, body.y])

        is_searching: bool = True
        while is_searching:
            random_x: int = random.randint(0, board_cols - 1) * move
            random_y: int = random.randint(0, board_cols - 1) * move
            
            if not [random_x, random_y] in blocked_points:
                return (random_x, random_y)