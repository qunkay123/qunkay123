list1=[]
for i in range(10):
    print("請輸入第",i+1,"個數字:",end="")
    num=int(input())
    list1.append(num)
list1.sort()
print("最大的3個數字為:",list1[9],",",list1[8],",",list1[7])
print("最小的3個數字為:",list1[2],",",list1[1],",",list1[0])

