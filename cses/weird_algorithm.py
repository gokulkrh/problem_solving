'''
problem link: https://cses.fi/problemset/task/1068/
'''

n = int(input())

res = []

while n != 1:
    res.append(str(n))
    
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    
res.append("1")
print(" ".join(res))
