nums = [3, 34, 4, 12, 5, 2]
summ = 9
n = len(nums)

dp = [[False for _ in range(summ + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = True

for i in range(1, n + 1):
    for j in range(1, summ + 1):
        if nums[i-1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - nums[i - 1]])
print(dp[n][summ])