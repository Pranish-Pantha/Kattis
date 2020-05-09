import math
constant = input()
length = len(constant)
specialDictionary = {"1": 1, "2": 2, "6": 3, "24": 4, "120": 5, "720": 6}
if constant in specialDictionary.keys():
    print(specialDictionary[constant])
else:
    for i in range(205016):
        x = i + 7
        lognum = math.log10(x)
        if math.floor((0.5 * (lognum + 0.798179868358115)) + (x * (lognum - 0.4342944819032518)) + 1) == length:
            print(x)
            break
