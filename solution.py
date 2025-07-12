def count_ranges(arr):
    if not arr:
        return 0
    s = set(arr)
    count = 0
    for x in arr:
        if x - 1 not in s:
            count += 1
    return count

def solve():
    N = int(input())
    K = int(input())
    P = [int(input()) for _ in range(N)]

    ranges_memo = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(i, N):
            subarray = P[i:j+1]
            ranges_memo[i][j] = count_ranges(subarray)

    dp = [[-1] * (K + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 0

    for j in range(1, K + 1):
        for i in range(1, N + 1):
            for k in range(i):
                if dp[k][j - 1] != -1:
                    if dp[i][j] < dp[k][j - 1] + ranges_memo[k][i-1]:
                         dp[i][j] = dp[k][j - 1] + ranges_memo[k][i-1]

    ans = 0
    for i in range(1, N + 1):
        if dp[i][K] > ans:
            ans = dp[i][K]
    print(ans)

if __name__ == '__main__':
    solve()
