from sys import stdin
import decimal
from math import factorial

decimal.getcontext().prec = 122
for line in stdin:
    cline = str(line.split()[0])
    length = len(cline)
    answer = decimal.Decimal(factorial(length))
    div = 1
    for char in set(cline):
        count = cline.count(char)
        div *= factorial(count)
    answer /= div
    print("{:.0f}".format(answer))
