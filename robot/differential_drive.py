import pygame
import math

from presentation.colors import Color


class Environment:
    def __init__(self, dimension):
        self.width = dimension[0]
        self.height = dimension[1]

        pygame.display.set_caption("Differential Drive Robot")
        self.map = pygame.display.set_mode((self.width, self.height))

        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.text = self.font.render("default", True, Color.White.value, Color.Black.value)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (dimension[0]- 600, dimension[1] - 100)

    def write_info(self, vl, vr, theta):
        txt = f"vl = {vl} vr = {vr} theta = {int(math.degrees(theta))}"
        self.text = self.font.render(txt, True, Color.White.value, Color.Black.value)
        self.map.blit(self.text, self.text_rect)