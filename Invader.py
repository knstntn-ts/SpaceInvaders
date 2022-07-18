from turtle import Turtle


class Invader(Turtle):
    def __init__(self, position):
        # --- INITIALIZE INVADER (SINGLE) --- #
        super().__init__()
        self.goto(position)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        # Speed of moving in x direction
        self.xmove = 2
        self.center_x = self.xcor()

    def move(self):
        # Invaders move left to right, best way to keep track of that is to calculate the distance they traveled
        # and trigger the change of their direction if certain value is passed

        # If traveled distance is more than 50 change the sign (change direction) and move closer to ship (or earth ;) )
        if abs(self.center_x - self.xcor()) == 50:
            self.xmove = -1*self.xmove
            self.sety(self.ycor() - 25)

        self.setx(self.xcor() + self.xmove)









