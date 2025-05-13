def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def in_triangle(a, b, c, p):
    cp1 = cross(a, b, p)
    cp2 = cross(b, c, p)
    cp3 = cross(c, a, p)

    if (cp1 >= 0 and cp2 >= 0 and cp3 >= 0) or (cp1 <= 0 and cp2 <= 0 and cp3 <= 0):
        if cp1 == 0 or cp2 == 0 or cp3 == 0:
            return "BOUNDARY"
        return "INSIDE"
    return "OUTSIDE"


def point_in_convex_polygon(poly, p):
    n = len(poly)
    if n < 3:
        return "OUTSIDE"

    p0 = poly[0]
    if cross(p0, poly[1], p) < 0 or cross(p0, poly[-1], p) > 0:
        return "OUTSIDE"

    left = 1
    right = n - 1
    while right - left > 1:
        mid = (left + right) // 2
        if cross(p0, poly[mid], p) > 0:
            left = mid
        else:
            right = mid

    return in_triangle(p0, poly[left], poly[(left + 1) % n], p)


n = int(input())
polygon = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
query_points = [tuple(map(int, input().split())) for _ in range(m)]

for p in query_points:
    print(point_in_convex_polygon(polygon, p))
