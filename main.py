import pygame
from checkers.constants import *
from checkers.game import Game
from checkers.algorithm import minimax

FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game')

def get_position_mouse(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def display_winner(window, winner):
    font = pygame.font.Font(None, 50)
    color_name = get_color(winner)
    text = font.render(f'{color_name} igrač je pobedio!', True, (255, 255, 255))
    window.fill((14, 114, 37))
    window.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.flip()
    pygame.time.delay(10000)

def main():
    pygame.init()
    pygame.font.init()
    run = True
    clock = pygame.time.Clock()
    game = Game(window)
    game.update_board()

    while run:
        clock.tick(FPS)

        if game.turn == BLACK:
            value, new_board = minimax(game.get_board(), 4, True, game)
            game.computer_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = get_position_mouse(position)
                game.select_piece(row, col)

        if game.game_over:
            win = game.get_winner()
            display_winner(window, win)
            run = False
            continue

        game.update_board()

    pygame.quit()

if __name__ == "__main__":
    main()