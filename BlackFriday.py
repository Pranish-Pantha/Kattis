num = int(input())
test = input()

original = list(map(int, test.split()))
sample = original[:]
sample.sort(reverse=True)

answer = None
for x in sample:
    if sample.count(x) == 1:
        answer = x
        break

if answer is None:
    print("none")
else:
    print(original.index(answer) + 1)
