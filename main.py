import turtle
import random 

pen = turtle.Turtle()
'''
pen.forward(50)
pen.right(140)
pen.forward(50)
pen.right(140)
pen.forward(60)
pen.right(150)
pen.forward(60)
pen.right(145)
pen.forward(55)

def drawStar(l):
  for x in range(5):
    pen.forward(l)
    pen.right(144)

drawStar(int(input("LENGTH :")))

# Exercise 2 - Drawing shapes
def drawRec(l,w):
  for y in range(2):
    pen.forward(l)
    pen.right(90)
    pen.forward(w)
    pen.right(90)
drawRec(30,50)

def drawShape(r,s):
  pen.circle(r,360,s)

drawShape(float(input("Radius: ")), int(input("Number of sides: ")))
'''

#Exercise 3 - Draw a Spiral 

#List with colors
colors=['orange', 'red', 'blue', 'green', 'cyan', 'purple']

#for loop
for x in range(50):
  pen.color(colors[x % 6])
  pen.width(x/5 +1)
  pen.forward(x)
  pen.left(20)