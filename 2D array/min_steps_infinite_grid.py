# You are in an infinite 2D grid where you can move in any of the 8 directions

#  (x,y) to 
#     (x+1, y), 
#     (x - 1, y), 
#     (x, y+1), 
#     (x, y-1), 
#     (x-1, y-1), 
#     (x+1,y+1), 
#     (x-1,y+1), 
#     (x+1,y-1) 
# You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.
# Input Format
# Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.

def coverPoints(A, B):
        length = len(A)
        count = 0
        for i in range(length-1):
            x = abs(A[i]-A[i+1])
            y = abs(B[i]-B[i+1])
            count += max(x, y)
        return count 
        
A = list(map(int, input("Enter x coordinates of point:").split()))
B = list(map(int, input("Enter y coordinates of point:").split()))
ans = coverPoints(A, B)
print(ans)
