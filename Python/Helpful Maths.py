import string
c = string.digits

s = input()
b = []
for i in s:
    if i in c:
        b.append(i)

b.sort()
ans = ""
for i in b:
    ans += i
    ans += "+"
ans = list(ans)
ans.pop(len(ans)-1)
p = ""
for i in ans:
    p += i
print(p)