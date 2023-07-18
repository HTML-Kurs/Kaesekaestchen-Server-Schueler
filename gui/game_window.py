import pygame, sys
from pygame.locals import *

from game import GameState, Player

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
L_GREY = (178, 178, 178)
D_GREY = (78, 78, 78)

pygame.init()

FONT = pygame.font.SysFont('Comic Sans MS', 20)
FONT2 = pygame.font.SysFont('Comic Sans MS', 13)
field_size = 40
padding = 5
wall_width = 10
padding_top = 100

def create_window(state:GameState, s1, s2, keep_open=False):
    global DISPLAY
    pygame.init()
    global FONT
    global FONT2
    global width
    FONT = pygame.font.SysFont('Comic Sans MS', 30)
    FONT2 = pygame.font.SysFont('Comic Sans MS', 13)
    width = field_size * state.size + (padding * 2 + wall_width) * (state.size + 1)
    height = width + padding_top
    DISPLAY = pygame.display.set_mode((width, height), 0, 32)
    k = True
    while k  and (state.get_winner() is None or keep_open):
        k = k and update_board(state, s1, s2)
    print("__________________________________________-")

def get_color(owner:Player, default:(int, int, int)):
    if owner is None:
        return default
    return owner.color

def update_board(state:GameState, s1, s2):
    global DISPLAY
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            return False

    DISPLAY.fill(WHITE)
    if s1 == 0:
        text_surface = FONT.render(f'{state.player1.score} - {state.player2.score}', False, BLACK)
        rect = text_surface.get_rect(center=(width // 2, 50))
        DISPLAY.blit(text_surface, rect)
    else:
        text_surface = FONT.render(f'{s1} - {s2}', False, BLACK)
        rect = text_surface.get_rect(center=(width // 2, 50))
        DISPLAY.blit(text_surface, rect)

        text_surface = FONT.render(f'{state.player1.score} - {state.player2.score}', False, BLACK)
        rect = text_surface.get_rect(center=(width // 2, 80))
        DISPLAY.blit(text_surface, rect)

    text_surface = FONT2.render(f'{state.player1.name} - {state.player2.name}', False, D_GREY)
    rect = text_surface.get_rect(center=(width // 2, 20))
    DISPLAY.blit(text_surface, rect)

    for r in state.fields:
        for field in r:
            color = get_color(field.owner, L_GREY)
            x_cord = (2 * padding + wall_width) * (1 + field.x) + (field_size) * field.x
            y_cord = (2 * padding + wall_width) * (1 + field.y) + (field_size) * field.y + padding_top
            pygame.draw.rect(DISPLAY, color, pygame.Rect(x_cord, y_cord, field_size, field_size))

    for r in state.hor_lines:
        for line in r:
            color = get_color(line.owner, D_GREY)
            x_cord = (padding + wall_width) * (1 + line.x) + (padding + field_size) * line.x  + padding
            y_cord = (padding) * (1 + line.y) + (padding + field_size + wall_width) * line.y + padding_top
            pygame.draw.rect(DISPLAY, color, pygame.Rect(x_cord, y_cord,  field_size, wall_width))

    for r in state.ver_lines:
        for line in r:
            color = get_color(line.owner, D_GREY)
            x_cord = (padding) * (1 + line.x) + (field_size + wall_width + padding) * line.x
            y_cord = (padding+ wall_width) * (1 + line.y) + (padding + field_size) * line.y + padding_top + padding
            pygame.draw.rect(DISPLAY, color, pygame.Rect(x_cord, y_cord, wall_width,  field_size))

    pygame.display.update()
    return True
