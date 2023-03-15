n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

for i in range(1, len(arr[0])+1):
    if(len(set(num[-i:] for num in arr)) == n): # 슬라이싱 후 set으로 중복 제거
        print(i)
        break
