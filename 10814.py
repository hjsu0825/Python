import sys
input = sys.stdin.readline

lst = []

for i in range(int(input())):
    [a,b] = map(str, input().split())
    lst.append([a, b])
lst.sort()
lst.sort(key=lambda x:x[0])

for j in lst:
    print(j[0], j[1])