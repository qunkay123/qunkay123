m=int(input(""))
d=int(input(""))
s=(m*2+d)%3
list=["普通","吉","大吉"]
for i in range(3):
    if (s==i):
        print(list[i])