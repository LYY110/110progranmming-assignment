import turtle

def drawSnake(rad,angle,len,neckrad):
        mycolor=["black","red","red","blue","yellow"]
        yocolor=["yellow","green","yellow","red","red"]
        for i in range(len):
            turtle.pencolor(mycolor[i])
            turtle.circle(rad,angle)
            turtle.pencolor(yocolor[i])
            turtle.circle(-rad,angle)
        turtle.pencolor("green")
        turtle.circle(rad,angle/2)
        turtle.pencolor("yellow")
        turtle.fd(rad)
        turtle.pencolor("red")
        turtle.circle(neckrad+1,180)
        turtle.pencolor("green")
        turtle.fd(rad*2/3)


def main():
       turtle.setup(1300,800,0,0)
       pythonsize=30
       turtle.pensize(pythonsize)
       turtle.seth(-40)
       
       drawSnake(40,80,5,pythonsize/2)

main()
