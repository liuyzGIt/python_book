import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_sprial(my_turtle, length):
    if length > 0:
        my_turtle.forward(length)
    else:
        return
    my_turtle.right(90)
    draw_sprial(my_turtle, length - 5)
    
draw_sprial(my_turtle, 100)
my_win.exitonclick()
