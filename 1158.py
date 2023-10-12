import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [_ for _ in range(1, n+1)]
result = []
num = 0

for i in range(n):
    num += k-1
    if num >= len(arr):
        num = num%len(arr)
    result.append(str(arr.pop(num)))
print('<'+', '.join(result)+'>')