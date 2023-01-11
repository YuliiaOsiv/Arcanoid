import pgzrun
from vector import Vector


class Circle:
    def __init__(self, vector: Vector):
        self.position = vector
        self.velocity = Vector(0, 0) # speed - scalar, velocity - vector
        self.acceleration = Vector(0, 0)


WIDTH = 800
HEIGHT = 800
RADIUS = 50

circle = Circle(Vector(200, 200))
gravity = Vector(0, 20)

def draw():
    screen.clear()
    screen.draw.circle((circle.position.x, circle.position.y), 50, "white")


def update(dt): # dt - time since last frame
    circle.acceleration += gravity
    circle.velocity += circle.acceleration
    v = circle.velocity
    circle.acceleration = Vector(0, 0)

    if circle.position.y >= HEIGHT - RADIUS and v.y > 0:
        circle.velocity = Vector(v.x, -v.y)
    circle.position += Vector(v.x * dt, v.y * dt)
    pass


pgzrun.go()