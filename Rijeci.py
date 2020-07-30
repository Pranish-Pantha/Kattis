num = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
Sequence = [0, 1, 1]
for x in range(43):
    Sequence.append(Sequence[-1] + Sequence[-2])
print(f"{Sequence[num-1]} {Sequence[num]}")
