q = []
for i in range(5):
    a = list(map(int, input().split()))
    q.append(a)

ans = 0
for i in q:
    r = q.index(i)
    for j in i:
        if j == 1:
            if r == 0 or r == 4:
                ans += 2
            if r == 1 or r == 3:
                ans += 1
            e = i.index(j)
            if e == 0 or e == 4:
                ans += 2
            if e == 1 or e == 3:
                ans += 1

print(ans)
