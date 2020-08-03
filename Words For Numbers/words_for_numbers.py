import sys
numToNum = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
            11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
            19: "nineteen"}
NumToNUM = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
            7: "seventy", 8: "eighty", 9: "ninety"}
for line in sys.stdin:
    text = line.split()
    string = []
    for x in range(len(text)):
        temp = text[x]
        if temp.isdigit():
            if int(temp) < 20:
                temp = numToNum.get(int(temp))
            else:
                a, b = list(str(temp))[0], list(str(temp))[1]
                a = [NumToNUM.get(int(a))]
                if int(b) != 0:
                    a += [numToNum.get(int(b))]
                temp = "-".join(a)
            if x == 0:
                string.append(temp.capitalize())
            else:
                string.append(temp)
        else:
            string.append(temp)
    print(" ".join(string))
