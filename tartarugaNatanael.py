import turtle 
import string

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.color("medium aquamarine")


with open('tartaruga.txt') as f:
    for line in f:
        if(line.strip("\n") == "CIMA"):
            tartaruga.penup()
        elif(line.strip("\n") == "BAIXO" ):
            tartaruga.pendown()
        else:
            x,y = line.split(" ")
            x = int(x)
            y = int(y)
            tartaruga.setpos(x, y)

