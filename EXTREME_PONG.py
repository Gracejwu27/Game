# Simple Pong game
import turtle

wn = turtle.Screen()
wn.title("XTREME PONG BY GRACE WU")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# Boundary Line
boundary_line = turtle.Turtle()
boundary_line.speed(0)
boundary_line.shape("square")
boundary_line.color("white")
boundary_line.shapesize(stretch_wid=40, stretch_len=0.3)
boundary_line.penup()
boundary_line.goto(0, 0)
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=3, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=3, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
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
pen.write("Player 1: 0                  Player 2: 0", align="center", font=("Serif", 24, "normal"))
# Score
score_1 = 0
score_2 = 0
# Game Functions
# Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 30
    paddle_a.setx(x)


def paddle_a_right():
    x = paddle_a.xcor()
    x += 30
    paddle_a.setx(x)

# Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

def paddle_b_left():
    x = paddle_b.xcor()
    x -= 30
    paddle_b.setx(x)

def paddle_b_right():
    x = paddle_b.xcor()
    x += 30
    paddle_b.setx(x)

# Key Bindings
wn.listen()
# Paddle A
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_a_left, "a")
wn.onkey(paddle_a_right, "d")

# Paddle B
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")
wn.onkey(paddle_b_left, "Left")
wn.onkey(paddle_b_right, "Right")
# Main Game Loop


while True:
    wn.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    # Paddle A
    if paddle_a.ycor() > 290:
        paddle_a.sety(280)

    if paddle_a.ycor() < -290:
        paddle_a.sety(-280)

    if paddle_a.xcor() > 0:
        paddle_a.setx(-10)

    if paddle_a.xcor() < -390:
        paddle_a.setx(-380)

    # Paddle B
    if paddle_b.ycor() > 290:
        paddle_b.sety(280)

    if paddle_b.ycor() < -290:
        paddle_b.sety(-290)

    if paddle_b.xcor() < 0:
        paddle_b.setx(10)

    if paddle_b.xcor() > 390:
        paddle_b.setx(380)
    # Ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Paddle and Ball Collisions
    if ball.xcor() >= 370 and ball.xcor() <= 380 and ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and(ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(370)
        ball.dx *= -1

    if ball.xcor() >= -380 and ball.xcor() <= -370 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-370)
        ball.dx *= -1

    if ball.xcor() >= 340 and ball.xcor() <= 350 and ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and(ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() >= -350 and ball.xcor() <= -340 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-340)
        ball.dx *= -1

    if ball.xcor() >= 310 and ball.xcor() <= 320 and ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and(ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(310)
        ball.dx *= -1

    if ball.xcor() >= -320 and ball.xcor() <= -310 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-310)
        ball.dx *= -1

    if ball.xcor() >= 280 and ball.xcor() <= 290 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(280)
        ball.dx *= -1

    if ball.xcor() >= -290 and ball.xcor() <= -280 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-280)
        ball.dx *= -1

    if ball.xcor() >= 250 and ball.xcor() <= 260 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(250)
        ball.dx *= -1

    if ball.xcor() >= -260 and ball.xcor() <= -250 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-250)
        ball.dx *= -1

    if ball.xcor() >= 220 and ball.xcor() <= 230 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(220)
        ball.dx *= -1

    if ball.xcor() >= -230 and ball.xcor() <= -220 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-220)
        ball.dx *= -1

    if ball.xcor() >= 190 and ball.xcor() <= 200 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(190)
        ball.dx *= -1

    if ball.xcor() >= -200 and ball.xcor() <= -190 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-190)
        ball.dx *= -1

    if ball.xcor() >= 160 and ball.xcor() <= 170 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(160)
        ball.dx *= -1

    if ball.xcor() >= -170 and ball.xcor() <= -160 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-160)
        ball.dx *= -1

    if ball.xcor() >= 130 and ball.xcor() <= 140 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(130)
        ball.dx *= -1

    if ball.xcor() >= -140 and ball.xcor() <= -130 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-130)
        ball.dx *= -1

    if ball.xcor() >= 100 and ball.xcor() <= 110 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(100)
        ball.dx *= -1

    if ball.xcor() >= -110 and ball.xcor() <= -100 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-100)
        ball.dx *= -1

    if ball.xcor() >= 70 and ball.xcor() <= 80 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(70)
        ball.dx *= -1

    if ball.xcor() >= -80 and ball.xcor() <= -70and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-70)
        ball.dx *= -1

    if ball.xcor() >= 40 and ball.xcor() <= 50 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(40)
        ball.dx *= -1

    if ball.xcor() >= -50 and ball.xcor() <= -40and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-40)
        ball.dx *= -1

    if ball.xcor() >= 10 and ball.xcor() <= 20 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(10)
        ball.dx *= -1

    if ball.xcor() >= -20 and ball.xcor() <= -10 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-10)
        ball.dx *= -1

    if ball.xcor() >= 0 and ball.xcor() <= 10 and  ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10 and (ball.ycor() < paddle_b.ycor() + 30) and ball.ycor() > paddle_b.ycor()-30:
        ball.setx(5)
        ball.dx *= -1

    if ball.xcor() >= -10 and ball.xcor() <= -0 and ball.xcor() < paddle_a.xcor() + 10 and ball.xcor() > paddle_a.xcor() - 10 and (ball.ycor() < paddle_a.ycor() + 30) and ball.ycor() > paddle_a.ycor()-30:
        ball.setx(-5)
        ball.dx *= -1

    # Score
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.color("white")
        pen.goto(0, 270)
        pen.write("Player 1: {}             Player 2: {}".format(score_1, score_2), align="center", font=("Serif", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.color("white")
        pen.goto(0, 270)
        pen.write("Player 1: {}             Player 2: {}".format(score_1, score_2), align="center", font=("Serif", 24, "normal"))