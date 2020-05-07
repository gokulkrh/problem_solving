n, h = map(int, input().split())
a = list(map(int, input().split()))[:n]
t = 0
s = 0
for i in a:
    if i <= h:
        s += 1
    else:
        t += 1

print(s+2*t)