num = int(input())
axiom = set()
output = "correct"
for n in range(num):
    line = input()
    if line[0] == "-":
        axiom.add(line[3:])
    else:
        assume = line.split()
        check = set(assume[:assume.index("->")])
        if check.issubset(axiom):
            axiom.add(assume[-1])
        else:
            print(n+1)
            exit()
print(output)
