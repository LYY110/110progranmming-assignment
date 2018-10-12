#e1.1TempConvert.py
a=input("请输入温度的符号:")
TempStr=eval(input("请输入温度的数值:"))
if a in ['F','f']:
   c=int((TempStr-32)/1.8)
   print("转换后的温度是{：d}C".format(C))
elif a in ['C','c']:
    F=eval(1.8*TempStr+32)
    print("转换后的温度是{：d}F".format(F))
else:
    print("输入格式错误")
        

