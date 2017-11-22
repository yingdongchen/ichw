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
t.goto(6,26.7)
kt.pendown()
t.shape("circle")
t.color("red")


g=turtle.Turtle()
g.speed(0)g.penup()
g.color('green')
g.goto(0,52.6)
g.pendown()
g.shape("circle")

e=turtle.Turtle()
e.speed(0)
e.penup()
e.color('brown')
e.goto(3,77.4)
e.pendown()
e.shape("circle")

m=turtle.Turtle()
m.speed(0)
m.penup()
m.color('blue')
m.goto(3.6,120)
m.pendown()
m.shape("circle")

l=turtle.Turtle()
l.speed(0)
l.penup()
l.color('purple')
l.goto(3.6,403.2)
l.pendown()
l.shape("circle") 

k=turtle.Turtle()
k.speed(0)
k.penup()
k.color('orange')
k.goto(2.1,703.2)
k.pendown()
k.shape("circle")
for x in range(0,1000): 
  for i in range(48*x,48+48*x):
     t.goto(6+30*sin(0.1*i),26.7*cos(0.1*i))
  for i in range(35*x,35+35*x):
    g.goto(52.6*sin(0.1*i),52.6*cos(0.1*i))
  for i in range(30*x,30+30*x):
    e.goto(3+77.4*sin(0.1*i),76.2*cos(0.1*i))
  for i in range(24*x,24+24*x):
    m.goto(3.6+120*sin(0.1*i),119.4*cos(0.1*i))
  for i in range(13*x,13+13*x):
    l.goto(3.6+403.2*sin(0.1*i),401*cos(0.1*i))
  for i in range(10*x,10+10*x):
    k.goto(2.1+705*sin(0.1*i),703.2*cos(0.1*i)
    k.goto(2.112+2463*sin(0.1*i),2460*cos(0.1*i))
