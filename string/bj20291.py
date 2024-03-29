import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    file = input().rstrip() # 개행문자 제거
    extension = file[file.find('.') + 1:] # 확장자명

    if extension in dic.keys():
        dic[extension] += 1
    else:
        dic[extension] = 1

for i in sorted(dic.items()):
    print(i[0], i[1])
