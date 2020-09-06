equation = {}
numToOperation = {0: "+", 1: "-", 2: "//", 3: "*"}


def generate(a, b, c):
    global equation
    a = numToOperation[a]
    b = numToOperation[b]
    c = numToOperation[c]
    string = "4 " + a + " 4 " + b + " 4 " + c + " 4"
    equation.update({string: eval(string)})


for i in range(4):
    for j in range(4):
        for k in range(4):
            generate(i, j, k)

n = int(input())
for x in range(n):
    test = int(input())
    for key, item in equation.items():
        if item == test:
            key = key.replace("//", "/")
            print(f"{key} = {test}")
            break
    else:
        print("no solution")
