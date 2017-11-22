import math
def sin(x):
    y=math.sin(math.radians(x))
    return y
def cos(x):
    y=math.cos(math.radians(x))
    return y
import turtle
wn = turtle.Screen()
wn.bgcolor("white")

p=turtle.Turtle()
p.dot(5,"yellow")
p.speed(0)
p.shape('circle')
p.color('yellow')

t=turtle.Turtle()
t.speed(0)
t.penup()
t.goto(20,89)
t.pendown()
t.shape("circle")
t.color("red")


g=turtle.Turtle()
g.speed(0)
g.penup()
g.color('green')
g.goto(0,175.4)
g.pendown()
g.shape("circle")

e=turtle.Turtle()
e.speed(0)
e.penup()
e.color('brown')
e.goto(10,258)
e.pendown()
e.shape("circle")

m=turtle.Turtle()
m.speed(0)
m.penup()
m.color('blue')
m.goto(12,400)
m.pendown()
m.shape("circle")

l=turtle.Turtle()
l.speed(0)
l.penup()
l.color('purple')
l.goto(12,1344)
l.pendown()
l.shape("circle") 

k=turtle.Turtle()
k.speed(0)
k.penup()
k.color('orange')
k.goto(7,2463)
k.pendown()
k.shape("circle")
for x in range(0,1000): 
  for i in range(48*x,48+48*x):
    t.goto(20+100*sin(0.1*i),89*cos(0.1*i))
  for i in range(35*x,35+35*x):
    g.goto(175.4*sin(0.1*i),175.4*cos(0.1*i))
  for i in range(30*x,30+30*x):
    e.goto(10+258*sin(0.1*i),257.4*cos(0.1*i))
  for i in range(24*x,24+24*x):
    m.goto(10+400*sin(0.1*i),399.4*cos(0.1*i))
  for i in range(13*x,13+13*x):
    l.goto(12+1344*sin(0.1*i),1340*cos(0.1*i))
  for i in range(10*x,10+10*x):
    k.goto(12+2463*sin(0.1*i),2460*cos(0.1*i))