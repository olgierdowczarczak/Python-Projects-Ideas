import pygame
from .game_display import GameDisplay
from .game_logic import GameLogic


class Game:

    def __init__(self):
        self.display = GameDisplay()
        self.logic = GameLogic(self.display)

    def run_game(self):

        while self.display.is_running is True:

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT: # EXIT BUTTON
                    self.display.is_running = False
                elif pygame.key.get_pressed()[pygame.K_r]: # R KEY PRESSED TO RESET
                    self.display.reset_board()
                    self.logic.reset_game()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # BUTTON CLICK
                    if self.logic.user_move == 1: # IS USER MOVE
                        user_row, user_col = self.display.get_square_position(pygame.mouse.get_pos())
                        if self.logic.is_place_correct((user_row, user_col)):
                            self.display.draw_o((user_row, user_col))
                            self.logic.set_mark((user_row, user_col), 1)

                    if self.logic.is_game == False:
                        self.display.reset_board()
                        self.logic.reset_game()

            pygame.display.update()