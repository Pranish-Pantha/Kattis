n = int(input())
li = input().split()
sense = list(map(str, range(1, n+1)))

for num in range(n):
    if sense[num-1] != li[num-1] and li[num-1] != "mumble":
        print("something is fishy")
        break
else:
    print("makes sense")
