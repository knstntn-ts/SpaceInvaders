from turtle import Turtle


class Invader(Turtle):
    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.xmove = 2
        self.center_x = self.xcor()

    def move(self):
        # if traveled distance is more than 50 change the sign
        if abs(self.center_x - self.xcor()) == 50:
            self.xmove = -1*self.xmove
            self.sety(self.ycor() - 25)

        self.setx(self.xcor() + self.xmove)









