n = int(input())
s = 0
r = 0
while(n%5!=0):
    n = n-1
    r += 1
if n%5==0:
    s += n//5
if r == 0:
    print(s)
else:
    print(s+1)