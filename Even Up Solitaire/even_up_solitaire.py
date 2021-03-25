from collections import deque
n = int(input())
stack = deque()
cards = list(map(int, input().split()))
N = n
for i in range(n):
    if not stack:
        stack.append(cards[i])
        continue
    left = stack.pop()
    if (left + cards[i]) % 2 == 0:
        N -= 2
    else:
        stack.extend([left, cards[i]])
print(N)