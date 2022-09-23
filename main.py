import turtle
from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=500, height=400)

# TODO: Ask who will win the race

answer = turtle.textinput("Turtle race", "Who is going to win?").lower()

green = Turtle()
green.color("green")
green.shape("turtle")
green.penup()

red = Turtle()
red.color("red")
red.shape("turtle")
red.penup()

blue = Turtle()
blue.color("blue")
blue.shape("turtle")
blue.penup()

orange = Turtle()
orange.color("orange")
orange.shape("turtle")
orange.penup()

black = Turtle()
black.color("black")
black.shape("turtle")
black.penup()

purple = Turtle()
purple.color("purple")
purple.shape("turtle")
purple.penup()


# TODO: Align all the turtles at the beginning of the screen
green.goto(-230, 80)
red.goto(-230, 50)
blue.goto(-230, 20)
orange.goto(-230, -10)
black.goto(-230, -40)
purple.goto(-230, -70)

# TODO: Make the steps random


def movement(func):
    speed = random.randint(0, 10)
    func.forward(speed)


# TODO: Complete the program once a turtle reaches the edge of the screen

my_list = [orange, green, black, red, purple, blue]

end = True

while end:
    movement(orange)
    movement(green)
    movement(black)
    movement(red)
    movement(purple)
    movement(blue)
    for colores in my_list:
        if colores.xcor() >= 180:
            winner = colores.color()
            winner_1 = winner[0]
            print(f"{winner_1} is the winner")
            if answer == winner_1.lower():
                print("Congrats! You chose the right turtle!    ")
            else:
                print("Try again!")
            end = False


# TODO: Print the winner on console


screen.exitonclick()