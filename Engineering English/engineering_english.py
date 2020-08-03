import sys
passed = set()
for line in sys.stdin:
    words = line.split()
    toprint = []
    for word in words:
        if passed.intersection({word.lower()}):
            toprint.append(".")
        else:
            toprint.append(word)
            passed.add(word.lower())
    print(" ".join(toprint))
