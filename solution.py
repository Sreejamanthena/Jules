import sys

def solve():
    try:
        # Fast I/O
        def get_ints():
            return list(map(int, sys.stdin.readline().strip().split()))
        def get_string():
            return sys.stdin.readline().strip()

        R_str = get_string()
        if not R_str:
            print(0)
            return
        R = int(R_str)

        if R == 0:
            print(0)
            return

        C = int(get_string())
        K = int(get_string())
        S = [get_string() for _ in range(R)]
    except (IOError, ValueError):
        # Handle empty input for local testing
        R, C, K, S = 0, 0, 0, []
        if R == 0:
            print(0)
            return

    # Helper to convert char to 0-25 index
    def char_to_int(c):
        return ord(c) - ord('a')

    # 1. Precomputation
    cost = [[[0] * 26 for _ in range(26)] for _ in range(R)]
    max_len_in_string = [[0] * 26 for _ in range(R)]

    for i in range(R):
        s = S[i]

        # Calculate cost[i] and max_len_in_string[i] in one pass
        dp_cost_s = [[0] * 26 for _ in range(26)]
        for j in range(C):
            c_val = char_to_int(s[j])

            # This char can start a new subsequence of length 1
            dp_cost_s[c_val][c_val] = max(dp_cost_s[c_val][c_val], 1)

            # This char can extend existing subsequences
            for start_c_idx in range(26):
                max_prev_len = 0
                for prev_c_idx in range(max(0, c_val - K), min(26, c_val + K + 1)):
                    if dp_cost_s[start_c_idx][prev_c_idx] > 0:
                        max_prev_len = max(max_prev_len, dp_cost_s[start_c_idx][prev_c_idx])

                if max_prev_len > 0:
                    new_len = 1 + max_prev_len
                    dp_cost_s[start_c_idx][c_val] = max(dp_cost_s[start_c_idx][c_val], new_len)

        cost[i] = dp_cost_s
        for start_c in range(26):
            for end_c in range(26):
                max_len_in_string[i][end_c] = max(max_len_in_string[i][end_c], cost[i][start_c][end_c])


    # 2. Main DP
    dp = [[0] * 26 for _ in range(1 << R)]
    ans = 0

    # Base cases
    for i in range(R):
        mask = 1 << i
        for c_idx in range(26):
            dp[mask][c_idx] = max_len_in_string[i][c_idx]
            ans = max(ans, dp[mask][c_idx])

    # Iterations
    for mask in range(1, 1 << R):
        for prev_c_idx in range(26):
            if dp[mask][prev_c_idx] > 0:
                for i in range(R):
                    if not (mask & (1 << i)):
                        next_mask = mask | (1 << i)
                        for start_c_idx in range(max(0, prev_c_idx - K), min(26, prev_c_idx + K + 1)):
                            for end_c_idx in range(26):
                                if cost[i][start_c_idx][end_c_idx] > 0:
                                    new_len = dp[mask][prev_c_idx] + cost[i][start_c_idx][end_c_idx]
                                    if new_len > dp[next_mask][end_c_idx]:
                                        dp[next_mask][end_c_idx] = new_len
                                    ans = max(ans, new_len)

    print(ans)

if __name__ == "__main__":
    solve()
