from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

q = deque([])
visited = []
res = 0

def bfs(v):
    q.append(v)
    while(q):
        node = q.popleft()
        if(node not in visited):
            q.extend(graph[node])
            visited.append(node)
    visited.append(v)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1-1].append(n2-1)
    graph[n2-1].append(n1-1)
    
for i in range(n): # 모든 정점의 연결요소를 확인
    if(i not in visited): # 방문했다면 연결 요소에 포함된 정점이므로 제외
        bfs(i)
        res += 1 # 연결 요소 개수 추가
    
print(res)
