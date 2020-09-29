n = int(input())
c = 0
while n > 0:
    s = n % 10
    if s == 7 or s == 4:
        c = c+1
    n = n//10
if c == 7 or c == 4:
    print("YES")
else:
    print("NO")