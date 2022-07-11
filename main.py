from turtle import Screen, Turtle
import Invader
import Bullet
import Ship
import time

# score variable
score = 0
# lives
lives = 3

# Initialization
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Space Invaders")
screen.tracer(0)

game_is_on = True

# Initialization of game elements
ship = Ship.Ship((0, -250))
# my_ball = Ball.Ball()
# put the invaders on the screen
invaders = {}
cnt = 0
for j in range(3):
    for i in range(6):
        invaders.update({cnt: Invader.Invader([i * 100 - 250, 75 + j * 75])})
        cnt += 1

# Displays the score
sketch = Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Score: {}.".format(score), align="center", font=("Courier", 24, "normal"))

screen.listen()
screen.onkey(ship.go_right, "Right")
screen.onkey(ship.go_left, "Left")
screen.onkey(ship.shoot, 'space')


# margin for detecting collisions with bricks and paddle
margin_x = 50


while game_is_on:
    time.sleep(0.01)
    screen.update()
    ship.check_bullet()
    for i in invaders.keys():

        if invaders.get(i):
            invaders[i].move()
            # check if it is game over, case when invaders reached the ship
            if invaders[i].ycor() < -250:
                sketch.clear()
                sketch.goto(0, 0)
                sketch.write("You died!", align="center", font=("Courier", 35, "normal"))
            # check if the invader is hit by a bullet
            if ship.bullet:
                if invaders[i].ycor() + 10 > ship.bullet.ycor() > invaders[i].ycor() - 10 and \
                                        invaders[i].xcor()+margin_x > ship.bullet.xcor() > invaders[i].xcor()-margin_x:
                    score += 1
                    sketch.clear()
                    sketch.write("Score: {}.".format(score), align="center", font=("Courier", 24, "normal"))
                    invaders[i].reset() # to remove the invader
                    invaders.pop(i) # pop from the dictionary
                    ship.bullet.reset()
                    ship.bullet = None
                    break # to exit for loop, otherwise gives an error that dictionary changed during iteration
    if score == 18:
        sketch.clear()
        sketch.goto(0,0)
        sketch.write("You won!", align="center", font=("Courier", 35, "normal"))
#     ### Collisions with the walls
#     # Detect collision with the side walls
#     if my_ball.xcor() > 380 or my_ball.xcor() < -380:
#         my_ball.xbounce()
#     # Detect collision with the upper wall
#     if my_ball.ycor() > 280:
#         my_ball.ybounce()
#     # Detect collision with the bottom wall
#     if my_ball.ycor() < -290:
#         lives -= 1
#         my_ball.reset_position()
#         sketch.clear()
#         sketch.write("Score: {}. Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
#         if lives == 0:
#             game_is_on = False
#
#     # Detect collision with the paddle
#     if -240 > my_ball.ycor() > -250 and paddle.xcor()+margin_x > my_ball.xcor() > paddle.xcor()-margin_x:
#         my_ball.sety(paddle.ycor()+20)
#         my_ball.ybounce()
#
#     # Detect collision with bricks
#     for i in bricks.keys():
#         if bricks.get(i):
#             if bricks[i].ycor()+10 > my_ball.ycor() > bricks[i].ycor()-10 and \
#                     bricks[i].xcor()+margin_x > my_ball.xcor() > bricks[i].xcor()-margin_x:
#                 score += 1
#                 sketch.clear()
#                 sketch.write("Score: {}. Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
#                 my_ball.sety(bricks[i].ycor() + 5)
#                 my_ball.ybounce()
#                 bricks[i].reset() # to remove the white square
#                 bricks.pop(i) # pop from the dictionary
#                 break # to exit for loop, otherwise gives an error that dictionary changed during iteration
#
#     # if there are no more bricks left stop the game
#     if len(bricks) == 0:
#         game_is_on = False
#         sketch.clear()
#         sketch.write("You won! You final score: {}".format(score), align="center", font=("Courier", 24, "normal"))
#     elif lives == 0:
#         game_is_on = False
#         sketch.clear()
#         sketch.write("You lost :( You final score: {}".format(score), align="center", font=("Courier", 24, "normal"))
#     my_ball.move()

screen.exitonclick()