import math
a, b = map(int, input().split())
n_1 = ((a/2) + 2 + math.sqrt(pow((a/2)+2,2)-4*(a+b)))/2
n_2 = (a+b) / n_1
print(int(n_1), int(n_2))
