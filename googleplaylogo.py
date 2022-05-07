import turtle
t = turtle.Turtle()
def calculation(r,deg1,deg2):
    #first circle of 120 degree calculation
    t.up()
    t.goto(-100,-100)
    t.setheading(270)
    t.circle(r,deg1)
    cor1,cor2 =t.pos()
    #second circle of 60 degree calculation
    t.goto(-100,-100)
    t.setheading(270)
    t.circle(r,deg2)
    cor3,cor4 =t.pos()
    print(cor3,cor4)
    t.down()
    t.clear()
    return(cor1,cor2,cor3,cor4)

def triangle(a,b,c,col,r,deg,cond1,cond2,cor1,cor2):

    t.up()
    #starting point
    t.goto(-100,-100)
    t.down()

    t.begin_fill()
    t.fillcolor(col)
    t.setheading(90)
    t.forward(a)    
    t.circle(-r,deg)
    #if first circle of 60 degree then 80 degree transfer is required
    if(deg==60):
        t.right(80)
    t.forward(b)
    if(col=="gold"):
        t.circle(-r,deg)
    t.goto(cor1,cor2)
    # for gold & red second circle of 120 degree is required
    if(col=='gold' or col =='#ff3333'):
        if(col=='#ff3333'):
            #to align to proper degree
            t.right(100)
        t.circle(-r,120)
    else:
        if(col=="#48ff48"):
            #to align to proper degree
            t.right(180)
        elif(col=="#3bccff"):
            #to align to proper degree
            t.right(160)     
        t.circle(-r,60)
    #to manually connect the last point if due to decimal minor gap is present
    t.goto(-100,-100)
    t.end_fill()
    
            
#to know the cordinate value of bottom circle at two different angles 
cor1,cor2,cor3,cor4=calculation(20,120,60)
#gold color triangle
triangle(200,200,200,'gold',20,120,True,True,cor1,cor2)
#green color triangle
triangle(200,130,185,'#48ff48',20,120,True,False,cor3,cor4)
#red color traingle
triangle(200,217,160,'#ff3333',20,60,False,True,cor1,cor2)
#blue color triangle
triangle(200,148,140,'#3bccff',20,60,False,True,cor3,cor4)


