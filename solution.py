import collections

def solve():
    N = int(input())
    adj = collections.defaultdict(list)
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        # Adjust to 0-based indexing for nodes
        adj[u - 1].append((v - 1, w))
        adj[v - 1].append((u - 1, w))

    P, Q = map(int, input().split())
    P -= 1  # Adjust to 0-based indexing
    Q -= 1  # Adjust to 0-based indexing

    # Placeholder for DFS and logic
    # print(f"N: {N}")
    # print(f"adj: {dict(adj)}")
    # print(f"P: {P}, Q: {Q}")

    xor_from_p = [-1] * N
    xor_from_q = [-1] * N

    def dfs(u, current_xor_sum, parent, target_array, graph_adj):
        target_array[u] = current_xor_sum
        for v, weight in graph_adj[u]:
            if v != parent:
                dfs(v, current_xor_sum ^ weight, u, target_array, graph_adj)

    dfs(P, 0, -1, xor_from_p, adj)
    dfs(Q, 0, -1, xor_from_q, adj)

    # print(f"xor_from_p: {xor_from_p}")
    # print(f"xor_from_q: {xor_from_q}")

    # Step 5: Check for path without teleportation
    if xor_from_p[Q] == 0:
        print("YES")
        return

    # Step 6: Check for path with one teleportation.
    # The condition for a successful path with one teleport is:
    # xor_from_p[u_current] == xor_from_q[v_teleport_dest]
    # where u_current is any node in the tree, and v_teleport_dest is any node != Q.

    # Create a set of all possible XOR sums from a teleport destination node to Q.
    # A teleport destination node `v_td` can be any node except Q.
    # The XOR sum from `v_td` to Q is `xor_from_q[v_td]`.
    teleport_dest_to_q_xors = set()
    for v_teleport_dest_idx in range(N):
        if v_teleport_dest_idx == Q: # Teleport destination cannot be Q
            continue
        if xor_from_q[v_teleport_dest_idx] != -1: # If Q is reachable from this potential teleport destination
            teleport_dest_to_q_xors.add(xor_from_q[v_teleport_dest_idx])

    # Now, iterate through all nodes `u_current_idx` that we could be at when deciding to teleport.
    # The XOR sum accumulated from P to `u_current_idx` is `xor_from_p[u_current_idx]`.
    # This value remains the same during teleportation.
    # We need this value to be equal to one of the values in `teleport_dest_to_q_xors`.
    for u_current_idx in range(N):
        # If u_current_idx is reachable from P
        if xor_from_p[u_current_idx] != -1:
            # If the XOR sum from P to u_current_idx matches an XOR sum
            # from a potential teleport destination (not Q) to Q:
            if xor_from_p[u_current_idx] in teleport_dest_to_q_xors:
                print("YES")
                return

    print("NO")

if __name__ == '__main__':
    solve()
