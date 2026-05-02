'''
problem link: https://cses.fi/problemset/task/1083
'''

n = int(input())

nums = list(map(int, input().split()))[:n-1]

expectedSum = n * (n + 1) // 2

print(expectedSum - sum(nums))