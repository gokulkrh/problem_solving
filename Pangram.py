import string
u = string.ascii_letters

n = int(input())
s = input()[:n]
s = s.lower()
p = []
for i in s:
    if i in u and i not in p:
        p.append(i)
if len(p)==26:
    print("YES")
else:
    print("NO")