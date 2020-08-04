num = int(input())
for n in range(num):
    p, r, f = map(int, input().split())
    if p > f:
        answer = 0
    else:
        answer = 0
        while p <= f:
            p *= r
            answer += 1
    print(answer)
