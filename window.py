import pygame
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 624, 720


class Window:
    def __init__(self, arr_renderer):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Visualizer')
        self.arr_renderer = arr_renderer

    def update_window(self):
        self.screen.fill((0, 0, 0))
        i = 0
        mult = 2
        for index, elem in enumerate(self.arr_renderer.arr):
            pygame.draw.rect(self.screen, (255, 255, 255), (index * mult, WINDOW_HEIGHT - elem, mult, elem))
        time.sleep(0.01)
        pygame.display.update()
