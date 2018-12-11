from random import random
def printIntro():
    print("这个程序模拟两个选手A和B的乒乓球比赛")
    print("这个程序需要A和B的能力值（以0到1之间的小数表示)")
def getInputs():
    a=eval(input("请输入选手A的能力值(0-1):"))
    b=eval(input("请输入选手B的能力值(0-1):"))
    n=eval(input("模拟比赛的场次:"))
    return a,b,n
def simNGames(n,probA,probB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simOneGame(7,probA,proB)
        if scoreA>scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB
sa,sb=0,0
for i in range(n):
    scoreA,srcoreB=simOneGame(probA,probB)
    if scoresA>scoresB:
        sa += 1
        if sa == n//2 + 1:
            return sa,sb
    else:
        sb+=1
        if sb==n//2+1:
            return sa,sb
def gameOver_1(a,b):
    if a==11 and b<10:
        return True
    elif a<10 and b==11:
        return True
    elif 11<a<20 and 11<b<20 and abs(a-b)==2:
        return True
    elif a==20 or b==20:
        return True
    return Faise
def gameOver_2(a,b):
    if a==21 and b<20:
        return True
    elif a<10 and b==11:
        return True
    elif 21<a<30 and 21<b<30 and abs(a-b)==2:
        return True
    elif a==30 or b==30:
        return True
    return Faise
def simOneGame(probA,probB):
    scoreA,scoreB=0,0
    serving=0
    t=0
    while not gameOver_1(scoreA,  scoreB):
        if serving==0:
            if random()<probA:
                scoreA += 1
            else:
                scoreB += 1
        else:
            if random()<probB:
                scoreB += 1
            else:
                scoreA += 1
        t=t+1
        if t%5==0:
            serving=(serving+1)%2
    return scoreA,scoreB
def printSummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsB/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsA/n))
def main():
    printIntro()
    probA,probB,n=getInputs()
    winsA,winsB=simNGames(n,probA,probB)
    printSummary(winsA,winsB)
main()
    
                
    
