list1=[]
list2=[]
a=int(input("輸入n值:"))
for i in range(a):
    name=str(input("請輸入姓名:"))
    email=str(input("請輸入電子郵件:"))
    list1.append(name)
    list2.append(email)
Who=str(input("請輸入要查詢電子郵件的姓名:"))
for i in range(len(list1)):
    while(list1[i]==Who):
        print(Who,"電子郵件帳號為",list2[i])
        break