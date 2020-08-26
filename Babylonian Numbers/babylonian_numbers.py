n = int(input())
for x in range(n):
    string = input().split(",")
    sum = 0
    for digit in range(len(string)):
        temp = string[(-digit)-1]
        if temp.isdigit():
            sum += int(temp) * pow(60, digit)
    print(sum)
