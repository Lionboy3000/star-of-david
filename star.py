import turtle
 
star = turtle.Turtle()
 
star.fillcolor("yellow")
star.begin_fill()
for i in range(5):
    star.forward(100)
    star.right(144)
star.end_fill()
 
turtle.done()