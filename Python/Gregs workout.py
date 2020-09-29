n = int(input())
a = list(map(int, input().split()))[:n]

ch = sum(a[0::3])
bc = sum(a[1::3])
bk = sum(a[2::3])

max = "chest"

if bc > ch and bc > bk:
    max = "biceps"
elif bk > ch and bk > bc:
    max = "back"


print(max)
