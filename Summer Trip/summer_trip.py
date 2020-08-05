string = list(input())
answer = 0
length = len(string) - 1
for x in range(length):
    try:
        index = string.index(string[x], x+1)
        answer += len(set(string[x+1:index]))
    except Exception as e:
        answer += len(set(string[x+1:]))
print(answer)
