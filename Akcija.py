num = int(input())
l = []
for x in range(num):
    l.append(int(input()))

l.sort(reverse = True)
counter = 0
length = len(l)
for x in range(2, length, 3):
    counter += l[x-1] + l[x-2]
remain = length%3
if remain == 2:
    counter += l[-2] + l[-1]
elif remain == 1:
    counter += l[-1]
print(counter)
