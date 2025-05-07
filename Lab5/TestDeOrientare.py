nrTeste = int(input())

def testDeOrientare(P, Q, R):

    determinant = (Q[0] * R[1] + P[1] * R[0] + P[0] * Q[1] -
                   Q[0] * P[1] - P[0] * R[1] - Q[1] * R[0])

    if determinant == 0:
        return "TOUCH"
    if determinant > 0:
        return "LEFT"
    if determinant < 0:
        return "RIGHT"


listTests = []
for i in range(nrTeste):
    n = input().split(" ")
    test = []
    P = (int(n[0]), int(n[1]))
    Q = (int(n[2]), int(n[3]))
    R = (int(n[4]), int(n[5]))
    test.append(P)
    test.append(Q)
    test.append(R)
    listTests.append(test)

for test in listTests:
    print(testDeOrientare(test[0], test[1], test[2]))

'''
3
1 1 5 3 2 3
1 1 5 3 4 1
1 1 5 3 3 2
'''