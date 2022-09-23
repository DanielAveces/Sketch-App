from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(5)
tim.color("blue")

def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_a():
    tim.right(10)


def move_d():
    tim.left(10)


def clear_command():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_a)
screen.onkey(key="d", fun=move_d)
screen.onkey(key="space", fun=clear_command)

screen.exitonclick()