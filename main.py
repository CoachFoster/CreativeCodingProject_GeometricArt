### Turtle Graphics
### make a geometric pattern

import time
import random
import turtle

scrn = turtle.Screen()
ct = turtle.Turtle()
ct.hideturtle()
ct.speed(0)

### Step 1: Make a hexagon
for i in range(6):
  ct.forward(100)
  ct.left(60)

time.sleep(1)

### Step 2: Repeat the hexagon
for n in range(36):   # complete a cicle
  for i in range(6):    # make a hexagon 
    ct.forward(100)
    ct.left(60)
  ct.right(10)

time.sleep(5)

### Experiment 4: Overlapping circles
ct.reset()
ct.speed(0)
ct.hideturtle()
ct.color('white')
scrn.bgcolor('purple')
time.sleep(1)
for n in range(36): # complete a 360-degree cicle
  ct.circle(100)
  ct.right(10)

time.sleep(5)

### Step 3: Change background and add rainbow colors
scrn.reset()
scrn.bgcolor('black')
ct.reset()
ct.speed(0)
ct.hideturtle()
pen_colors = ['red', 'green', 'orange', 'orange', 'yellow', 'red']
for n in range(36):         # complete a 360-degree cicle
  for i in range(6):        # make a hexagon 
    ct.color(pen_colors[i]) # choose the next color
    ct.forward(100)
    ct.left(60)
  ct.right(10)

time.sleep(1)

### Step 4: Add circles around the pattern
ct.penup()
ct.color('white')
for i in range(36):
  ct.forward(220)
  ct.pendown()
  ct.circle(5)
  ct.penup()
  ct.backward(220)
  ct.right(10)
print('Tada!')

time.sleep(5)

### Experiment 5a: Circle of circles
ct.reset()
ct.speed(0)
ct.hideturtle()
ct.color('white')
for n in range(36):
  ct.penup()
  ct.forward(200)
  for i in range(6):
    ct.pendown()
    ct.circle(5)
    ct.penup()
    ct.backward(20)
  ct.backward(80)
  ct.right(10)

time.sleep(5)

### Experiment 5b: A rainbow circle of circles
ct.reset()
ct.speed(0)
ct.hideturtle()
rainbow_colors = ['red', 'lime', 'blue', 'yellow', 'orange', 'purple']
for n in range(36):
  ct.penup()
  ct.forward(200)
  for i in range(6):
    ct.color(rainbow_colors[i])
    ct.pendown()
    ct.circle(5)
    ct.penup()
    ct.backward(20)
  ct.backward(80)
  ct.right(10)

time.sleep(5)

### Experiment 5c: Square of squares
ct.reset()
ct.speed(0)
ct.hideturtle()
ct.color('yellow')
for i in range(190):
  ct.forward(i*3)
  ct.right(90)

time.sleep(5)

### Experiment 1a: Create a row of colored squares
ct.reset()
ct.speed(0)
ct.hideturtle()
ct.pensize(4)
rainbow_colors = ['red', 'lime', 'blue', 'yellow', 'orange', 'magenta']
for n in range(6):
  # ct.color(random.choice(rainbow_colors)) # pick a random color
  ct.color(rainbow_colors[n])
  for i in range(4):
    ct.forward(20)
    ct.left(90)
  ct.penup()
  ct.forward(30)
  ct.pendown()
ct.hideturtle()

time.sleep(2)

### Experiment 1b: Create rows of colored squares
ct.reset()
ct.speed(0)
ct.hideturtle()
ct.pensize(2)
rainbow_colors = ['red', 'lime', 'blue', 'yellow', 'orange', 'magenta']
for j in range(6): # draw rows of squares
  for n in range(6): # draw a row of squares
    ct.color(rainbow_colors[n])
    for i in range(4): # draw a square
      ct.forward(20)
      ct.left(90)
    ct.penup()
    ct.forward(30)
    ct.pendown()
  ct.penup()
  ct.goto(0,ct.ycor()+25)
  ct.pendown()

time.sleep(5)

### Experiment 2: Make a face
scrn.reset()
ct.reset()

def draw_head():
  ct.begin_fill()
  ct.color('green')
  ct.circle(150)
  ct.end_fill()

def draw_eye():
  ct.begin_fill()
  ct.color('white')
  ct.circle(30)
  ct.end_fill()
  ct.begin_fill()
  ct.color('black')
  ct.circle(20)
  ct.end_fill()

ct.penup()
ct.goto(0,-75)
ct.pendown()
draw_head()

ct.penup()
ct.goto(-35,100)
ct.pendown()
draw_eye()

ct.penup()
ct.goto(35,100)
ct.pendown()
draw_eye()

ct.penup()
ct.goto(0.0)
ct.shape('circle')
print('Hello, World!')

time.sleep(5)

### Experiment 3: Make a house
scrn.bgcolor('tan')
ct.reset()
ct.speed(0)
ct.hideturtle()

# make the first big square for the house
ct.begin_fill()
ct.color('gray')
for i in range(4):
  ct.forward(100)
  ct.left(90)
ct.end_fill()
ct.penup()
ct.goto(-20,100)
ct.pendown()

# make a triangle roof
ct.begin_fill()
ct.color('navy')
for i in range(3):
  ct.forward(140)
  ct.left(120)
ct.end_fill()

# make two windows
ct.penup()
ct.goto(15,70)
ct.begin_fill()
ct.color('yellow')
for i in range(4):
  ct.forward(20)
  ct.left(90)
ct.end_fill()

ct.penup()
ct.goto(65,70)
ct.begin_fill()
ct.color('yellow')
for i in range(4):
  ct.forward(20)
  ct.left(90)
ct.end_fill()

# make a door
ct.penup()
ct.goto(40,0)
ct.begin_fill()
ct.color('black')
ct.forward(30)
ct.left(90)
ct.forward(40)
ct.left(90)
ct.forward(30)
ct.left(90)
ct.forward(40)
ct.end_fill()

# add a doorknob
ct.penup()
ct.goto(60,15)
ct.begin_fill()
ct.color('red')
ct.circle(3)
ct.end_fill()