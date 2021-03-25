import sys
for line in sys.stdin:
    left = False
    right = False
    for char in line.strip():
        binary = str(format(ord(char), 'b'))
        if binary.count('1') % 2 == 1:
            left = not left
        else:
            right = not right
    print("trapped" if left or right else "free")