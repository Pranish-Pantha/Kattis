line = input().split()
if len(line) == 1:
    print(2**(int(line[0])+1) -1)
else:
    start, string = int(line[0]), line[1]
    answer = 2**(start+1)-1
    start = 2**(start+1)-1
    lossL = []
    lossR = []
    for char in range(len(string)):
        if string[char] == "L":
            for x in range(len(lossL)):
                answer -= lossL[x]
                lossL[x] *= 2
            lossL.append(1)
            answer -= 1
            for x in range(len(lossR)):
                answer -= lossR[x]
                lossR[x] *= 2
        else:
            lossR.append(1)
            for x in range(len(lossR)):
                answer -= lossR[x]
                lossR[x] *= 2
            answer -= 1
            for x in range(len(lossL)):
                answer -= lossL[x]
                lossL[x] *= 2

    print(answer)
