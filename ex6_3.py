def testReEle(lis):
    for e in nList:
       if nList.count(e) > 1:
           return True
    return False
def getList():
    lis=[]
    ch=input("请输入判定元素，回车表示结束:")
    while ch != '': 
        lis.append(ch)
        ch=input("请输入一个判定元素，回车表示结束：")
    testReEle(lis)
getList()
