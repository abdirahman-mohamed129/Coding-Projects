

#import os
import turtle


# Screen

wn = turtle.Screen()
wn.title("Rally")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #the game will take really long to update without this - hence the game becomes very slow

# Score
score = 0

# Paddle 
racket = turtle.Turtle()
racket.speed(0)
racket.shape("square")
racket.color("white")
racket.shapesize(stretch_wid=7, stretch_len=1)
racket.penup()
racket.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(-150, 0)
ball.dx = 0.2			# speed
ball.dy = -0.2			# speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle() #unless you hide the pen object it will stay there next to the writing 
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 24, "normal"))


# Function
def racket_up():
    y = racket.ycor()
    y += 20
    racket.sety(y)

def racket_down():
    y = racket.ycor()
    y += -20
    racket.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(racket_up, "Up")
wn.onkeypress(racket_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:    # top of the screen
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:   # bottom of the screen
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:  # left side of the screen
        ball.setx(-390)
        ball.dx *= -1

    if ball.xcor() > 390:  # right side of the screen (game ends to ball returns to the centre, score returns to 0, ball speed = initial speed)
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        score = 0
        pen.write("Score: {}". format(score), align="center", font=("Courier", 24, "normal"))
        score = 0
        ball.dx = -0.2			# initial speed
        ball.dy = 0.2			# initial speed 

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < racket.ycor() + 58 and ball.ycor() > racket.ycor() -58):
        ball.setx(340)
        ball.dx *= -1.2
        score += 1
        pen.clear()
        pen.write("Score: {}". format(score), align="center", font=("Courier", 24, "normal"))
   

# os.system("pause")
