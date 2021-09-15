#
#
#	Juego retro de ping pong 
#	Programmer: Roberto A. Pérez Iga | @0zym4ndias
#	Fecha: 12 de Septiembre 2021
#
#

#	Modules
import turtle 

window = turtle.Screen()
window.title("Pong game by @0zym4ndias") #  Game title 
window.bgcolor("grey12") #  Background color 
window.setup(width = 800, height = 600)
window.tracer(0) #  It stops the window for updating, so that the game runs smoother


#  Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0) #  Speed of animation - sets it to maxiumum speed 
right_paddle.shape("square") #  Shape of the padlet
right_paddle.color("white") #  The color of the padlet
right_paddle.shapesize(stretch_wid = 5, stretch_len = 1) #  We stretch the square 
right_paddle.penup()
right_paddle.goto(350, 0) #  The initial position of the paddle

#  Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0) #  Speed of animation - sets it to maxiumum speed 
left_paddle.shape("square") #  Shape of the padlet
left_paddle.color("white") #  The color of the padlet
left_paddle.shapesize(stretch_wid = 5, stretch_len = 1) #  We stretch the square 
left_paddle.penup()
left_paddle.goto(-350, 0) #  The initial position of the paddle

#  Ball 
ball = turtle.Turtle()
ball.speed(0) #  Speed of animation - sets it to maxiumum speed 
ball.shape("square") #  Shape of the padlet
ball.color("white") #  The color of the padlet
ball.penup()
ball.goto(0, 0) #  The initial position of the paddle
ball.dx = 0.1 #  The ball moves by two pixels
ball.dy = 0.1 #  The ball moves by two pixels

#  Function
def left_paddle_up():
	y = left_paddle.ycor() #  It returns the y coordinates
	y += 20 #  It will go up
	left_paddle.sety(y) #  Set the paddle to the new y coordinate 

#  Function
def left_paddle_down():
	y = left_paddle.ycor() #  It returns the y coordinates
	y -= 20 #  It will go down
	left_paddle.sety(y) #  Set the paddle to the new y coordinate 

def right_paddle_up():
	y = right_paddle.ycor() #  It returns the y coordinates
	y += 20 #  It will go up
	right_paddle.sety(y) #  Set the paddle to the new y coordinate 

#  Function
def right_paddle_down():
	y = right_paddle.ycor() #  It returns the y coordinates
	y -= 20 #  It will go down
	right_paddle.sety(y) #  Set the paddle to the new y coordinate 

#  Keyboard
window.listen() #  Listen for keyboard input
window.onkeypress(left_paddle_up, "w") #  The w key will make the paddle go up
window.onkeypress(left_paddle_down, "s") #  The s key will make the paddle go down
window.onkeypress(right_paddle_up, "Up") #  The Up arrow will make the paddle go up
window.onkeypress(right_paddle_down, "Down") #  The Down arrow will make the paddle go down

#  Game loop 
while True:
	window.update() #  Every single time the loop runs the window will update the screen

	#  Movement of the ball 
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#  Borders of the window (Up & Down)
	#  Top
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1 #  It will reverse the direction of the ball 
	#  Bottom
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1 #  It will reverse the direction of the ball 

	#  Put the ball back on the center if it goes out 
	if ball.xcor() > 390:
		ball.goto(0, 0) #  Put ball back to the center
		ball.dx *= -1 #  It will reverse the direction of the ball 

	if ball.xcor() < -390:
		ball.goto(0, 0) #  Put ball back to the center
		ball.dx *= -1 #  It will reverse the direction of the ball 

	#  Collisons 
	#if ball.xcor() > 340 and (ball.ycor() < right_paddle)










