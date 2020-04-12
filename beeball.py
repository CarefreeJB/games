import turtle

wn = turtle.Screen()
wn.title("BEEBALL BY CAREFREE")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Function
def paddle_a_left():
    x = paddle_a.xcor()
    x += 100
    paddle_a.setx(x)

def paddle_a_right():
    x = paddle_a.xcor()
    x -= 100
    paddle_a.setx(x)

# Keyboard binding
wn.onkeypress(paddle_a_left, "w")
wn.onkeypress(paddle_a_right, "s")

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1

    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1

    if ball.xcor() > 390:
       ball.goto(0, 0)
       ball.dx *= -1

    if ball.xcor() < -390:
       ball.goto(0, 0)
       ball.dx *= -1



     # Border checking
    if ball.xcor() > 290:
       ball.sety(290)
       ball.dx *= -1

    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1

    if ball.xcor() > 390:
       ball.goto(0, 0)
       ball.dx *= -1

    if ball.ycor() < -390:
       ball.goto(0, 0)
       ball.dy *= -1

# Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and ( ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(340)
        ball.dx *= -1


