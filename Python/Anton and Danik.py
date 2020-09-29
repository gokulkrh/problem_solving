n = int(input())
s = input()
a = 0
d = 0
for i in s:
    if i == 'A':
        a += 1
    elif i == 'D':
        d += 1
    else:
        print("invalid input")

if a < d:
    print("Danik")
elif a > d:
    print("Anton")
elif a == d:
    print("Friendship")