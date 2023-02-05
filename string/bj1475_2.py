# 풀이2

roomNum = input()
numCnt = [0] * 9

for n in range(len(roomNum)):
    if (int(roomNum[n]) == 9): # 9의 개수는 6의 개수에 포함
        numCnt[6] += 1
    else:
        numCnt[int(roomNum[n])] += 1
        
numCnt[6] = (numCnt[6] + 1) // 2
