cup = [1, 2, 3]
for i in range(int(input())):
    x,y = map(int,input().split())
    x1 = cup.index(x)
    y1 = cup.index(y)
    cup[x1], cup[y1] = cup[y1], cup[x1]
print(cup[0])