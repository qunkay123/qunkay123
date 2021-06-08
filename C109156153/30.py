M = int(input("小明身上有幾元:"))
N = int(input("販賣機有幾種飲料:"))
shopl = []
index = 0
for i in range(0,N):
    shop = input("飲料價格:")
    shopl.append(shop)
for x in shopl:
    if M/int(x) > 1 or M/int(x) == 1:
        index+=1
print(index)
        