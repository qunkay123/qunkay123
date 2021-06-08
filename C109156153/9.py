a = input("輸入s1為:")
b = input("輸入s2為:")
win = False
if b.startswith(a):
    win = True
if win==True:
    print('YES')
else:
    print('No')
    