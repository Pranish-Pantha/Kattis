length, s = map(int, input().split())
inputs = list(map(int, input().split()))
flipDic = {
'1': '1',
'2': '2',
'3': '-1',
'4': '-1',
'5': '5',
'6': '9',
'7': '-1',
'8': '8',
'9': '6',
'0': '0'
}
output = "NO"
def flip(x):
    string = ""
    for char in str(x):
        z = flipDic.get(char)
        if int(z) > -1:
            string += z
        else:
            return 0
    return int("".join(string)[::-1])

m = set()
for item in inputs:
    flipped = flip(item)
    sub = {item, flipped}
    if m.intersection(sub):
        output = "YES"
    else:
        m.update([s-item, s-flipped])
print(output)
