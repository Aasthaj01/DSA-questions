#In this even odd problem, given a range [low, high] (both inclusive), select K numbers from the range (a number can be chosen multiple times) such that sum of those K numbers is even.
# Calculate the number of all such permutations.
# As this number can be large, print it modulo (1e9 +7).

# Constraints
# 0 <= low <= high <= 10^9
# K <= 10^6.

# Input
# First line contains two space separated integers denoting low and high respectively
# Second line contains a single integer K.

# Output
# Print a single integer denoting the number of all such permutations

# Example 1
# Input
# 4 5
# 3
# Output
# 4
# There are 4 valid permutations viz. {4, 4, 4}, {4, 5, 5}, {5, 4, 5} and {5, 5, 4} which sum up to an even number
#============================================================================================================================================================
from itertools import product

def sum_of_tup(n):
    summ=0
    for i in range(len(n)):
        summ=summ+int(n[i])
    return summ


parameter =list(map(int,input().split()))
low = parameter[0]
high = parameter[1]
k=int(input())
lst=[]
for i in range(low,high+1):
    lst.append(i)
count=0
perm=product(lst,repeat=k)
for i in perm:
    if (sum_of_tup(i)%2==0):
        count+=1
print(count%1000000007)
