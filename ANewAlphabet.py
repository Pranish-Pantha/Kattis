newAlp = {
    'a': '@',
    'b': '8',
    'c': '(',
    'd': '|)',
    'e': '3',
    'f': '#',
    'g': '6',
    'h': '[-]',
    'i': '|',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '[]\/[]',
    'n': '[]\[]',
    'o': '0',
    'p': '|D',
    'q': '(,)',
    'r': '|Z',
    's': '$',
    't': "']['",
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '}{',
    'y': '`/',
    'z': '2'
}
line = input()
string = ''
for char in line:
    if char.lower() in newAlp.keys():
        string += newAlp[char.lower()]
    else:
        string += char

print(string)
