num = list(map(int, input().split()))
A = min(num)
C = max(num)
B = (set(num) - {A} - {C}).pop()
order = list(input())
dictionary = {"A": A, "B": B, "C": C}
answer = []
for x in order:
    answer.append(dictionary.get(x))
print(" ".join(map(str, answer)))
