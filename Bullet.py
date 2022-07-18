from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, ship_position_x):
        # --- INITIALIZE THE BULLET --- #
        super().__init__()
        self.shape('triangle')
        self.color("#800080")
        self.tilt(90)
        self.penup()
        self.goto((ship_position_x, -250))

