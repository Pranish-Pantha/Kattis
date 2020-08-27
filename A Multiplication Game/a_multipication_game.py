import sys
import math

def switch(n):
    return 9 if n==2 else 2

for line in sys.stdin:
    num = int(line)
    counter = 2
    temp = 1
    while temp < num:
        counter = switch(counter)
        temp *= counter
    if counter == 2:
        print("Ollie wins.")
    else:
        print("Stan wins.")
