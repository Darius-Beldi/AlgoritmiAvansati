
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
puncte_nu_in_acoperire = set(x for x in listPoints) - set(x for x in acoperire_convexa_rezultat)
puncte_nu_in_acoperire = list(x for x in puncte_nu_in_acoperire)
print(puncte_nu_in_acoperire)
def cost(A, B):
    temp = B[0] - A[0] + B[1] - A[1]
    if temp < 0 :
        temp = -temp
    return round((temp)**(1/2),1)
print(cost((1,1),(2,2)))
convex_hull = []
for punct in puncte_nu_in_acoperire:
    min = 100000
    temp1, temp2 = 0, 0
    for i in range(len(acoperire_convexa_rezultat)-1):
        _cost = (cost(acoperire_convexa_rezultat[i], punct) +
            cost(punct, acoperire_convexa_rezultat[i+1]) -
            cost(acoperire_convexa_rezultat[i], acoperire_convexa_rezultat[i+1]) )
        if _cost< min:
            min = _cost
            temp1 = acoperire_convexa_rezultat[i]
            temp2 = acoperire_convexa_rezultat[i+1]

    convex_hull.append(temp1)
    convex_hull.append(punct)
    convex_hull.append(temp2)

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

