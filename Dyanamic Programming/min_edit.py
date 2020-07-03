# Given 2 strings and 3 operations insert, delete, replace, return min number of operations required to make one string similar to other

def min_edit(s1, s2, m, n):
    listt = [[0]*(n+1)]*(m+1)

    for i in range(0, m+1):
        listt[i][0] = i
    for j in range(0, n+1):
        listt[0][j] = j
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1]==s2[j-1]:
                listt[i][j] = listt[i-1][j-1]
            else:
                listt[i][j] == 1+min(listt[i-1][j], listt[i][j-1], listt[i-1][j-1])
    return listt[m][n]    

s1 = str(input("Enter string 1:"))
m = len(s1)
s2 = str(input("Enter string 2:"))
n = len(s2)
print("Minimum number of operations required are:", min_edit(s1, s2, m, n))
