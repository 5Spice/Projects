import pygame 
from .constants import TAN, BROWN, ROWS, COLUMNS, WHITE, RED, SQUARE_SIZE
from .pieces import Piece

class Board:
    def __init__(self):
        self.board = []
        #remaining pieces
        self.red_left = self.white_left = 12    
        self.red_kings = self.white_kings = 0
        self.create_board()

    def create_squares(self, window):
        window.fill(TAN)
        for row in range(ROWS):
            for col in range( row % 2, COLUMNS, 2):
                pygame.draw.rect(window, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self,color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        #king converter
        if row == ROWS - 1 or row == 0:
            piece.create_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_pieces(self,row, col):
        return self.board[row][col]   

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLUMNS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    


    def draw(self, window):
        self.create_squares(window)
        for row in range(ROWS):
            for col in range(COLUMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)
    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0    
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def get_possible_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))

        return moves


#Multiple jump combos diagonal left
    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = []
        for i in range (start , stop, step):
            if left < 0:
                break

            current = self.board[i][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves [(i, left)] = last + skipped
                else:
                    moves[(i, left)] = last
                if last:
                    if step == -1:
                        row = max(i-3, 0)
                    else:
                        row = min(i+3, ROWS)
                    moves.update(self._traverse_left(i+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(i+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            
            left -= 1
        
        return moves


#Multiple jumps combo diagonal right
    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        for i in range(start, stop, step):
            if right >= COLUMNS:
                break
            
            current = self.board[i][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(i,right)] = last + skipped
                else:
                    moves[(i, right)] = last
                
                if last:
                    if step == -1:
                        row = max(i-3, 0)
                    else:
                        row = min(i+3, ROWS)
                    moves.update(self._traverse_left(i+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(i+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves