import math
inputs = list()
while(1):
    x = int(input())
    if x == 0:
        break
    inputs.append(x)

k1 = math.log(2*math.pi)


def factorial(n):
    return math.lgamma(n+1)

def stirlings(n):
    return 0.5 *(k1 + math.log(n)) + n * math.log(n) - n


for x in inputs:
    n1 = factorial(x)
    n2 = stirlings(x)
    print(math.pow(math.e, (n1-n2)))
