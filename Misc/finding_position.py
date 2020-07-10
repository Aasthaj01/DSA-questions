#Some people are standing in a queue. A selection process follows a rule where people standing on even positions are selected. Of the selected people a queue is formed and again out of these only people on even position are selected. This continues until we are left with one person. Find out the position of that person in the original queue.

#Input:
#The first line of input contains an integer T denoting the number of test cases.The first line of each test case is N,number of people standing in a queue.

#Output:
#Print the position(original queue) of that person who is left.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def even(n):
    if n == 0 or n == 1:
        return 
    elif n == 2:
        return 2
    else:    
        for i in reversed(range(n+1)):
            if 2**i < n:
                return 2**i
t = int(input("Enter number of test cases:"))
arr = []
for i in range(t):
    n = int(input())
    ans = even(n)
    arr.append(ans)
for i in range(len(arr)):    
    print(arr[i], end = ' ')
#     --------------------------------------------------------------------------------------------------------------------

import math
t = int(input())
for i in range(t):
    n =int(input())
    print(pow(2,int(math.log(n,2))))
