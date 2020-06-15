# non negative integral solutions to an equation
# x1 + x2 + x3 + x4 + x5 = 1
# Number of possible solution are : 
# (0 0 0 0 1), (0 0 0 1 0), (0 0 1 0 0),
# (0 1 0 0 0), (1 0 0 0 0)
# Total number of possible solutions are 5


def countSolution(n, v):
    total = 0
    if n==1 and v>=0:
        return 1
    for i in range(v+1):    
        total = total+ countSolution(n-1, v-i )
    return total    
    
    
number_of_variable = int(input("Enter the number of variable you want:"))
total = int(input("Enter the sum of variable which you want from the equation:"))
print("The number of solutions are:", countSolution(number_of_variable, total))
