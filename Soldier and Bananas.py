k, n, w = map(int, input().split())
c = ((w*(w+1)) * k)//2
print(max(c-n, 0))