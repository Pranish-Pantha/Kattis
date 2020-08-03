from collections import Counter
N, t = map(int, input().split())
arr = list(map(int, input().split()))
if t == 1:
    answer = "No"
    passed = {7777 - arr[0]}
    for item in arr[1:]:
        if len(passed.intersection({item})) > 0:
            answer = "Yes"
        else:
            passed.add(7777-item)
    print(answer)
if t == 2:
    if len(arr) == len(set(arr)):
        print("Unique")
    else:
        print("Contains duplicate")
if t == 3:
    size = N/2
    check, n = Counter(arr).most_common(1)[0]
    if n > size:
        print(check)
    else:
        print(-1)
if t == 4:
    length = len(arr)
    temp = sorted(arr)
    if len(arr)%2 == 1:
        print(temp[length//2])
    else:
        print(f"{temp[length//2 -1]} {temp[length//2]}")
if t == 5:
    temp = sorted(list(x for x in arr if 100<=x<=999))
    print(" ".join(map(str, temp)))
