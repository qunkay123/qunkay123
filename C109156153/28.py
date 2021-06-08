answer=list("1234")
guess=list(input(""))
a=0
b=0
for i in range(4):
    if (answer[i]==guess[i]):
        a=a+1
    else:
        b=b+1
print(a,"A",b,"B")