import math
n = int(input())
list1 = list()
end = 1
while n != 1:
    counter = 0
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            list1.append(i)
            counter += 1
            break
    if counter == 0:
        print(len(list1) + 1)
        end = 0
        break
    n = n / list1[len(list1)-1]
if end == 1:
    print(len(list1))
