km=float(input("請輸入路程公里數(km):"))
total=75
a=0
b=0
if (km<=1.5):
    print("所需車資為:",total)
else:
   a=(km-1.5)*1000
   if (a<=250):
       total=total+5
       print("所需車資為:",total)
   else:
       if ((a%250)==0):
           total=total+5*(a//250)
           print("所需車資為:",total)
       else:
           total=total+5*(a//250)+5
           print("所需車資為:",total)