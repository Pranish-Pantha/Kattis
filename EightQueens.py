masterlist = list()
list1 = list(input())
list2 = list(input())
list3 = list(input())
list4 = list(input())
list5 = list(input())
list6 = list(input())
list7 = list(input())
list8 = list(input())
notpos = 0
notlistplus = list()
notlistminus = list()
listpermanentnot = list()
masterlist.append(list1)
masterlist.append(list2)
masterlist.append(list3)
masterlist.append(list4)
masterlist.append(list5)
masterlist.append(list6)
masterlist.append(list7)
masterlist.append(list8)
valid = "valid"
counter = 0
for i in range(8):
    pos = masterlist[i]
    if "*" not in pos:
        valid = "invalid"
        break
    else:
        notpos = pos.index("*")
        if notpos in notlistplus or notpos in notlistminus or notpos in listpermanentnot:
            valid = "invalid"
            break
        if notpos < 0:
            valid = "invalid"
            break
        for a in range(8):
            if pos[a] == "*":
                counter += 1
        if counter > 1:
            valid = "invalid"
            break
        else:
            counter = 0
        listpermanentnot.append(notpos)
        num1 = notpos + 1
        num2 = notpos - 1
        for x in range(len(notlistplus)-1, -1, -1):
            notlistplus[x] += 1
            if notlistplus[x] > 7:
                del notlistplus[x]
        for y in range(len(notlistminus)-1, -1, -1):
            notlistminus[y] -= 1
            if notlistminus[y] < 0:
                del notlistminus[y]
        if 0 <= num1 < 8:
            notlistplus.append(num1)
        if 0 <= num2 < 8:
            notlistminus.append(num2)

print(valid)
