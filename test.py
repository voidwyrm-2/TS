from turtle import Turtle, Screen
#Turtle.hideturtle(Turtle)

screen = Screen()
screen.screensize(800, 800)
screen.register_shape('Greeben-flat.gif')

turt = Turtle()
turt.penup()
#turt.goto(-280, -280)
turt.shape('Greeben-flat.gif')

screen.mainloop()