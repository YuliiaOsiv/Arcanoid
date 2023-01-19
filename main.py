import pgzrun
import random
from pgzero.actor import Actor
import pygame

WIDTH = 600
HEIGHT = 800
COLORS = {'red': 1, 'pink': 2, 'beige': 3, 'purple': 4}


class Paddle:

    def __init__(self):
        self.actor = Actor('paddle.png', center=(WIDTH // 2, HEIGHT - 100))

    def update(self, ball):
        if self.actor.colliderect(ball.actor):
            ball.ball_y *= -1
            if random.randint(0, 1):
                ball.ball_x *= 1
            else:
                ball.ball_x = -1

    def draw(self):
        self.actor.draw()