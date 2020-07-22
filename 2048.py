board = list()
for x in range(4):
    line = list(map(int, input().split()))
    board.append(line)
move = int(input())
newboard = list()


def getPrevious(List, col):
    if 0 in List:
        if List.index(0) == 0:
            return 0
    return List[:col].count(0)

def getAfter(List, col):
    if 0 in List:
        if list(reversed(List)).index(0) == 0:
            return 0
    return List[col:].count(0)

def getColPrevious(Board, col, ind):
    temp = []
    for line in Board:
        temp.append(line[col])
    if 0 in temp:
        if temp.index(0) == 0:
            return 0
    return temp[:ind].count(0)

def getColAfter(Board, col, ind):
    temp = []
    for line in Board:
        temp.append(line[col])
    if 0 in temp:
        if list(reversed(temp)).index(0) == 0:
            return 0
    return temp[ind:].count(0)

if move == 0:
    for line in range(len(board)):
        newLine = []
        for num in range(len(board[0])):
            if board[line][num] == 0:
                pass
            else:
                if len(newLine) == 0:
                    newLine.append(board[line][num])
                elif board[line][num] == board[line][num-1 - getPrevious(board[line], num)] and board[line][num] ==newLine[-1]:
                    newLine[-1] *= 2
                else:
                    newLine.append(board[line][num])
        newboard.append(newLine)
        newboard[-1] += (4-len(newboard[-1]))*[0]
if move == 2:
    for line in range(len(board)):
        newLine = []
        for num in range(len(board[0])-1, -1, -1):
            if board[line][num] == 0:
                pass
            else:
                if len(newLine) == 0:
                    newLine.append(board[line][num])
                elif board[line][num] == newLine[-1] and board[line][num] == board[line][num+1+ getAfter(board[line], num)]:
                    newLine[-1] *= 2
                else:
                    newLine.append(board[line][num])
        newLine.reverse()
        newboard.append(newLine)
        newboard[-1] = (4-len(newboard[-1]))*[0] + newboard[-1]

if move == 1:
    newboard = [[], [], [], []]
    for col in range(len(board[0])):
        newLine = []
        for line in range(len(board)):
            holderBoard = []
            if board[line][col] == 0:
                pass
            else:
                if len(newLine) == 0:
                    newLine.append(board[line][col])
                elif board[line][col] == board[line-1 - getColPrevious(board, col, line)][col] and board[line][col] == newLine[-1]:
                    newLine[-1] *= 2
                else:
                    newLine.append(board[line][col])
        newLine += (4 - len(newLine)) * [0]
        holderBoard.append(newLine)
        left = 4 - len(holderBoard[-1])
        for z in range(len(holderBoard[-1])):
            newboard[z] += [holderBoard[-1][z]]
if move == 3:
    newboard = [[], [], [], []]
    for col in range(len(board[0])):
        newLine = []
        for line in range(len(board)-1, -1, -1):
            holderBoard = []
            if board[line][col] == 0:
                pass
            else:
                if len(newLine) == 0:
                    newLine.append(board[line][col])
                elif board[line][col] == board[line+1 + getColAfter(board, col, line)][col] and board[line][col] == newLine[-1]:
                    newLine[-1] *= 2
                else:
                    newLine.append(board[line][col])
        newLine.reverse()
        newLine = (4 - len(newLine)) * [0] + newLine
        holderBoard.append(newLine)
        left = 4 - len(holderBoard[-1])
        for z in range(len(holderBoard[-1])):
            newboard[z] += [holderBoard[-1][z]]
for line in newboard:
    print(" ".join(map(str, line)))
