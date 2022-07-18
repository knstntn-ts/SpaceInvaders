from turtle import Turtle
import Bullet


class Ship(Turtle):
    def __init__(self, start_position):
        # --- INITIALIZE THE SHIP --- #
        self.x_pointer_pos = 0
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        self.goto(start_position)

        # Variable for bullet
        self.bullet = None
        # variable for moving speed of the bullet
        self.ymove = 10
        # variable for initial position of the bullet
        self.bullet_start = None

    def check_bullet(self):
        # If the ship fired the bullet, move it
        if self.bullet:
            self.move_bullet(self.bullet.ycor() + self.ymove)

    def shoot(self):
        # If there is no current fired bullet, initiate new one with the x-coordinates of the ship
        if not self.bullet:
            self.bullet_start = self.xcor()
            self.bullet = Bullet.Bullet(self.bullet_start)

    def move_bullet(self, new_y):
        self.bullet.sety(new_y)

        # If the bullet moves out of the screen, remove it
        if new_y > 250:
            self.bullet.reset()
            self.bullet = None

    # Functions to move ship left and right
    def go_left(self):
        if self.xcor() > - 300:
            self.setx(self.xcor() - 20)

    def go_right(self):
        if self.xcor() < 300:
            self.setx(self.xcor() + 20)