arr = []
false1 = 0
false2 = 0

for _ in range(9):
    ans = int(input())
    arr.append(ans)

arr.sort()

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)): 
        if(sum(arr) - (arr[i] + arr[j]) == 100): # i, j번째를 제외한 나머지 합이 100이면
            false1 = arr[i]
            false2 = arr[j]

for i in arr:
    if (i != false1 and i !=false2): # i, j번째 사람을 제외하여 출력
        print(i)
