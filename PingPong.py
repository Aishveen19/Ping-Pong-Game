import turtle as t
playerA=0
playerB=0

# creating screen
window=t.Screen()
window.title=("Pong Game")
window.bgcolor("yellow")
window.setup(width=800, height=600)
window.tracer(0)

# creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("blue")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

# creating right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("blue")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

# creating ball
ball=t.Turtle()
ball.speed(0)
ball.color("red")
ball.shape("circle")
ball.penup()
ball.goto(5,5)
ballxdirection=0.3
ballydirection=0.3

# creating pen to write score
pen=t.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center", font=('Arial',24,'normal'))

# moving left paddle
def leftpaddleup():
	y=leftpaddle.ycor()
	y=y+90
	leftpaddle.sety(y)

def leftpaddledown():
	y=leftpaddle.ycor()
	y=y-90
	leftpaddle.sety(y)

# moving right paddle
def rightpaddleup():
	y=rightpaddle.ycor()
	y=y+90
	rightpaddle.sety(y)

def rightpaddledown():
	y=rightpaddle.ycor()
	y=y-90
	rightpaddle.sety(y)

window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

# ball movement
while True:
	window.update()

	ball.setx(ball.xcor()+ballxdirection)
	ball.sety(ball.ycor()+ballydirection)

# setting border

	if ball.ycor()>290:
		ball.sety(290)
		ballydirection=ballydirection*-1
	if ball.ycor()<-290:
		ball.sety(-290)
		ballydirection=ballydirection*-1

	if ball.xcor()>390:
		ball.goto(0,0)
		ballxdirection=ballxdirection*-1
		playerA=playerA+1
		pen.clear()
		pen.write("Player A:{} Player B:{}".format(playerA , playerB), align="center", font=("Arial",24,"normal"))

	if ball.xcor()<-390:
		ball.goto(0,0)
		ballxdirection=ballxdirection*-1
		playerB=playerB+1
		pen.clear()
		pen.write("Player A:{} Player B:{}".format(playerA , playerB), align="center", font=("Arial",24,"normal"))

# Handling collisions
	if ball.xcor()>340 and ball.xcor()<350 and(ball.ycor()<rightpaddle.ycor()+ 40 and ball.ycor()>rightpaddle.ycor()-50):
		ball.setx(340)
		ballxdirection*=-1

	if ball.xcor()<-340 and ball.xcor()>-350 and(ball.ycor()<leftpaddle.ycor()+ 40 and ball.ycor()>leftpaddle.ycor()-50):
		ball.setx(-340)
		ballxdirection*=-1
