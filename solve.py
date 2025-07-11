def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    ans = []
    for q_idx in queries:
        sub_array = arr[0:q_idx + 1]
        ans.append(min(sub_array))

    print(*(ans))

if __name__ == "__main__":
    solve()
