import pygame
from utilities.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from utilities.game_logic import Game
from minimax.algorithm import minimax

FPS = 60

pygame.display.set_caption("Checkers")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def cursor_location(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True 
    clock = pygame.time.Clock() #limit by FPS instead of processing speed
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False
             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = cursor_location(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()