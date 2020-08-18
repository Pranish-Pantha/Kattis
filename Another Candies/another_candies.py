num = int(input())
for n in range(num):
    input()

    SUM = 0
    count = 0
    y = int(input())
    for z in range(y):
        x = int(input())
        SUM += x
        count += 1
    if SUM % count == 0:
        print("YES")
    else:
        print("NO")
