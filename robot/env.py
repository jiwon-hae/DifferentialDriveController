import pygame
import math

from presentation.colors import Color


class Environment:
    def __init__(self, dimension):
        self.width = dimension[0]
        self.height = dimension[1]

        pygame.display.set_caption("Differential Drive Robot")
        self.map = pygame.display.set_mode((self.width, self.height))

        self.font = pygame.font.Font("freesansbold.ttf", 40)
        self.text = self.font.render("default", True, Color.White.value, Color.Black.value)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (dimension[0]-800, dimension[1] - 100)
        self.trail_set = []

    def write_info(self, vl, vr, wl, wr, theta):
        txt = f"vl = {vl} vr = {vr} wl = {round(wl, 2)} wr = {round(wr, 2)} theta = {int(math.degrees(theta))}"
        self.text = self.font.render(txt, True, Color.White.value, Color.Black.value)
        self.map.blit(self.text, self.text_rect)

    def trail(self, pos):
        for i in range(0, len(self.trail_set) - 1):
            pygame.draw.line(self.map, Color.Yellow.value, (self.trail_set[i][0], self.trail_set[i][1]), (self.trail_set[i+1][0], self.trail_set[i+1][1]))

        if self.trail_set.__sizeof__() > 30000:
            self.trail_set.pop(0)

        self.trail_set.append(pos)

    def robot_frame(self, pos, rotation):
        n = 80
        center_x, center_y = pos
        x_axis = (center_x + n * math.cos(-rotation), center_y + n*math.sin(-rotation))
        y_axis = (center_x + n * math.cos(-rotation + math.pi / 2), center_y + n*math.sin(-rotation + math.pi/2))
        pygame.draw.line(self.map, Color.Red.value, (center_x, center_y), x_axis, 3)
        pygame.draw.line(self.map, Color.Green.value, (center_x, center_y), y_axis, 3)
