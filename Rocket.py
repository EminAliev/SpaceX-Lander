import time


class Rocket:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.color = color
        self.acceleration = False  # ускорение
        self.startAcceleration = time.time()
        self.fuel = 1000
        self.speed = speed
