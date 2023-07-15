import pygame, sys
from pygame.locals import *

from game import GameState

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
L_GREY = (178, 178, 178)
D_GREY = (78, 78, 78)

FONT = pygame.font.SysFont('Comic Sans MS', 30)

field_size = 40
padding = 5
wall_width = 10
padding_top = 50

def create_window(state:GameState):
    global DISPLAY

    pygame.init()

    width = field_size * state.size + (padding + wall_width) * (state.size + 2)
    height = width + padding_top
    DISPLAY = pygame.display.set_mode((width, height), 0, 32)


def update_board(state:GameState):
    global DISPLAY
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAY.fill(WHITE)

    text_surface = FONT.render(f'{state.player1.score} - {state.player2.score}', False, BLACK)
    DISPLAY.blit(text_surface, (200, 0))

    for r in state.fields:
        for field in r:
            color = field.owner.color if field.owner is None else L_GREY
            x_cord = (padding + wall_width) * (1 + field.x) + field_size * field.x
            y_cord = (padding + wall_width) * (1 + field.y) + field_size * field.y + padding_top
            pygame.draw.rect(DISPLAY, color, x_cord, y_cord, field_size, field_size)

    for r in state.hor_lines:
        for line in r:
            color = line.owner.color if line.owner is None else D_GREY
            x_cord = (padding) * (1 + line.x) + (field_size + wall_width) * line.x
            y_cord = (padding) * (1 + line.y) + (field_size + wall_width) * line.y + padding_top
            pygame.draw.rect(DISPLAY, color, x_cord, y_cord, field_size, wall_width)

    for r in state.ver_lines:
        for line in r:
            color = line.owner.color if line.owner is None else D_GREY
            x_cord = (padding) * (1 + line.x) + (field_size + wall_width) * line.x
            y_cord = (padding) * (1 + line.y) + (field_size + wall_width) * line.y + padding_top
            pygame.draw.rect(DISPLAY, color, x_cord, y_cord, wall_width, field_size)

    pygame.display.update()
