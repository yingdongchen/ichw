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
p.dot(1,"yellow") 
p.speed(0) 
p.shape('circle') 
p.color('yellow')

 
t=turtle.Turtle() 
t.speed(0) 
t.penup() 
t.goto(3,13.4) 
t.pendown() 
t.shape("circle") 
t.color("red") 

 
g=turtle.Turtle() 
g.speed(0) 
g.penup() 
g.color('green') 
g.goto(0,26.3) 
g.pendown() 
g.shape("circle") 

 
e=turtle.Turtle() 
e.speed(0) 
e.penup() 
e.color('brown') 
e.goto(1.5,38.1) 
e.pendown() 
e.shape("circle") 

 
m=turtle.Turtle() 
m.speed(0) 
m.penup() 
m.color('blue') 
m.goto(1.8,60) 
m.pendown() 
m.shape("circle") 

 
l=turtle.Turtle() 
l.speed(0) 
l.penup() 
l.color('purple') 
l.goto(1.8,200.5) 
l.pendown() 
l.shape("circle")  
 
 
k=turtle.Turtle() 
k.speed(0) 
k.penup() 
k.color('orange') 
k.goto(1.1,351.6) 
k.pendown() 
k.shape("circle") 
for x in range(0,1000):  
  for i in range(48*x,48+48*x): 
    t.goto(3+15*sin(0.1*i),13.4*cos(0.1*i)) 
  for i in range(35*x,35+35*x): 
    g.goto(26.3*sin(0.1*i),26.3*cos(0.1*i)) 
  for i in range(30*x,30+30*x): 
    e.goto(1.5+38.7*sin(0.1*i),38.1*cos(0.1*i)) 
  for i in range(24*x,24+24*x): 
    m.goto(1.8+60*sin(0.1*i),60*cos(0.1*i)) 
  for i in range(13*x,13+13*x): 
    l.goto(1.8+201.6*sin(0.1*i),200.5*cos(0.1*i)) 
  for i in range(10*x,10+10*x): 
    k.goto(1.1+352.5*sin(0.1*i),351.6*cos(0.1*i)) 



