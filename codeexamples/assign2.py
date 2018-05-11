# CST 100 Assignment 2 - Draw a Snowman
# by Mike Davidovich
# Last modified 3/26/2016

# import turtle module, set screen color and size

import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
wn.screensize(canvheight=1200)

# name turtle and set attributes to create snowman body (circles)

circle = turtle.Turtle()
circle.pen(fillcolor = "white", pensize = 3)
circle.speed(10)
circle.hideturtle()

# set starting position for body starting with lowest third, use for loop to draw and fill circles
circle.up()
circle.setposition(0,-200)
circle.down()

circle.begin_fill()
for i in range(313):
    circle.forward(2)
    circle.left(1.15)
circle.end_fill()

# middle circle for snowman body

circle.up()
circle.setposition(0,0)
circle.down()

circle.begin_fill()
for i in range(313):
    circle.forward(1.5)
    circle.left(1.15)
circle.end_fill()

# upper circle for snowman body

circle.up()
circle.setposition(0,150)
circle.down()
    
circle.begin_fill()
for i in range(313):
    circle.forward(1)
    circle.left(1.15)
circle.end_fill()

# set position and atributes for eyes

circle.up()
circle.setposition(-20,220)
circle.down()

# use stamp to stamp first eye

circle.pen(fillcolor = "black")
circle.shape("circle")
circle.stamp()

# set position for second eye

circle.up()
circle.setposition(20,220)
circle.down()

# use stamp to stamp second eye

circle.shape("circle")
circle.stamp()

# set position and attributes for nose

circle.up()
circle.setposition(0,205)
circle.color("orange")
circle.down()

# draw nose

circle.forward(10)
circle.right(105)
circle.forward(35)
circle.right(150)
circle.forward(35)
circle.right(105)
circle.forward(10)

# set attributes for buttons

circle.color("black")
circle.pen(fillcolor = "red")
circle.shape("circle")

# set positions for buttons and stamp to draw

circle.up()
circle.setposition(0,125)
circle.right(90)
circle.down()
circle.stamp()

# button two

circle.up()
circle.setposition(0,95)
circle.right(90)
circle.down()
circle.stamp()

# button three

circle.up()
circle.setposition(0,65)
circle.right(90)
circle.down()
circle.stamp()

# button four

circle.up()
circle.setposition(0,35)
circle.right(90)
circle.down()
circle.stamp()

# set position and attributes for brim of hat

circle.up()
circle.setposition(0,250)
circle.pensize(6)
circle.down()

# draw brim of hat

circle.forward(50)
circle.forward(-100)

# set position and attributes for top hat portion

circle.up()
circle.setposition(0,250)
circle.pensize(6)
circle.pen(fillcolor = "black")
circle.down()

# draw and fill top hat portion

circle.begin_fill()
circle.forward(25)
circle.left(90)
circle.forward(100)
circle.left(90)
circle.forward(50)
circle.left(90)
circle.forward(100)
circle.left(90)
circle.forward(30)
circle.end_fill()

# set position and attributes for arms

circle.up()
circle.setposition(75,75)
circle.pensize(6)
circle.down()

# draw first arm

circle.forward(100)
circle.forward(-15)
circle.left(45)
circle.forward(15)
circle.forward(-15)
circle.right(90)
circle.forward(15)
circle.forward(-15)

# set position for second arm

circle.up()
circle.setposition(-75,75)
circle.down()

# draw second arm

circle.forward(-100)
circle.forward(15)
circle.left(45)
circle.forward(-15)
circle.forward(15)
circle.right(90)
circle.forward(-15)
circle.forward(15)

wn.exitonclick()

# end program

