user = []
for x in range(7):
    line = input()
    length = len(line)
    for y in range((length+1) // 6):
        user.append(line[y*6: y*6 + 5])
final = []
length = len(user) // 7
for x in range(length):
    line = []
    for y in range(7):
        line.append(user[y*length + x])
    final.append(line)

numbers = {
"xxxxxx...xx...xx...xx...xx...xxxxxx":0,
"....x....x....x....x....x....x....x":1,
"xxxxx....x....xxxxxxx....x....xxxxx":2,
"xxxxx....x....xxxxxx....x....xxxxxx":3,
"x...xx...xx...xxxxxx....x....x....x":4,
"xxxxxx....x....xxxxx....x....xxxxxx":5,
"xxxxxx....x....xxxxxx...xx...xxxxxx":6,
"xxxxx....x....x....x....x....x....x":7,
"xxxxxx...xx...xxxxxxx...xx...xxxxxx":8,
"xxxxxx...xx...xxxxxx....x....xxxxxx":9,
".......x....x..xxxxx..x....x.......":-1
}
inv_map = {v: k for k, v in numbers.items()}
first = []
second = []
for num in final:
    number = numbers.get("".join(map(str,num)))
    if number == -1:
        for n in final[final.index(num) + 1:]:
            second.append(numbers.get("".join(map(str,n))))
        break
    else:
        first.append(number)
first = int("".join(map(str,first)))
second = int("".join(map(str,second)))

answer = first + second
answer = list(map(int, list(str(answer))))
output = []
for x in answer:
    output.append(inv_map.get(x))

for row in range(7):
    line = []
    for col in range(len(output)):
        line.append(output[col][row*5: row*5 + 5])
        line.append(".")
    print("".join(line[:-1]))
