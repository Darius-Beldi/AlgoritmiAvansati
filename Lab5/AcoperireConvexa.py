
def testDeOrientare(P, Q, R):

    determinant = (Q[0] * R[1] + P[1] * R[0] + P[0] * Q[1] -
                   Q[0] * P[1] - P[0] * R[1] - Q[1] * R[0])

    if determinant == 0:
        return "TOUCH"
    if determinant > 0:
        return "LEFT"
    if determinant < 0:
        return "RIGHT"

def acoperire_convexa(puncte):
    if len(puncte) <= 3:
        return puncte

    stiva = [puncte[0], puncte[1]]
    for i in range(2, len(puncte)):
        while len(stiva) > 1 and testDeOrientare(stiva[-2], stiva[-1], puncte[i]) != "LEFT":
            stiva.pop()

        stiva.append(puncte[i])

    while len(stiva) > 1 and testDeOrientare(stiva[-2], stiva[-1], puncte[0]) != "LEFT":
        stiva.pop()

    return stiva


n = int(input(""))

listPoints = []
for i in range(n):
    Point = (input().split(" "))
    Point = (int(Point[0]), int(Point[1]))
    listPoints.append(Point)

acoperire_convexa_rezultat = acoperire_convexa(listPoints)

k = len(acoperire_convexa_rezultat)
print(k)

for punct in acoperire_convexa_rezultat:
    print(punct[0], punct[1])
'''
12
-8 0
-6 -2
-4 0
-4 2
-3 2
-2 2
0 -1
2 -4
4 -2
6 2
8 8
10 0

'''
