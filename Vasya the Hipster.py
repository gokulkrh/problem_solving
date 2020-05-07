a, b = map(int, input().split())
if a<b:
    c = b-a
    print(a, c//2)
else:
    c = a-b
    print(b, c//2)