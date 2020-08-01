num = int(input())
dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
whiteField = [[0, 0, 0, 21, 12, 0, 0, 0],
 [0, 0, 41, 32, 23, 14, 0, 0],
  [0, 61, 52, 43, 34, 25, 16, 0],
   [81, 72, 63, 54, 45, 36, 27, 18],
   [0, 83, 74, 65, 56, 47, 38, 0],
   [0, 0, 85, 76, 67, 58, 0, 0],
   [0, 0, 0, 87, 78, 0, 0, 0]]
blackField = [[0, 0, 0, 11, 0, 0, 0],
[0, 0, 31, 22, 13, 0, 0],
[0, 51, 42, 33, 24, 15, 0],
[71, 62, 53, 44, 35, 26, 17],
[82, 73, 64, 55, 46, 37, 28],
[0, 84, 75, 66, 57, 48, 0],
[0, 0, 86, 77, 68, 0, 0],
[0, 0, 0, 88, 0, 0, 0]]
invDict = {y: x for x, y in dictionary.items()}

for x in range(num):
    x1, y1, x2, y2 = input().split()
    x1, x2 = dictionary.get(x1), dictionary.get(x2)
    y1, y2 = int(y1), int(y2)
    if x1 % 2 == y1 % 2:
        StartBlack = True
    else:
        StartBlack = False
    if x2 % 2 == y2 % 2:
        EndBlack = True
    else:
        EndBlack = False
    if not StartBlack and not EndBlack:
        movesArr = [invDict.get(x1), y1]
        moves = 0
        start = str(x1) + str(y1)
        rowS = int((x1 + y1 + 1)/2 - 2)
        columnS = whiteField[rowS].index(int(start))
        end = str(x2) + str(y2)
        rowE = int((x2 + y2 + 1)/2 -2)
        columnE = whiteField[rowE].index(int(end))

        if rowS == rowE and columnS == columnE:
            pass
        elif rowS == rowE:
            moves += 1
            res = str(whiteField[rowS][columnE])
            movesArr += [invDict.get(int(res[0])), int(res[1])]
        elif columnS == columnE:
            moves += 1
            res = str(whiteField[rowE][columnS])
            movesArr += [invDict.get(int(res[0])), int(res[1])]
        else:
            if whiteField[rowE][columnS] == 0:
                moves += 2
                res = str(whiteField[rowS][columnE])
                movesArr += [invDict.get(int(res[0])), int(res[1])]
                movesArr += [invDict.get(x2), y2]
            else:
                moves += 2
                res = str(whiteField[rowE][columnS])
                movesArr += [invDict.get(int(res[0])), int(res[1])]
                movesArr += [invDict.get(x2), y2]

        print(moves, " ".join(map(str, movesArr)))
    elif StartBlack and EndBlack:
        movesArr = [invDict.get(x1), y1]
        moves = 0
        start = str(x1) + str(y1)
        rowS = int((x1 + y1)/2 - 1)
        columnS = blackField[rowS].index(int(start))
        end = str(x2) + str(y2)
        rowE = int((x2 + y2)/2 -1)
        columnE = blackField[rowE].index(int(end))

        if rowS == rowE and columnS == columnE:
            pass
        elif rowS == rowE:
            moves += 1
            res = str(blackField[rowS][columnE])
            movesArr += [invDict.get(int(res[0])), int(res[1])]
        elif columnS == columnE:
            moves += 1
            res = str(blackField[rowE][columnS])
            movesArr += [invDict.get(int(res[0])), int(res[1])]
        else:
            if blackField[rowE][columnS] == 0:
                moves += 2
                res = str(blackField[rowS][columnE])
                movesArr += [invDict.get(int(res[0])), int(res[1])]
                movesArr += [invDict.get(x2), y2]
            else:
                moves += 2
                res = str(blackField[rowE][columnS])
                movesArr += [invDict.get(int(res[0])), int(res[1])]
                movesArr += [invDict.get(x2), y2]
        print(moves, " ".join(map(str, movesArr)))
    else:
        print("Impossible")
