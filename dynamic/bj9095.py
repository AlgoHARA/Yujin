t = int(input())
dp = [0, 1, 2, 4]

for i in range(4, 11):
    # dp[4] -> (dp[3] + 1) + (dp[2] + 2) + (dp[1] + 3)
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for _ in range(t):
    print(dp[int(input())])
