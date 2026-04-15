import sys

def secureMaximumDeliveries(deliveryLogs, k):
    n = len(deliveryLogs)
    max_secure = 0
    half_k = k // 2

    # The maximum value of X is bounded by the maximum delivery log value,
    # as any larger X would result in C = 0 < half_k (since k >= 2).
    max_log = 0
    if n > 0:
        max_log = max(deliveryLogs)

    for X in range(1, max_log + 1):
        C = 0
        remainders = []
        for log in deliveryLogs:
            q = log // X
            r = log % X
            C += q
            remainders.append(r)
        
        if C >= half_k:
            # Number of X-sized blocks we can afford to put in the safe group.
            # We must reserve at least half_k blocks of size at least X for the compromised group.
            # Since each X-block is exactly size X, and we want to maximize the safe group,
            # we use as many X-blocks as possible for the safe group, up to half_k.
            num_X_safe = min(half_k, C - half_k)

            current_sum = num_X_safe * X

            # We need a total of half_k warehouses in the safe group.
            needed = half_k - num_X_safe

            if needed > 0:
                # To maximize the sum, we pick the largest available remainders.
                # Each log can provide at most one remainder warehouse after its X-blocks are used.
                remainders.sort(reverse=True)
                # We can only take as many remainders as there are logs.
                for i in range(min(needed, n)):
                    current_sum += remainders[i]

            if current_sum > max_secure:
                max_secure = current_sum

    return max_secure

def solve():
    # Use sys.stdin.read().split() for fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    deliveryLogs = []
    for i in range(n):
        deliveryLogs.append(int(input_data[i+1]))

    # k is the last element
    k = int(input_data[n+1])

    print(secureMaximumDeliveries(deliveryLogs, k))

if __name__ == '__main__':
    solve()
