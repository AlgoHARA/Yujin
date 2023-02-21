# 소요시간: 12분

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

weight = 0
for i in range(n):
    weight = max(weight, arr[i] * (n - i))
    
print(weight)
