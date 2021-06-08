a = int(input("請輸入組數:"))
for i in range(1,a+1):
    b = input("第"+str(i)+"組")
    c=b.split(" ")
    money=250*int(c[0])+175*int(c[1])
    print("第"+str(i)+'組應收費用:'+str(money))
    
        
            