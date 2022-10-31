# Python program to draw hexagon
# using Turtle graphics
# basic turtle syntax
#hexagon
import turtle
polygon = turtle.Turtle()

num_sides = 6 #specifying the number of sides
side_length = 70 #specifying the length of one side
angle = 360.0 / num_sides 

for i in range(num_sides): #loop
	polygon.forward(side_length)#length

	polygon.right(angle)
	
turtle.done()
#Eof program hehe
