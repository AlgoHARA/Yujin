# 소요시간: 약 2시간

n, m = map(int, input().split()) # 3, 5
arr = [[] for _ in range(n)] # [[],[],[]]

for i in range(n):
    nums = input()
    for j in range(len(nums)):
        arr[i].append(int(nums[j]))

width = min(n, m) # 정사각형 변의 길이

def find(width, arr):
    for i in range(len(arr) - width + 1):
        for j in range(len(arr[0]) - width + 1):
            if(width == 1): # 변의 길이가 1까지 줄어들었을 시 무조건 최대 넓이가 1이므로 탐색할 필요없음
                return 1
            if(arr[i][j] == arr[i][j+width-1] == arr[i+width-1][j] == arr[i+width-1][j+width-1]):
                return width * width
                
    return find(width - 1, arr) # 위 코드에서 return 호출이 없었을 시 width 크기를 1 감소하여 재귀 실행

print(find(width, arr))
