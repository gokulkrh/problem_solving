n = int(input())
c = 0
for i in range(n):
    a = list(map(int, input().split()))
    q = 0
    for j in a:
        if j == 1:
            q += 1
    if q >= 2:
        c += 1

print(c)