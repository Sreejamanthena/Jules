def solve():
    R = int(input())
    C = int(input())
    K = int(input())
    S = [input() for _ in range(R)]

    f = [[0] * 26 for _ in range(R)]
    for i in range(R):
        lens = [0] * 26
        for j in range(C):
            char = S[i][j]
            char_code = ord(char) - ord('a')
            max_prev_len = 0
            for c_prev_code in range(26):
                if abs(char_code - c_prev_code) <= K:
                    max_prev_len = max(max_prev_len, lens[c_prev_code])
            lens[char_code] = max(lens[char_code], 1 + max_prev_len)
        f[i] = lens

    h = [[[0] * 26 for _ in range(26)] for _ in range(R)]
    for i in range(R):
        for c_prev_code in range(26):
            lens = [0] * 26
            for j in range(C):
                char = S[i][j]
                char_code = ord(char) - ord('a')
                max_len_ending_at_j = 0
                if abs(char_code - c_prev_code) <= K:
                    max_len_ending_at_j = 1

                max_prev_len_in_s = 0
                for c_in_s_code in range(26):
                    if abs(char_code - c_in_s_code) <= K:
                        max_prev_len_in_s = max(max_prev_len_in_s, lens[c_in_s_code])

                if max_prev_len_in_s > 0:
                    max_len_ending_at_j = max(max_len_ending_at_j, 1 + max_prev_len_in_s)

                lens[char_code] = max(lens[char_code], max_len_ending_at_j)
            h[i][c_prev_code] = lens

    dp = [[0] * 26 for _ in range(1 << R)]

    for i in range(R):
        for c in range(26):
            dp[1 << i][c] = f[i][c]

    for mask in range(1, 1 << R):
        for i in range(R):
            if mask & (1 << i):
                prev_mask = mask ^ (1 << i)
                if prev_mask == 0:
                    continue
                for c_end in range(26):
                    for c_prev in range(26):
                        if dp[prev_mask][c_prev] > 0 and h[i][c_prev][c_end] > 0:
                            dp[mask][c_end] = max(dp[mask][c_end], dp[prev_mask][c_prev] + h[i][c_prev][c_end])

    max_len = 0
    for mask in range(1, 1 << R):
        for c in range(26):
            max_len = max(max_len, dp[mask][c])

    print(max_len)

if __name__ == '__main__':
    solve()
