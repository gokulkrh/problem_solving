n = int(input())
q = []
for i in range(n):
    e = input()
    q.append(e)
c = 0
p = q[0]
for i in q:
    w = q.count(i)
    if w > c:
        c = w
        p = i
print(p)
