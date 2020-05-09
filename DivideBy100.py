list1 = list(input())
counter = len(input()) - 1
answer = ""
length = len(list1)
decimal = 0
counter2 = 0
if counter >= length:
    add = counter - length
    answer += "0."
    answer += "0" * add
else:
    counter2 = length - counter
    list1.insert(counter2, ".")
    length += 1
decimal = length-1
for x in range(decimal, counter2-1, -1):
    if list1[x] == "0":
            decimal = decimal - 1
    elif list1[x] != ".":
            break
    else:
        decimal = decimal - 1
        break
for z in range(0, decimal+1):
    answer += list1[z]
print(answer)
