num = int(input())
for n in range(num):
    cases = list(map(int, input().split()))
    total = cases[0]
    cases = cases[1:]
    average = sum(cases) / total
    answer = sum(map(lambda x: 1 if x>average else 0, cases)) / total
    answer = round(answer*100, 3)
    print(f'{answer:.3f}%')
