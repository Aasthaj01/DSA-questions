import numpy as np

def sum_diagonal_elements(mat, r, c):
    primary_sum = 0
    sec_sum = 0
    if r == c:
        for i in range (0, r):
            for j in range (0, c):
                if i == j:
                    primary_sum = primary_sum + mat[i][i]
                    sec_sum += mat[i][r - i - 1] 
        print(primary_sum)
        print(sec_sum)

    else:
        print("diagonal sum cannot be computed as the matrix is not square matrix")


m = int(input("enter the number of rows: "))
n = int(input("enter the number of columns: "))
print("Enter the numbers you want in your matrix: ")
entries = list(map(int, input().split()))
mat = np.array(entries).reshape(m, n)
print(mat)
sum_diagonal_elements(mat, m, n)
