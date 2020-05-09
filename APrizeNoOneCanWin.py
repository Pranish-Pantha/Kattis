list1 = input().split()
numItems = list1[0]
minPrice = list1[1]
list2 = list(map(int, input().split()))
list.sort(list2)
answer = 1
for x in range(int(numItems)):
    j = x + 1
    for k in range(j, int(numItems)):
        if list2[x] + list2[k] <= int(minPrice):
            answer += 1
            break
        if list2[x] + list2[j] > int(minPrice):
            break
print(answer)
