import sys
import math
for line in sys.stdin:
    num = int(line)
    answer = 0
    if num == 0 or num == 1:
        print(1)
    else:
        answer = math.log10(math.sqrt(2 * num * math.pi))
        other = num*math.log10((num/math.e))
        answer = math.floor(answer + other)
        print(answer+1)
