import sys
input = sys.stdin.readline

arr = []
for i in range(int(input())):
    [x,y] = map(int,input().split())
    arr.append([x,y])
arr.sort(key = lambda x:(x[1],x[0]))

for j in arr:
    print(j[0], j[1])