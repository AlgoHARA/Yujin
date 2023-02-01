# 11721 - 열 개씩 끊어 출력하기
# 풀이 1

string = input()

n = len(string) // 10 # 입력받은 문자열 길이에서 십의자릿수만 제외

for i in range(1, n+1): # 반복문 안에서 10글자씩 출력
    print(string[(i-1)*10:i*10])
    
print(string[n*10:]) # 반복문 종료 시 나머지 출력
