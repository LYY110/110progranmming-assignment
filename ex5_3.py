def isNum(n):
    try:
        n=eval(n)
        return True
    except:
        return False
s = input("请输入一个字符串:")
if isNum(s):
    print("{} is a number".format(s))
else:
    print("{} is not a number".format(s))

