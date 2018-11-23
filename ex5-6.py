def Febric(n):
    if n==1 or n==2:
        return 1
    else:
        return Febric(n-1)+Febric(n-2)
n=int(input("请输入一个正整数："))
print("Fabric数列如下:")
    for i in range(1,nprint(Febric(n))
