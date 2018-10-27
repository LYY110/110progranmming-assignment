from turtle import*
pensize(1)
pencolor("green")
i=1
while(i<=160):
    seth(90)
    fd(i)
    seth(180)
    fd(i+1)
    seth(-90)
    fd(i+2)
    seth(0)
    fd(i+3)
    i=i+4
seth(90)
fd(161)
seth(180)
fd(162)
seth(-90)
fd(164)
seth(0)
    
