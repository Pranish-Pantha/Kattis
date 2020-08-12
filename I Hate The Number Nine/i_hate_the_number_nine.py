num = int(input())
for x in range(num):
    answer = 8 * pow(9, int(input()) -1, 1000000007)
    print(answer % 1000000007)
