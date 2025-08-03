import math

class Solution:
    """
    Solves the findEnergy problem.
    """
    def findEnergy(self, A):
        """
        Calculates the minimum energy to produce A lines of text.
        :param A: An integer representing the target number of lines.
        :return: An integer representing the minimum energy required.
        """
        if A == 1:
            return 0
        
        dp = [0] * (A + 1)

        for i in range(2, A + 1):
            # Initialize with a safe upper bound (select 1, paste i-1 times)
            dp[i] = i

            # Iterate through all possible previous states j
            for j in range(1, i):
                lines_to_add = i - j

                # Operation: Select All
                # This is only possible if lines_to_add is a multiple of j
                if lines_to_add % j == 0:
                    m = lines_to_add // j
                    cost = dp[j] + 1 + m # 1 for select all, m for pastes
                    dp[i] = min(dp[i], cost)

                # Operation: Select k from top
                # Iterate through all possible selection sizes k
                # k must be a divisor of lines_to_add
                # k must be less than or equal to j
                for k in range(1, int(math.sqrt(lines_to_add)) + 1):
                    if lines_to_add % k == 0:
                        # First factor pair: k and m1
                        m1 = lines_to_add // k
                        if k <= j:
                            cost1 = dp[j] + k + m1
                            dp[i] = min(dp[i], cost1)

                        # Second factor pair: m1 and k
                        k2 = lines_to_add // k
                        if k2 != k and k2 <= j:
                            cost2 = dp[j] + k2 + k
                            dp[i] = min(dp[i], cost2)

        return dp[A]
