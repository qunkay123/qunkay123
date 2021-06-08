index=int(input("請輸入階層值M:"))
a=1
i=1
while(index>a):
    a=a*i
    i=i+1
    if(a>index):
        break
print("超過M為",str(index),"的最小階層N值為:",str(i-1))
    
    