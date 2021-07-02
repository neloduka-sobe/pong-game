#!/usr/bin/env python3
# Pong game OOP by neloduka_sobe

# Imports

import turtle


# Classes

class Logic():
    """ Responsible for harnessing all other classes together and for game logic """
    def __init__(self, player1, player2, ball):
        """ Initializing screen and keyboard bindings """
        # Variables to operate on
        self.player1 = player1
        self.player2 = player2
        self.ball = ball

        # Creates pen for writing a current score
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)

        # Creates and configures window
        self.window = turtle.Screen()
        self.window.title("Pong by neloduka_sobe")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        # Sets up keyboard interactions
        self.window.listen()
        self.window.onkeypress(self.player1.move_up, "w")
        self.window.onkeypress(self.player1.move_down, "s")
        self.window.onkeypress(self.player2.move_up, "Up")
        self.window.onkeypress(self.player2.move_down, "Down")

    def check_border(self):
        """
        Checks if ball is out of the border.
        Bounces if hits floor or ceiling.
        Teleports to the center when ball hits right or left border.
        """

        # Upper border
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1

        # Downer border
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1

        # Score controll
        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.player1.score += 1
            self.write_score()

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.player2.score += 1
            self.write_score()

        # Left border
        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1

        # Right border
        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1

        # Collision detection
        if (self.ball.xcor() > 340 and self.ball.xcor() < 350 and (self.ball.ycor() < self.player2.ycor() + 40 and self.ball.ycor() > self.player2.ycor() - 50)):
            self.ball.setx(340)
            self.ball.dx *= -1

        if self.ball.xcor() < -340 and self.ball.xcor() > -350 and (self.ball.ycor() < self.player1.ycor() + 40 and self.ball.ycor() > self.player1.ycor() - 50):
            self.ball.setx(-340)
            self.ball.dx *= -1



    def write_score(self):
        """ Writes current score within a window """
        self.pen.clear()
        self.pen.write("Player A: {}  Player B: {}".format(self.player1.score, self.player2.score), align="center", font=("Courier", 12, "normal"))

class Ball(turtle.Turtle):
    """ Class responsible for handling ball object """

    def __init__(self):
        """ Inits a ball object and give it properties """
        # Inheriting from Turtle class
        super().__init__()
        turtle.Turtle.__init__(self)

        # Setting up properties
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)

        # Responsible for ball speed (can be changed)
        self.dx = 1.2
        self.dy = 1.2

    def move(self):
        """ Moves ball specified amount of pixels in a specific direction """
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)


class Paddle(turtle.Turtle):
    """ Responsible for handling paddles interactions """

    # Total number of instances of a class
    num_of_paddles = 0

    def __init__(self):
        """ Responsible for initializing instance and setting up properties"""
        self.score = 0
        Paddle.num_of_paddles += 1

        # Inheriting from Turtle class
        super().__init__()
        turtle.Turtle.__init__(self)

        # Setting up properties
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        # Decides whether to locate a paddle left or right
        if Paddle.num_of_paddles == 1:
            self.goto(-350, 0)
        elif Paddle.num_of_paddles == 2:
            self.goto(350, 0)
        else:
            assert False

    def move_up(self):
        """ Responsible for moving a paddle up """
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        """ Responsible for moving a paddle down """
        y = self.ycor()
        y -= 20
        self.sety(y)


# Main game loop

if __name__ == "__main__":

    # Creating paddles, ball and game logic objects
    paddle_a = Paddle()
    paddle_b = Paddle()
    ball = Ball()
    game = Logic(paddle_a, paddle_b, ball)
    game.write_score()

    while True:
        game.window.update()
        ball.move()
        game.check_border()
