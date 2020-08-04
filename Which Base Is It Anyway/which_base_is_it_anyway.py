num = int(input())
for x in range(num):
    k, n = input().split()
    length = len(n)

    sumO = 0
    sumH = 0
    for x in range(length):
        sumO += int(n[x]) * 8 **(length - x - 1)
        sumH += int(n[x]) * 16 **(length - x - 1)
    Oct = sumO
    Hex = sumH
    if max(map(int, list(n)) ) > 7:
        Oct = 0
    print(k, Oct, int(n), Hex)
