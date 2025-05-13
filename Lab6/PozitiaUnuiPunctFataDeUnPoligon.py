def on_segment(a, b, p):
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def point_in_polygon(poly, p):
    n = len(poly)
    inside = False
    for i in range(n):
        a = poly[i]
        b = poly[(i + 1) % n]
        if on_segment(a, b, p):
            return "BOUNDARY"
        if (a[1] > p[1]) != (b[1] > p[1]):
            x_intersect = a[0] + (b[0] - a[0]) * (p[1] - a[1]) / (b[1] - a[1])
            if x_intersect > p[0]:
                inside = not inside

    return "INSIDE" if inside else "OUTSIDE"

n = int(input())
polygon = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
query_points = [tuple(map(int, input().split())) for _ in range(m)]

for p in query_points:
    print(point_in_polygon(polygon, p))
