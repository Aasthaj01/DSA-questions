# Given a square piece and a total number of cuts available n,
# Find out the maximum number of rectangular or square pieces of equal size that can be obtained with n cuts.
# The allowed cuts are horizontal and vertical cut.

def max_pieces(n):
    # let horizontal cuts be x, vertical will be n-x
    if n>0:
        x = n//2
        return (n-x+1)*(x+1)
    else:
        return 0
        
        
n = int(input("Enter the number of cuts: "))
print(max_pieces(n))
