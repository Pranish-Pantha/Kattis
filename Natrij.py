time1 = input().split(":")
time2 = input().split(":")

seconds = minutes = hours = 0
if int(time1[2]) > int(time2[2]):
    time1[1] = str(int(time1[1]) + 1)
    seconds = int(60 - int(time1[2])) + int(time2[2])
else:
    seconds = int(time2[2]) - int(time1[2])
if int(time1[1]) > int(time2[1]):
    time1[0] = str(int(time1[0]) + 1)
    minutes = int(60 - int(time1[1])) + int(time2[1])
else:
    minutes += int(time2[1]) - int(time1[1])
if int("".join(time1)) < int("".join(time2)):
    hours += int(time2[0]) - int(time1[0])
else:
    hours += (24 - int(time1[0]) + int(time2[0]))

hours = list(str(hours))
if len(hours) < 2:
    hours.insert(0, "0")
minutes = list(str(minutes))
if len(minutes) < 2:
    minutes.insert(0, "0")
seconds = list(str(seconds))
if len(seconds) < 2:
    seconds.insert(0, "0")
print("".join(hours) + ":" + "".join(minutes) + ":" + "".join(seconds))
