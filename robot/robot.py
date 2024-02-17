import math

import pygame

from presentation.util import Utils


class Robot:
    def __init__(self, start_position, robot_img, width):
        self.w = width
        self.x = start_position[0]
        self.y = start_position[1]
        self.theta = 0
        self.vl = Utils.meters2Pixel(0.01)
        self.vr = Utils.meters2Pixel(0.01)
        self.max_speed = Utils.meters2Pixel(0.02)
        self.min_speed = Utils.meters2Pixel(0.02)

        # graphics
        self.img = pygame.image.load(robot_img)
        self.rotated = self.img
        self.rect = self.rotated.get_rect(center = (self.x, self.y))

    def draw(self, map):
        map.blit(self.rotated, self.rect)

    def move(self, dt, event = None, ):
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.vl += Utils.meters2Pixel(0.001)
                elif event.key == pygame.K_e:
                    self.vl -= Utils.meters2Pixel(0.001)
                elif event.key == pygame.K_a:
                    self.vr += Utils.meters2Pixel(0.001)
                elif event.key == pygame.K_d:
                    self.vr -= Utils.meters2Pixel(0.001)

        # differential drive control
        self.x += ((self.vl + self.vr) / 2) * math.cos(self.theta) * dt
        self.y -= ((self.vl + self.vr) / 2) * math.sin(self.theta) * dt
        self.theta += (self.vr - self.vl) / self.w * dt
        self.rotated = pygame.transform.rotozoom(self.img, math.degrees(self.theta), 1)
        self.rect = self.rotated.get_rect(center = (self.x, self.y))
