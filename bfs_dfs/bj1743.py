from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())
graph = [[False for _ in range(m)] for _ in range(n)]
visited = set()

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = True # 음식물

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, visited):
    cnt = 1
    q = deque([(i, j)])
    visited.add((i, j))
    
    while(q):
        x, y = q.popleft()
        
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
                
            # 좌표가 범위 내에 존재 & 방문하지 않은 좌표 & 해당 좌표값이 1일 경우
            if(0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and graph[nx][ny]):
                q.append((nx, ny))
                visited.add((nx, ny))
                cnt += 1
    return cnt

max_cnt = 0 # 제일 큰 음식물의 크기

for i in range(n):
    for j in range(m):
        if((i, j) not in visited and graph[i][j]):
            max_cnt = max(bfs(i, j, visited), max_cnt)

print(max_cnt)
