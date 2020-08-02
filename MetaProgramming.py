import sys
vals = {}
for line in sys.stdin:
    if line[0] == "d":
        temp= line.split()
        num = int(temp[1])
        name = temp[2]
        vals.update({name: num})
    else:
        temp = line.split()
        if temp[1] in vals.keys() and temp[3] in vals.keys():
            compar = vals.get(temp[1])
            compar2 = vals.get(temp[3])
            if temp[2] == "=":
                if compar == compar2:
                    print("true")
                else:
                    print("false")
            elif temp[2] == ">":
                if compar > compar2:
                    print("true")
                else:
                    print("false")
            else:
                if compar < compar2:
                    print("true")
                else:
                    print("false")
        else:
            print("undefined")
