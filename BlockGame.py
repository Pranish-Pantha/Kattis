small, big = sorted(map(int, input().split()))
winA = False
loseA = False
winorlose = ["win", "lose"]
index = 0
YourTurn = 1
while(1):
    if small == 1:
        print(winorlose[index])
        break
    elif big % small == 0:
        print(winorlose[index])
        break
    else:
        num = big // small
        big -= (num) * small
        if num > 1:
            if YourTurn:
                print("win")
                break
            else:
                print('lose')
                break
        big, small = small, big
    index = 1 - index
    YourTurn = 1 - YourTurn
