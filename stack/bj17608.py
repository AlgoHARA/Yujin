import sys

sticks = []
n = int(input())

sticks.append(int(input())) # 첫번째 막대

for i in range(n - 1):
    curStick = int(sys.stdin.readline()) # sys.stdin.readline() = input()과 유사(여러 줄 입력 받을 때 시간초과 방지)
    while(sticks[-1] <= curStick): # 마지막 막대가 새 막대보다 짧거나 같을 때
        sticks.pop() # 마지막 막대 제거
        if(len(sticks) == 0):
            break
    sticks.append(curStick)
    
print(len(sticks))
