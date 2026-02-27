import sys
from collections import deque

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    try:
        N = int(next(it))
        M = int(next(it))
        source = int(next(it))
        target = int(next(it))

        cursed = []
        # The cursed status can be N space-separated integers or a single string of length N
        # We try to handle both by reading until we have N integers
        while len(cursed) < N:
            val = next(it)
            if len(val) > 1 and len(cursed) == 0:
                cursed.extend([int(c) for c in val])
            else:
                cursed.append(int(val))

        # In case we read more than N due to the string logic
        cursed = cursed[:N]

        adj = [[] for _ in range(N)]
        for _ in range(M):
            try:
                u = int(next(it))
                v = int(next(it))
                if u < N and v < N:
                    adj[u].append(v)
                    adj[v].append(u)
            except StopIteration:
                break
    except StopIteration:
        pass

    # Basic checks
    if source < 0 or source >= N or target < 0 or target >= N:
        print("-1")
        return

    if cursed[source] == 1 or cursed[target] == 1:
        print("-1")
        return

    if source == target:
        print("0")
        return

    # BFS for shortest path
    queue = deque([(source, 0)])
    visited = [False] * N
    visited[source] = True

    while queue:
        u, dist = queue.popleft()
        
        if u == target:
            print(dist)
            return

        for v in adj[u]:
            if not visited[v] and cursed[v] == 0:
                visited[v] = True
                queue.append((v, dist + 1))

    print("-1")

if __name__ == "__main__":
    solve()
