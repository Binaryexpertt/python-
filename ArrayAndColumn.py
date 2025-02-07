"""Program snippet that transfers the multiplication of the rows of array A and the column values
of array B to array C """

A=[[0 for i in range(5)] for j in range(5)]
B=[[0 for i in range(5)] for j in range(5)]
C=[[0 for i in range(5)] for j in range(5)]
print(A)
print(B)
print(C)

for j in range(5):
    for k in range(5):
        A[j][k]=float(input(f"Of A {j+1}. row {k+1}. column= "))
for j in range(5):
    for k in range(5):
        B[j][k]=float(input(f"Of B {j+1}. row {k+1}. column= "))
for j in range(5):
    for k in range(5):
        C[j][k]=A[j][k]*B[j][k]
        print(f"Of C {j+1}.rows {k+1}.column Multiplication={C[j][k]}")