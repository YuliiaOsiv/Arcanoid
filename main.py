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
        self.actor.draw(

class Ball:
    def __init__(self, speed: int):
        self.actor = Actor('cookie.png', center=(WIDTH // 2, HEIGHT//2))
        self.speed = speed
        self.ball_x = self.speed
        self.ball_y = self.speed
        self.radius = 25 #радіус, щоб знайти, чи перетнулась кулька з перешкодою

    def update(self):
        self.actor.x += self.ball_x
        self.actor.y += self.ball_y # зміна координат кульки 60 разів на секунду

        if not (0 <= ball.actor.x <= WIDTH): # відбивання від стінок
            self.ball_x *= -1

        if not (0 <= ball.actor.y <= HEIGHT): # відбивання від верхньої грані
            self.ball_y *= -1

        if ball.actor.y == HEIGHT: # якщо мʼячик падає, то забирається одне сердечко
            global hearts_alive
            global loss
            hearts_alive.pop(len(hearts_alive)-1) # кількість сердечок зменшується на одне
            if len(hearts_alive) == 0:
                loss = True
            self.actor.y = HEIGHT // 2 # мʼячик падає з середини екрану
            self.actor.x = WIDTH // 2

    def hits(self):
        ball.ball_y *= -1 # якщо мʼячик вдаряється, то він відбивається
        if random.randint(0, 1):
            ball.ball_x *= 1
        else:
            ball.ball_x = -1

    def draw(self):
        self.actor.draw()

class Heart:
    def __init__(self, x):
        self.actor = Actor('heart.png', center=(20+25*x, 30))

    def draw(self):
        self.actor.draw()


class HeartBonusLife:
    def __init__(self, x, y, generate_time: int):
        self.actor = Actor('heart.png', center=(x, y))
        self.last = pygame.time.get_ticks() # бонусні сердечка випадають через деякий час, але програма паралельно також працює
        self.cooldown = generate_time * 1000 # час, через який випадають бонусні сердечка
        self.hide = True

    def draw(self):
        self.actor.draw()

    def update(self):
        global hearts_alive # змінні global не виходять за рамки класу
        if not self.hide:
            self.actor.y += 5 # швидкість, з якою летить бонусне сердечко

        if self.actor.colliderect(paddle.actor):
            hearts_alive.append(Heart(len(hearts_alive)))
            self.actor.pos = (-10, -10)
            self.hide = True

        # if self.actor.y > HEIGHT + 20:
        #     self.actor.pos = (-10, -10)
        #     self.hide = True

        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            self.hide = False # якщо час, який пройшов, більший, ніж час, який сердечко чекає, то воно падає
            self.actor.pos = (random.randint(10, WIDTH - 10), 0)