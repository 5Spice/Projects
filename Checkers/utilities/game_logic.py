import pygame
from .constants import RED, WHITE, GREEN, SQUARE_SIZE
from utilities.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
         
    def update(self):
        self.board.draw(self.win)
        self.draw_possible_moves(self.possible_moves)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.possible_moves = {}
    
    def winner(self):
        return self.board.winner()
     
    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_pieces(row, col)
        if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.possible_moves = self.board.get_possible_moves(piece)
                return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_pieces(row, col)
        if self.selected and piece == 0 and (row, col) in self.possible_moves:    #checks if the move is possible (within boundaries, selected, and not occupied)
            self.board.move(self.selected, row, col)
            skipped = self.possible_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True

    def draw_possible_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2 , row * SQUARE_SIZE + SQUARE_SIZE//2), 40)

    def change_turn(self):
        self.possible_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
    
    def get_board(self):
        return self.board
    
    def ai_move(self, board):
        self.board = board
        self.change_turn()