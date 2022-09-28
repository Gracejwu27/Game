# Simple Pong game

import turtle

wn = turtle.Screen()
wn.title("Pong by Grace Wu")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Serif", 24, "normal"))

# Score
score_1 = 0
score_2 = 0
# Game Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

# Key Bindings
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

# Main Game Loop


while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if paddle_a.ycor() > 290:
        paddle_a.sety(280)

    if paddle_a.ycor() < -290:
        paddle_a.sety(-280)

    if paddle_b.ycor() > 290:
        paddle_b.sety(280)

    if paddle_b.ycor() < -290:
        paddle_b.sety(-290)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Serif", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Serif", 24, "normal"))

    # Paddle and Ball Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40) and ball.ycor() > paddle_b.ycor()-40:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() > -350 and ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40) and ball.ycor() > paddle_a.ycor()-40:
        ball.setx(-340)
        ball.dx *= -1

    # AI Player
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10 and ball.xcor() > 300:
        paddle_b_up()

    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10 and ball.xcor() > 300:
        paddle_b_down()

    # Winning a game
    if score_2 >= 5:
        pen.goto(0, 0)
        pen.write("Player 2 wins! Player 1 sucks!", align="center", font=("Serif", 24, "normal"))
    if score_1 >= 5:
        pen.goto(0, 0)
        pen.write("Player 1 wins! Player 2 sucks!", align="center", font=("Serif", 24, "normal"))
