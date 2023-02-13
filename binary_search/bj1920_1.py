# 소요시간: 약 1시간 반

import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split()))
m = int(input())
targetList = list(map(int, input().split()))

numList.sort()

def search(low, high, target):
    mid = (low + high) // 2
    
    # 정수를 찾은 경우
    if(numList[mid] == target):
        return 1
    
    # 정수를 찾지 못한 경우
    if(low > high): # 배열 안에 해당 수가 없을 때
        return 0
    
    if(numList[mid] > target): # target이 mid보다 작을 때
        return search(low, mid - 1, target)
    else: # target이 mid보다 클 때
        return search(mid + 1, high, target)
       
for target in targetList:
    print(search(0, n-1, target))
