import random
import math


class GameLogic:
    
    def __init__(self, display):
        self.board: list[list[int, int, int], list[int, int, int], list[int, int, int]] = [[None for _ in range(0, 3)] for _ in range(0, 3)]
        self.display = display
        self.is_game: bool = True
        self.user_move = random.randint(0, 1)
        if self.user_move == 0:
            self.bot_move()
    
    def reset_game(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.is_game = True
        self.user_move = random.randint(0, 1)
        if self.user_move == 0:
            self.bot_move()

    def is_place_correct(self, pos: tuple[int, int]) -> bool:
        return True if self.board[pos[0]][pos[1]] is None else False

    def set_mark(self, pos: tuple[int, int], number: int):
        self.board[pos[0]][pos[1]] = number
        self.user_move = not self.user_move

        # check game
        if self.check_game() == True:
            self.is_game = False
            return

        # bot move
        if self.user_move == 0:
            self.bot_move()

    def check_game(self) -> bool:
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != None:
                return True

        for col in range(len(self.board[0])):
            if all(self.board[row][col] == self.board[0][col] and self.board[row][col] != None for row in range(len(self.board))):
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            return True

        return False

    # Minimax with Alpha-Beta Pruning
    def all_possible_moves(self) -> list:
        moves: list = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.is_place_correct((i, j)):
                    moves.append((i, j))
        
        return moves

    def minimax(self, depth, maximizing_player):
        all_moves = self.all_possible_moves()
        if(len(all_moves) == 0):
            return 0

        if maximizing_player:
            max_eval = -math.inf
            for move in all_moves:
                self.board[move[0]][move[1]] = 0
                eval = self.minimax(depth+1, False)
                self.board[move[0]][move[1]] = None
                max_eval = max(max_eval, eval)

            return max_eval            
        else:
            min_eval = math.inf
            for move in all_moves:
                self.board[move[0]][move[1]] = 1
                eval = self.minimax(depth+1, True)
                self.board[move[0]][move[1]] = None
                min_eval = min(min_eval, eval)

            return min_eval

    def find_best_move(self) -> tuple[int, int]:
        best_eval = -math.inf
        best_move: None|tuple = None

        for move in self.all_possible_moves():
            self.board[move[0]][move[1]] = 0
            eval = self.minimax(0, False)
            self.board[move[0]][move[1]] = None
            if eval > best_eval:
                best_eval = eval
                best_move = move

        return best_move
    # Minimax with Alpha-Beta Pruning

    def bot_move(self):
        bot_row, bot_col = self.find_best_move()
        self.display.draw_x((bot_row, bot_col))
        self.set_mark((bot_row, bot_col), 0)