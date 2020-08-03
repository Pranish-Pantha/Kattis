N, t = map(int, input().split())
arr = list(map(int, input().split()))
if t == 1:
    print(7)
elif t == 2:
    if arr[0] > arr[1]:
        print("Bigger")
    elif arr[0] == arr[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    temp = sorted(arr[:3])[1]
    print(temp)
elif t == 4:
    print(sum(arr))
elif t == 5:
    temp = arr[:]
    print(sum(map(lambda x: x*(1-(x % 2)), temp)))
elif t == 6:
    temp = arr[:]
    alpha = {
    0: "a",
     1: "b",
      2: "c",
       3: "d",
        4:"e",
         5:"f",
          6:"g",
           7:"h",
            8:"i",
             9:"j",
              10: "k",
               11:"l",
                12:"m",
                 13:"n",
                  14:"o",
                   15:"p",
                    16:"q",
                     17:"r",
                      18:"s",
                       19:"t",
                        20:"u",
                         21:"v",
                          22:"w",
                           23:"x",
                            24:"y",
                             25:"z"}
    temp = map(lambda x: x % 26, temp)
    temp = map(lambda x: alpha.get(x), temp)
    print("".join(temp))
elif t == 7:
    passed = {0}
    i = 0
    while 0<=i<=N-1:
        i = arr[i]
        if i > N-1:
            print("Out")
            break
        elif i == N-1:
            print("Done")
            break
        elif len(passed.intersection({i})) > 0:
            print("Cyclic")
            break
        passed.add(i)
