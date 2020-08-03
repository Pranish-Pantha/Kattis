n, time = map(int, input().split())
dictionary = {}
for x in range(n):
    money, t = map(int, input().split())
    if money in dictionary.keys():
        dictionary[money] += [t]
    else:
        dictionary.update({money: [t]})
sum = 0
times = [""] * time
lis = list(dictionary.keys())
lis.sort(reverse=True)
for money in lis:
    if time >0:
        temp = sorted(dictionary.get(money))
        for m in temp:
            if time > 0:
                temp_time = m
                for x in range(temp_time, -1, -1):
                    if times[x] == "":
                        times[x] = money
                        break
    else:
        break
for m in times:
    if type(m) is int:
        sum += m
print(sum)
