room_num = str(input())
arr = []

for i in range(10):
    arr.append(room_num.count(str(i)))

sixnine = (arr[6] + arr[9] + 1) // 2 # 6, 9 개수만 보았을 때 필요한 세트 수 (ex. 666999 -> 3)
arr[6], arr[9] = 0, 0 # 6, 9 제외

if (max(arr) < sixnine):
    print(sixnine)
else: # 6, 9 제외한 다른 수가 최빈값일 때 (ex.1111169 -> 5)
    print(max(arr)) 
