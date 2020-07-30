#add 1 to number
# Given a non-negative number represented as an array of digits,
# add 1 to the number ( increment the number represented by the digits ).
# The digits are stored such that the most significant digit is at the head of the list.

def plusOne(A):
    
    n=len(A)
    if n<1:
        return [1]
    for i in range(n-1,-1,-1):
        if A[i] == 9:
            A[i]=0
        else:
            A[i]=A[i]+1
            break
    if A.count(0)==len(A): 
        A[0]=1
        A.append(0)
    k=0
    for i in range(len(A)): 
        if A[i]==0:
            k+=1
        else:
            break
    return A[k:]
    
listt = list(map(int, input().split()))
ans =plusOne(listt)
print(ans)
