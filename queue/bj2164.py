from collections import deque

n = int(input())
q = deque(range(1, n + 1))

if(n == 1): # 주어진 카드가 한 장일 때
    print(n)
else:
    while(True): # 카드가 한 장 남을 때까지 반복
        q.popleft()
        if(len(q) == 1):
            break
        q.rotate(-1)
    print(q[0])
