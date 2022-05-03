A = [[1,2,3],
    [4,5,6],
    [7,8,9]]

B = [[7,5,7],
    [6,4,5],
    [1,7,8]]

C = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(C)):
            C[i][j]+= A[i][k] * B[k][j]

for r in C:
    print(r)