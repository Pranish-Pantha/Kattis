num1 = input()
num2 = input()

num1 = list(map(int, list(num1)))
num2 = list(map(int, list(num2)))

if len(num1) > len(num2):
    num2 = [0] * (len(num1) - len(num2)) + num2
elif len(num2) > len(num1):
    num1 = [0] * (len(num2) - len(num1)) + num1


finalNum1 = []
finalNum2 = []

for num in range(len(num1)):
    if num1[num] > num2[num]:
        finalNum1.append(num1[num])
    elif num2[num] > num1[num]:
        finalNum2.append(num2[num])
    else:
        finalNum1.append(num1[num])
        finalNum2.append(num2[num])

if len(finalNum1) == 0:
    finalNum1 = "YODA"
else:
    finalNum1 = list(map(str, finalNum1))
    finalNum1 = int("".join(finalNum1))
if len(finalNum2) == 0:
    finalNum2 = "YODA"
else:
    finalNum2 = list(map(str, finalNum2))
    finalNum2 = int("".join(finalNum2))
print(finalNum1)
print(finalNum2)
