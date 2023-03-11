from math import inf
import sys

n, m, b = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tall = 0
ans = inf

for i in range(257): # 땅의 높이의 최대는 256이므로 0 ~ 256까지만 탐색
    get_block = 0
    use_block = 0
    for j in range(n): # 가로
        for k in range(m): # 세로
            if arr[j][k] < i: # 블럭이 현재 높이 보다 작다면
                use_block += (i - arr[j][k]) # 현재 높이가 블록 높이보다 높을 때 (use_block 만큼 인벤토리에서 꺼내서 채워야 함)

            else:
                get_block += (arr[j][k] - i) # 블록 높이가 현재 높이보다 높을 때 (get_block 만큼 블록이 제거된 후 인벤토리에 들어감)

    inventory = get_block + b # 인벤토리에 있는 총 블록수 = 현재 인벤토리에 있는 블록 + get_block

    if inventory < use_block: # 전부 채울 수 없으므로 패스
        continue

    time = 2 * get_block + use_block # 블록 제거는 2초, 블록 추가는 1초
    
    if time <= ans: # 높이는 0 ~ 256 까지 오름차순으로 탐색하기 때문에 걸린 시간이 같아도 더 높은 높이가 출력 된다
        ans = time
        tall = i

print(ans, tall)
