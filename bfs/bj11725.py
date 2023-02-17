# 소요시간: 70분

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
queue = deque([1])
parent = [1, 1] + [0] * (n - 1) # 각 index번째 노드의 부모 리스트(0으로 초기화)

while(len(queue) > 0):
    pop = queue.popleft()
    for i in range(len(graph[pop])): # graph[pop][i] => 6, 4
        if(parent[graph[pop][i]] == 0): # 부모 없을 시
            parent[graph[pop][i]] = pop # 갱신
            queue.append(graph[pop][i])
        
for i in parent[2:]: # 2번째 노드부터 부모 노드 출력
    print(i)
