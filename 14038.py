arr = [input() for i in range(6)]
cnt = arr.count('W')
if cnt >= 5:
    print(1)
elif cnt >= 3:
    print(2)
elif cnt >= 1:
    print(3)
else:
    print(-1)