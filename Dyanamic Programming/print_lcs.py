def LCS(A,B,n,m):
    M = [ [ 0 for x in range(m+1)] for x in range(n+1) ]
    seq = []
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                M[i][j] = 0
            else:
                if A[i-1]==B[j-1]:
                    M[i][j] = 1+M[i-1][j-1]
                else:
                    M[i][j] = max(M[i-1][j],M[i][j-1])
    i = n
    j = m
    
    while i>0 and j>0:
        if M[i][j]>M[i-1][j] and M[i][j] == M[i][j-1]:
            j-=1
            
        elif M[i][j]==M[i-1][j] and M[i][j] >M[i][j-1]:
            i-=1
        elif M[i][j]>M[i][j-1] and M[i][j]>M[i-1][j]:
            seq.append(A[i-1])
            i-=1
            j-=1
        elif M[i][j]==M[i-1][j] and M[i][j]==M[i][j-1]:
            i-=1
   
       
    return " ".join(map(str,seq[::-1]))

n, m = list(map(int, input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(LCS(A,B,n,m))
