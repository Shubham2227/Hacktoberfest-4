from turtle import *
speed(100)

#DESIGN
color("#D6B268")
penup()
goto(0,-140)
pendown()

for i in range(17):
    begin_fill()
    left(50)
    circle(-30, -90)
    left(80)
    circle(-20, 120)
    left(130)
    circle(-20, 100)
    forward(13)
    left(50)
    circle(-30,-85)
    right(121.5)
    forward(30)
    right(165)
    end_fill()


#OUTER CIRCLE
color("#2255A4")
begin_fill()
penup()
goto(0,-140)
pendown()
right(6)
circle(180)
end_fill()

#INNER CIRCLE
color("#B3E3EE")
begin_fill()
penup()
goto(17,-45)
pendown()
circle(90)
end_fill()

# INNER DOT LINE
penup()
goto(22,-60)
pendown()

color("#D6B268")
right(3)

for i in range(30):
    dot(9)
    left(12)
    penup()
    forward(22)

#OUTER DOT LINE
penup()
goto(0,-125)
pendown()
right(1)
for i in range(50):
    dot(9)
    left(7.5)
    penup()
    forward(22)

#star
penup()
goto(85,-35)
pendown()
left(105)

begin_fill()
for i in range(5):
    forward(172)
    left(144)
end_fill()

pensize(3)

#B
penup()
goto(-50,-60)
pendown()
left(33)
forward(10)
circle(5,180)
forward(10)
back(12)
right(150)
circle(5,180)
right(30)
forward(9)
left(90)
forward(20)

#O
penup()
goto(-70,-55)
pendown()
right(10)
circle(9)

#A
penup()
goto(-77,-25)
pendown()
right(180)
forward(20)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(10)
back(10)
left(90)
forward(10)

#R
penup()
goto(-85,-10)
pendown()
left(180)
forward(15)
circle(-6,300)
left(180)
circle(-7,50)
forward(7)

#D
penup()
goto(-90,5)
pendown()
left(60)
forward(5)
circle(10,180)
forward(5)
left(90)
forward(22)

#O
penup()
goto(-95,45)
pendown()
left(90)
right(10)
circle(9)

#F
penup()
goto(-90,65)
pendown()
right(10)
left(90)
forward(10)
right(90)
forward(10)
back(10)
left(90)
forward(10)
right(90)
forward(12)

#C
penup()
goto(-80,105)
pendown()
right(10)
circle(10,-200)

#O
penup()
goto(-90,130)
pendown()
circle(10)

#N
penup()
goto(-61,132)
pendown()
right(100)
forward(20)
right(150)
forward(22)
left(150)
forward(20)

#T
penup()
goto(-45,150)
pendown()
forward(20)
right(90)
forward(7.5)
back(15)

#R
penup()
goto(-38,155)
pendown()
right(90)
left(180)
forward(15)
circle(-6,300)
left(180)
circle(-7,50)
forward(7)


#OL
write("OL",font=("algerian",20))

#FOR
penup()
goto(10,165)
pendown()
write("FOR",font=("algerian",20))

#C
penup()
goto(95,155)
pendown()
circle(10,-200)

#R
penup()
goto(100,150)
pendown()
right(80)
forward(15)
circle(-6,300)
left(180)
circle(-7,50)
forward(7)

#I
penup()
goto(117,135)
pendown()
left(70)
forward(15)
back(7.5)
left(90)
forward(20)
right(90)
forward(7.5)
back(15)

#C
penup()
goto(138,110)
pendown()
circle(10,-200)

#K
penup()
goto(145,100)
pendown()
right(90)
forward(20)
back(10)
right(50)
forward(15)
back(15)
right(80)
forward(15)

#E
penup()
goto(150,85)
pendown()
left(30)
forward(12)
back(12)
left(90)
forward(10)
right(90)
forward(12)
back(12)
left(90)
forward(10)
right(90)
forward(12)

#T
penup()
goto(155,55)
pendown()
left(90)
forward(20)
left(90)
forward(7.5)
back(15)

#I
penup()
goto(180,15)
pendown()
right(20)
forward(15)
back(7.5)
left(90)
forward(20)
right(90)
forward(7.5)
back(15)

#N
penup()
goto(155,15)
pendown()
right(100)
forward(22)
right(150)
forward(22)
left(150)
forward(22)

#I
penup()
goto(155,-20)
pendown()
right(110)
forward(15)
back(7.5)
left(90)
forward(20)
right(90)
forward(7.5)
back(15)

#N
penup()
goto(150,-60)
pendown()
right(90)
forward(22)
right(150)
forward(22)
left(150)
forward(22)

#D
penup()
goto(130,-55)
pendown()
left(80)
forward(5)
circle(10,180)
forward(5)
left(90)
forward(22)

#I
penup()
goto(105,-95)
pendown()
right(110)
forward(15)
back(7.5)
left(90)
forward(20)
right(90)
forward(7.5)
back(15)

#A
penup()
goto(90,-80)
pendown()
right(90)
forward(20)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(10)
back(10)
left(90)
forward(10)

#heart
penup()
goto(35,-120)
pendown()
left(25)
begin_fill()
forward(28)
circle(-12,200)
setheading(55)
circle(-12,200)
forward(28)
end_fill()

hideturtle()
done()
