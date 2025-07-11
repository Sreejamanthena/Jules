import collections

def solve():
    N = int(input())
    adj = collections.defaultdict(list)
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adj[u - 1].append((v - 1, w))
        adj[v - 1].append((u - 1, w))

    P, Q = map(int, input().split())
    P -= 1
    Q -= 1



    xor_from_p = [-1] * N
    xor_from_q = [-1] * N

    def dfs(u, current_xor_sum, parent, target_array, graph_adj):
        target_array[u] = current_xor_sum
        for v, weight in graph_adj[u]:
            if v != parent:
                dfs(v, current_xor_sum ^ weight, u, target_array, graph_adj)

    dfs(P, 0, -1, xor_from_p, adj)
    dfs(Q, 0, -1, xor_from_q, adj)

    if xor_from_p[Q] == 0:
        print("YES")
        return
    teleport_dest_to_q_xors = set()
    for v_teleport_dest_idx in range(N):
        if v_teleport_dest_idx == Q: 
            continue
        if xor_from_q[v_teleport_dest_idx] != -1: 
            teleport_dest_to_q_xors.add(xor_from_q[v_teleport_dest_idx])


    for u_current_idx in range(N):
        
        if xor_from_p[u_current_idx] != -1:
            if xor_from_p[u_current_idx] in teleport_dest_to_q_xors:
                print("YES")
                return

    print("NO")

if __name__ == '__main__':
    solve()
