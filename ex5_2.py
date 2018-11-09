def isodd(n):
    if n%2==0:
        return True
    else:
        return False
def main():
    while True:
        n=int(input("请输入一个整数："))
        if isodd(n):
            print("n是偶数")
        else:
            print("n是奇数")
main()


