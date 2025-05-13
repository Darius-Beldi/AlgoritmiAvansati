def is_monotone(polygon, axis):
    n = len(polygon)

    if axis == 'x':
        key = lambda p: (p[0], p[1])
    else:
        key = lambda p: (p[1], p[0])

    min_idx = min(range(n), key=lambda i: key(polygon[i]))
    max_idx = max(range(n), key=lambda i: key(polygon[i]))

    def is_chain_monotone(start, end, direction):
        i = start
        while i != end:
            ni = (i + direction + n) % n
            if key(polygon[i]) > key(polygon[ni]):
                return False
            i = ni
        return True

    chain1 = is_chain_monotone(min_idx, max_idx, +1)
    chain2 = is_chain_monotone(min_idx, max_idx, -1)

    return chain1 and chain2


n = int(input())
polygon = [tuple(map(int, input().split())) for _ in range(n)]

print("YES" if is_monotone(polygon, 'x') else "NO")
print("YES" if is_monotone(polygon, 'y') else "NO")
