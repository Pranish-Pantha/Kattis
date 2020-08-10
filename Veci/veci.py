import itertools
num = int(input())
li = itertools.permutations(list(str(num)), len(str(num)))
li = sorted(set(map(lambda x: int("".join(x)), li)))
if li.index(num) + 1 == len(li):
    print(0)
else:
    print(li[li.index(num) + 1])
