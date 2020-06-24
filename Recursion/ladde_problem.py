# Ladder problem
#calculates the total number of ways in which a person can climb n stairs when maximum number of steps that can be taken at a time is k

def ladder_prob(n, k):

    if n==0:
        return 1
    elif n<0:
        return 0
        
    answer = 0 
    i = 1
    while i<= k and i<= n:
        answer= answer+ ladder_prob(n-i, k)
        i = i+1
    return answer
    
    
n = int(input("Enter the total number of steps:"))
k = int(input("Enter the max number of steps that can be taken:"))
print(ladder_prob(n, k))





