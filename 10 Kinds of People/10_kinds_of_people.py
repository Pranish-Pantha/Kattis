def search(endr, endc, r, c, group):
    temp = []
    num = Map[r][c]
    if groups[r][c] == 0:
        temp.append([r, c])
        while len(temp)>0:
            tempr = temp[0][0]
            tempc = temp[0][1]
            groups[tempr][tempc] = group
            temp.pop(0)
            if tempr>0 and num == Map[tempr-1][tempc] and groups[tempr-1][tempc] == 0:
                groups[tempr-1][tempc] = group
                temp.append([tempr-1, tempc])
            if tempc>0 and num == Map[tempr][tempc-1] and groups[tempr][tempc-1] == 0:
                groups[tempr][tempc-1] = group
                temp.append([tempr, tempc-1])
            if tempr<len(Map) -1 and num == Map[tempr+1][tempc] and groups[tempr+1][tempc] == 0:
                groups[tempr+1][tempc] = group
                temp.append([tempr+1, tempc])
            if tempc<len(Map[0]) -1 and num == Map[tempr][tempc+1] and groups[tempr][tempc+1] == 0:
                groups[tempr][tempc+1] = group
                temp.append([tempr, tempc+1])
    if groups[r][c] == groups[endr][endc]:
        if Map[r][c] == "0":
            print("binary")
        else:
            print("decimal")
    else:
        print("neither")

Map = []
r, c = map(int, input().split())
for x in range(r):
    Map.append(list(input()))
groups = [[0 for x in range(c)] for y in range(r)]
num = int(input())
for x in range(num):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    search(r2, c2, r1, c1, x+1)
