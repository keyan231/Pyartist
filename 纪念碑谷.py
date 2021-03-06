import turtle

def 纪念碑谷():
    t = turtle.Pen()
    t.speed(9)
    turtle.bgcolor("#A688EC")
    
    #Part1
    t.pencolor("#5C9EF2")
    t.fillcolor("#5C9EF2")
    t.penup()
    t.goto((-50), 150)
    t.setheading((-30))
    t.pendown()
    t.begin_fill()
    t.forward(230)
    t.right(120)
    t.forward(200)
    t.right(120)
    t.forward(30)
    t.right(60)
    t.forward(140)
    t.left(120)
    t.forward(200)
    t.right(120)
    t.forward(30)
    t.end_fill()

    #Part2
    #t.penup()
    t.backward(30)
    t.right(60)
    t.pencolor("#3578D3")
    t.fillcolor("#3578D3")
    t.begin_fill()
    t.forward(200)
    t.right(120)
    t.forward(30)
    t.right(60)
    t.forward(140)
    t.left(120)
    t.forward(200)
    t.right(120)
    t.forward(30)
    t.right(60)
    t.forward(230)
    t.end_fill()
    
    #Part3
    t.pencolor("#2556A2")
    t.fillcolor("#2556A2")
    t.penup()
    t.right(120)
    t.forward(30)
    t.right(60)
    t.forward(30)
    t.pendown()
    t.begin_fill()
    t.forward(200)
    t.left(120)
    t.forward(230)
    t.left(60)
    t.forward(30)
    t.left(120)
    t.forward(200)
    t.right(120)
    t.forward(140)
    t.left(60)
    t.forward(30)
    t.end_fill()

    #Part4
    t.penup()
    t.backward(6)
    t.pencolor("#5C9EF2")
    t.fillcolor("#5C9EF2")
    t.left(120)
    t.forward(25)

    def drawCube():
        t.pendown()
        t.begin_fill()
        t.forward(4)
        t.left(120)
        t.forward(20)
        t.left(60)
        t.forward(4)
        t.left(120)
        t.forward(20)
        t.left(60)
        t.end_fill()
        t.penup()

    for i in range(12):
        drawCube()
        t.forward(12)

    #Part5
    t.fillcolor("#FFFFFF")
    t.pencolor("#FFFFFF")
    t.goto(90, 60)
    t.pensize(2)
    t.pendown()
    t.forward(9)
    t.left(60)
    t.forward(3)
    t.hideturtle()
    t.penup()
    t.goto(95, 60)
    t.right(60)
    t.pendown()
    t.forward(6)
    t.left(60)
    t.forward(3)
    t.penup()
    t.goto(93, 80)
    t.pendown()
    t.right(33)
    t.begin_fill()
    t.forward(18)
    t.right(85)
    t.circle((-20), 60)
    t.right(87)
    t.forward(18)
    t.right(85)
    t.circle(8)
    t.end_fill()
    t.sety(80)
    t.begin_fill()
    t.lt(150)
    t.fd(25)
    t.rt(145)
    t.fd(25)
    t.rt(90)
    t.fd(4)
    t.end_fill()
    t.goto(95,78)
    t.setheading(180)
    t.pensize(2)
    t.pencolor('#000000')
    for i in range(9):
        t.fd(3)
        t.right(18)
    t.penup()

    #words
    t.goto(-60,-160)
    t.pencolor("#2556A2")
    t.pendown()
    t.write('纪念碑谷', font=("Arial", 30, "normal"))
    t.penup()
    turtle.done()
    
纪念碑谷()
    

