a = int(input("請輸入電費"))
summer = 0
nonsummer = 0
power = 0
if a>700:
    power = a - 701
    summer += power * 5.63
    nonsummer += power * 4.50
    a = 700
if a>500 and a<701:
    power = a-500
    summer += power * 4.97
    nonsummer += power * 4.01
    a = 500
if a>330 and a<501:
    power = a-330
    summer += power * 4.39
    nonsummer += power * 3.61
    a = 330
if a>120 and a<331:
    power = a -120
    summer += power * 3.02
    nonsummer += power*2.68
    a = 120
if a<121:
    summer += a*2.10
    nonsummer += a*2.10
print('Summer months:'+str(summer))
print('Non-Summer months:'+str(nonsummer))
