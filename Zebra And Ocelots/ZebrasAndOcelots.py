i = int(input())
answer = 0
counter = 0
list1 = list()


def pattern(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return 2**(n-1) + pattern(n-1)


for a in range(i):
    list1.append(input())
for j in range(len(list1)-1, -1, -1):
    if list1[j] == "O":
        answer += 1
        if j != len(list1) - 1:
            answer += pattern(counter)
        counter += 1
    else:
        counter += 1
print(answer)
