m, n = map(int, input().split())
tasks = list(map(int, input().split()))
music = list(map(int, input().split()))
tasks.sort()
music.sort()

length = len(music)
count = 0
while tasks and music:
    if tasks[-1] <= music[-1]:
        count += 1
        music.pop(-1)
    tasks.pop(-1)

print(count)
