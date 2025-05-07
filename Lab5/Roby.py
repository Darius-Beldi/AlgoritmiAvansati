

def testDeOrientare(P, Q, R):

    determinant = (Q[0] * R[1] + P[1] * R[0] + P[0] * Q[1] -
                   Q[0] * P[1] - P[0] * R[1] - Q[1] * R[0])

    if determinant == 0:
        return "TOUCH"
    if determinant > 0:
        return "LEFT"
    if determinant < 0:
        return "RIGHT"

n = int(input())
listPoints = []
for i in range(n):
    Point = (input().split(" "))
    Point = (int(Point[0]), int(Point[1]))
    listPoints.append(Point)

vDreapta = 0
vStanga = 0
ramas = 0

listPoints.append(listPoints[0])

for i in range(len(listPoints)):
    if listPoints[i+1] == listPoints[0]:
        break
    if testDeOrientare(listPoints[i], listPoints[i+1], listPoints[i+2]) == "LEFT":
        vStanga += 1
    if testDeOrientare(listPoints[i], listPoints[i+1], listPoints[i+2]) == "RIGHT":
        vDreapta += 1
    if testDeOrientare(listPoints[i], listPoints[i+1], listPoints[i+2]) == "TOUCH":
        ramas += 1
print(vStanga, vDreapta, ramas)

'''
7
1 1
2 2
2 0
3 0
4 0
5 0
6 0
'''