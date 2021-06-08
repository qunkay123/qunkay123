a = list(input('請輸入值:'))
min = sorted(a,reverse=True)
index = sorted(a,reverse=False)
max = int("".join(min))
mid = int("".join(index))
ans = max - mid
print("最大值數列與最小值數列差值為:"+str(ans))
