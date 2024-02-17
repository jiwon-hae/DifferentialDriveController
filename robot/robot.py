import math

import pygame

from presentation.util import Utils


class Robot:
    def __init__(self, start_position, robot_img, width, wheel_radius):
        self.b = width
        self.r = wheel_radius
        self.x = start_position[0]
        self.y = start_position[1]

        # rotation angle of the robot
        self.theta = 0

        # ground contact speed of left and right wheel
        self.vl = Utils.meters2Pixel(0.01)
        self.vr = Utils.meters2Pixel(0.01)
        self.v = (self.vl + self.vr) / 2

        # angular velocity of left and right wheel
        self.w = 0
        self.wl = 0
        self.wr = 0

        self.max_speed = Utils.meters2Pixel(0.02)
        self.min_speed = Utils.meters2Pixel(-0.02)

        # graphics
        self.img = pygame.image.load(robot_img)
        self.rotated = self.img
        self.rect = self.rotated.get_rect(center=(self.x, self.y))

    def draw(self, map):
        map.blit(self.rotated, self.rect)

    def move(self, dt, event=None):
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

        self.x += ((self.vl + self.vr) / 2) * math.cos(self.theta) * dt
        self.y -= ((self.vl + self.vr) / 2) * math.sin(self.theta) * dt
        change_in_theta = (self.vr - self.vl) / self.b * dt
        self.theta += change_in_theta

        self.w = 0 if dt == 0 else change_in_theta / dt
        self.wl = (self.v - self.w * self.b / 2) / self.r
        self.wr = (self.v + self.w * self.b / 2) / self.r

        if self.theta > 2 * math.pi or self.theta < -2 * math.pi:
            self.theta = 0

        self.vr = max(self.min_speed, min(self.vr, self.max_speed))
        self.vl = max(self.min_speed, min(self.vl, self.max_speed))

        self.rotated = pygame.transform.rotozoom(self.img, math.degrees(self.theta), 1)
        self.rect = self.rotated.get_rect(center=(self.x, self.y))
