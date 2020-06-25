#Program to count the number of ways to reach n'th stair when user climb 1 .. m stairs at a time. 

#-------------------------------------BOTTOM-UP APPROACH with O(steps*m) time complexity----------------------------------------------------------------------------------
def countWaysUtil(n, m): 
     
    res = [0 for x in range(n)]  
    res[0], res[1] = 1, 1
      
    for i in range(2, n): 
        j = 1
        while j<= m and j<= i: 
            res[i] = res[i] + res[i-j] 
            j = j + 1 
    return res[n-1] 
   
def countWays(steps, m): 
    return countWaysUtil(steps + 1, m) 
      

steps, m = list(map(int, input("Enter the number of steps and max steps to be taken at a time:").split()))
print("Number of ways =", countWays(steps, m))
  
