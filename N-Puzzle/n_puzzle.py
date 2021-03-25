def findPos(arr, char):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == char:
                return r, c

ideal = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', '.']
]
board = []
for line in range(4):
    board.append(list(input()))
iterable = sum(ideal, [])
scatter = 0
for char in iterable:
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == '.':
                continue
            if col == char:
                r0, c0 = findPos(ideal, char)
                scatter += abs(r0-r) + abs(c0-c)
print(scatter)
