##### IMPORT STATEMENTS
from turtle import Screen, Turtle
import Invader
import Ship
import time

##### GAME VARIABLES
# score variable
score = 0
# lives
lives = 3


# --- Initialization --- #
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Space Invaders")
screen.tracer(0)
game_is_on = True

# --- SETUP OF GAME ELEMENTS --- #
ship = Ship.Ship((0, -250))
# Invaders are saved in a dictionary with 'cnt' as their id for reference in the code
invaders = {}
cnt = 0
# There are total 18 invaders, 3 rows and 6 columns
for j in range(3):
    for i in range(6):
        invaders.update({cnt: Invader.Invader([i * 100 - 250, 75 + j * 75])})
        cnt += 1

# --- DISPLAY SETUP --- #
sketch = Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Score: {}.".format(score), align="center", font=("Courier", 24, "normal"))

# --- SETUP OF EVENT LISTENERS --- #
screen.listen()
screen.onkey(ship.go_right, "Right")
screen.onkey(ship.go_left, "Left")
screen.onkey(ship.shoot, 'space')

# Margin for detecting collisions with bricks and paddle. (works well for me, you might need to change according
# to your preference
margin_x = 50

# --- GAME LOOP --- #
while game_is_on:
    # Update the screen to see if there are any changes. I found that finding right time delay amount is crucial for
    # smooth experience, this value worked well for me.
    time.sleep(0.01)
    screen.update()

    # Check if ship has fired
    ship.check_bullet()

    # Deal with the invaders. In this loop each invader is modified
    for i in invaders.keys():

        if invaders.get(i):
            # Move the particular invader
            invaders[i].move()

            # Check if it is game over, case when invaders reached the ship
            if invaders[i].ycor() < -250:
                sketch.clear()
                sketch.goto(0, 0)
                sketch.write("You died!", align="center", font=("Courier", 35, "normal"))

            # Check if the invader is hit by a bullet
            if ship.bullet:
                # Following if statement checks the distance between the bullet and an invader
                if invaders[i].ycor() + 10 > ship.bullet.ycor() > invaders[i].ycor() - 10 and \
                                        invaders[i].xcor()+margin_x > ship.bullet.xcor() > invaders[i].xcor()-margin_x:
                    # Update the score
                    score += 1
                    sketch.clear()
                    sketch.write("Score: {}.".format(score), align="center", font=("Courier", 24, "normal"))

                    # Remove hit invader
                    invaders[i].reset()

                    # Remove from invaders dictionary
                    invaders.pop(i)

                    # Reset the bullet
                    ship.bullet.reset()
                    ship.bullet = None

                    # IMPORTANT: To exit for loop, otherwise gives an error that dictionary changed during iteration
                    break

    # Check if all invaders are hit, then end the game
    if score == 18:
        sketch.clear()
        sketch.goto(0, 0)
        sketch.write("You won!", align="center", font=("Courier", 35, "normal"))
        game_is_on = False

screen.exitonclick()
