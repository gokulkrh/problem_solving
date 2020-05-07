n, m = map(int, input().split())
q = []
for i in range(n):
    s = input()[:m]
    q.append(s)
c = 0
for i in range(0,len(q)-1):
    if q[i]==q[i+1]:
        c += 1
for i in q:
    for j in range(0,len(i)-1):
        if i[j]!=i[j+1]:
            c += 1
if c>0:
    print("NO")
else:
    print("YES")