import sys
input = sys.stdin.readline

stk = []
s = input().rstrip()
chk = False
res = ''

<<<<<<< Updated upstream
for i in s:
    if i == " ":
        while stk:
            res += stk.pop()
        res += i
    elif i == "<":
        while stk:
            res += stk.pop()
        chk = True
        res += i
    elif i == ">":
        chk = False
        res += i
    elif chk:
        res += i
    else:
        stk.append(i)
        
while stk:
    res += stk.pop()
print(res)
=======
for i in range(len(s)):
    string = ''
    if "<" in s[i]:
        print(s[i])
    else:
        for j in s[i]:
            string = j + string
        print(string, end=" ")
>>>>>>> Stashed changes
