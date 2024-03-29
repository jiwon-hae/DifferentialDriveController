import pygame
from presentation.colors import *
from presentation.util import Utils

from robot.env import Environment
from robot.robot import Robot

if __name__ == "__main__":
    pygame.init()
    start = (200, 200)
    dims = (1200, 600)
    running = True
    dt = 0
    last_time = pygame.time.get_ticks()

    env = Environment(dims)
    robot = Robot(start, "./assets/DDR.png", Utils.meters2Pixel(0.01), Utils.meters2Pixel(0.001))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            robot.move(dt, event)

        dt = (pygame.time.get_ticks() - last_time) / 1000
        last_time = pygame.time.get_ticks()
        pygame.display.update()
        env.map.fill(Color.Black.value)
        env.write_info(int(robot.vl), int(robot.vr), robot.wl, robot.wr, robot.theta)
        env.trail((robot.x, robot.y))
        env.robot_frame((robot.x, robot.y), robot.theta)

        robot.move(dt)
        robot.draw(env.map)
