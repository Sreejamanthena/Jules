import sys

def secureMaximumDeliveries(deliveryLogs, k):
    if not deliveryLogs or k == 0:
        return 0

    half_k = k // 2
    max_secure = 0

    max_log = max(deliveryLogs)
    if max_log == 0:
        return 0

    for x in range(1, max_log + 1):
        Q = 0
        # Use a frequency array for remainders to optimize sorting
        remainder_freq = [0] * x
        for log in deliveryLogs:
            Q += log // x
            r = log % x
            if r > 0:
                remainder_freq[r] += 1

        if Q >= half_k:
            # We need half_k warehouses >= x for the compromised set.
            # We take exactly half_k warehouses of size x for compromised.
            # Then we have half_k safe warehouses left to fill.
            # Available warehouses for safe slots:
            # (Q - half_k) warehouses of size x
            # plus remainders of size < x

            count_x = Q - half_k
            if count_x >= half_k:
                current_sum = half_k * x
            else:
                current_sum = count_x * x
                needed = half_k - count_x
                # Fill the remaining safe slots with the largest possible remainders
                for r_val in range(x - 1, 0, -1):
                    if remainder_freq[r_val] > 0:
                        take = min(needed, remainder_freq[r_val])
                        current_sum += take * r_val
                        needed -= take
                        if needed == 0:
                            break

            if current_sum > max_secure:
                max_secure = current_sum

    return max_secure

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    try:
        n = int(input_data[0])
        deliveryLogs = []
        for i in range(n):
            deliveryLogs.append(int(input_data[i+1]))
        
        k = int(input_data[n+1])
        print(secureMaximumDeliveries(deliveryLogs, k))
    except (ValueError, IndexError):
        pass

if __name__ == '__main__':
    solve()
