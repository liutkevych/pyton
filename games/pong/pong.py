import turtle
import os

player_a = input("Player1 name: ").strip()
player_b = input("Player2 name: ").strip()

wn = turtle.Screen()
wn.title("Pong by @oli")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("pink")
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
ball.dx = 2
ball.dy = 2


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Function
def paddle_a_up():
    # ycor is a method from turtle which defines y coordinate
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

def write_score():
    pen.write(
        f"{player_a}: {score_a}  {player_b}: {score_b}", 
        align="center", 
        font=("Courier", 24, "normal")
    )

def play_sound():
    os.system("afplay bouce.mp3&")

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Print initial score
write_score()

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border cheking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        play_sound()
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_sound()
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        write_score()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        write_score()
    # Paddle and ball colisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        play_sound()
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > paddle_a.ycor() -40 and ball.ycor() < paddle_a.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1
        play_sound()
