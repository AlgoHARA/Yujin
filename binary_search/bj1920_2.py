# set 활용

n = int(input())
numList = set(map(int, input().split()))
m = int(input())
targetList = list(map(int, input().split()))

for target in targetList:
    if(target in numList): # O(1)
        print(1)
    else:
        print(0)
