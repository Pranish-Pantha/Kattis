num = int(input())
for x in range(num):
    y = list(input())
    max = 0
    string = ""
    for char in y:
        string += char
        z = str(bin(int(string)))[2:]
        temp = z.count("1")
        if temp > max:
            max = temp
    print(max)
