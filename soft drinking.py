n, k, l, c, d, p, nl, np = map(int, input().split())
x = min([k*l//nl, c*d, p//np])
y = x//n
print(y)