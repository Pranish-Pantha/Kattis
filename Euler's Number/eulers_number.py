import math

num = int(input())
answer = 0
if num < 17:
    for i in range(0, num + 1):
        answer += 1/(math.factorial(i))
else:
    answer = 2.7182818284590455
print(answer)
