from turtle import Turtle
import Bullet


class Ship(Turtle):
    def __init__(self, start_position):
        self.x_pointer_pos = 0
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        self.goto(start_position)
        # self.speed(100)
        self.bullet = None
        self.ymove = 10
        self.bullet_start = None

    def check_bullet(self):
        if self.bullet:
            self.move_bullet(self.bullet.ycor() + self.ymove)

    def shoot(self):
        if not self.bullet:
            self.bullet_start = self.xcor()
            self.bullet = Bullet.Bullet(self.bullet_start)

    def move_bullet(self, new_y):
        self.bullet.sety(new_y)

        if new_y > 250:
            self.bullet.reset()
            self.bullet = None
        # self.bullet.goto((self.bullet_start, new_y))

    def go_left(self):
        if self.xcor() > - 300:
            self.setx(self.xcor() - 20)

    def go_right(self):
        if self.xcor() < 300:
            self.setx(self.xcor() + 20)