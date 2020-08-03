import itertools
import math


def findsubsets(s, n): 
    return list(itertools.permutations(s, n))

 
primes = set()
num = int(input())
for n in range(num):
    number = input()
    length = len(number)
    for x in range(length):
        sets = findsubsets(list(number), x + 1)
        for y in sets:
            z = int("".join(y))
            counter = 0
            if z <=1:
                counter +=1
            elif z <4:
                primes.add(z)
            elif z%2 ==0 or z%3 == 0:
                counter += 1
            elif z <25:
                primes.add(z)
            elif z not in primes:
                i = 5
                while i * i <= z:
                    if z % i == 0 or z%(i + 2) == 0:
                        counter += 1
                        break
                    i += 6
                if counter == 0:
                    primes.add(z)
            # for i in range(2, int(math.sqrt(z))+1):
            #     if z % i == 0:
            #         counter += 1
            # if counter == 0:
            #     primes.add(z)
    print(len(primes))
    primes.clear()
