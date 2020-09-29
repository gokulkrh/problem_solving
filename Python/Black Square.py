a, b, c, d = map(int, input().split())
q = 0
n = int(input())
p = list(map(int, str(n)))
for i in p:
    if i == 1:
        q += a
    elif i ==2:
        q += b
    elif i ==3:
        q += c
    elif i == 4:
        q += d

print(q)