import math
numbers = []
while(1):
    num = input()
    if num == "END":
        break
    num = float(num)
    numbers.append(num)

for num in numbers:
    if num == 0 or num == 1:
        print("MEMBER")
    else:
        digits = len(str(num)) - 2
        numerator = int(num * 10**digits)
        denominator = int(10**digits)
        while math.gcd(numerator, denominator) > 1:
            common = int(math.gcd(numerator, denominator))
            numerator = int(numerator / common)
            denominator = int(denominator / common)
        cantor = []
        #print(numerator, denominator)
        for m in range(100):
            x = numerator * 3
            y = x // denominator
            cantor.append(y)
            r = x % denominator
            numerator = r
        #print(cantor)
        isC = True
        if 1 in cantor:
            isC = False
        if isC:
            print("MEMBER")
        else:
            print("NON-MEMBER")
