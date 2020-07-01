UserInput = input().split()
password = UserInput[0]
test = UserInput[1]
looking = list(password[:])
length = 0
Pass = "FAIL"
for x in test:
    if x in looking:
        if x == looking[0]:
            length += 1
            looking.pop(0)
            if length == len(password):
                Pass = "PASS"
                break
        else:
            break

print(Pass)
