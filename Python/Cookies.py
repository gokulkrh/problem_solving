n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(0,len(a)):
    r = a[0]
    a.pop(0)
    q = sum(a)
    a.append(r)
    if q%2==0:
        c += 1
print(c)