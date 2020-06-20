#Given an array,A , having N integers A1, A2, A3...AN.Two elements of the array Ai and Aj are called similar iff Ai = Aj+1 or Aj = Ai+1
Also, the similarity follows transitivity. If Ai and Aj are similar and Aj and Ak are similar, then Ai and Ak are also similar. 
Note: Ai, Ak ,Aj are all distinct.
Input
The first line contains a single integer N denoting number of elements in the array.
The second line contains A  space separated integers where  elements indicate.
#-----------------------------------------------------------------------------------------------------------------------
def pairing(N, A):
    count = 0
    key = 0
    ans = 0
    similar = False
    
    for num in A:
        if num == key:
            count += 1  
        elif key+1 == num:
            count += 1
            similar = True
        else:
            if similar:
                ans += (count * (count-1)) // 2
                similar = False
            count = 1
        key = num
    if similar:
        ans += (count * (count-1)) // 2
    return ans
    
            
N = int(input())
A = list(map(int, input().split()))
A.sort()
print(A)
answer = pairing(N, A)
print(answer)
