score = int(input())
num1 = num2 = num3 = 0
s1 = s2 = s3 = None
numOfShots = 0
if score <= 20:
    num1 = score
    s1 = "Single"
    numOfShots = 1
elif score <= 40:
    num1, num2 = 20, score - 20
    s1 = s2 = "Single"
    numOfShots = 2
elif score <= 60:
    num1, num2, num3 = 20, 20, score - 40
    s1 = s2 = s3 = "Single"
    numOfShots = 3
elif score <= 80:
    num1, num2 = 20, score - 60
    s1, s2 = "Triple", "Single"
    numOfShots = 2
elif score <= 100:
    num1, num2, num3 = 20, 20, score - 80
    s1, s2, s3 = "Triple", "Single", "Single"
    numOfShots = 3
elif score <= 120:
    num1, num2, num3 = 20, 20, score - 100
    s1, s2, s3 = "Triple", "Double", "Single"
    numOfShots = 3
elif score <= 140:
    num1, num2, num3 = 20, 20, score - 120
    s1, s2, s3 = "Triple", "Triple", "Single"
    numOfShots = 3
elif score <= 160:
    if (score - 120) % 3 == 0:
        num1, num2, num3 = 20, 20, (score - 120) / 3
        s1 = s2 = s3 = "Triple"
        numOfShots = 3
    elif (score - 120) % 2 != 0:
        if (score - 117) % 2 == 0:
            num1, num2, num3 = 20, 19, (score - 117) / 2
            s1, s2, s3 = "Triple", "Triple", "Double"
            numOfShots = 3
        else:
            numOfShots = 4
    else:
        num1, num2, num3 = 20, 20, (score -120) / 2
        s1, s2 ,s3 = "Triple", "Triple", "Double"
        numOfShots = 3
elif score <= 180:
    if (score - 120) % 3 == 0:
        num1, num2, num3 = 20, 20, (score - 120) / 3
        s1 = s2 = s3 = "Triple"
        numOfShots = 3
    elif (score % 2 != 0) or ((score - 120) / 2 > 20):
        numOfShots = 4
    else:
        num1, num2, num3 = 20, 20, (score - 120) / 2
        s1, s2, s3 = "Triple", "Triple", "Double"
        numOfShots = 3

num1 = str(int(num1))
num2 = str(int(num2))
num3 = str(int(num3))
if numOfShots == 1:
    print(s1, num1)
elif numOfShots == 2:
    print(s1, num1)
    print(s2, num2)
elif numOfShots == 3:
    print(s1, num1)
    print(s2, num2)
    print(s3, num3)
else:
    print("impossible")
