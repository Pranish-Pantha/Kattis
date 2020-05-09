import math
num = int(input())
days = math.ceil(1 + math.log(num)/math.log(2))
print(days)
