s=input("请输入一行字符：")
zm,sz,kong,qt=0,0,0,0
for c in s:
    if 'a'<=c<='z'or 'A'<=c<='Z':
        zm+=1
    elif '1'<=c<='9':
        sz+=1
    elif c=='':
        kong+=1
    else:
        qt=qt+1
print("英文字符的个数为{0}，数字的个数为{1}，空格的个数为{2}，其他字符的个数为{3}".format(zm,sz,kong,qt))
