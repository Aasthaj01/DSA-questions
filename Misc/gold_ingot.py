#Ramesh is a goldsmith, who brought a large number of gold ingot each of different length(L) but equal breadth(B) and height(H). He wants to weld the ingots of same length with each other. He tasks his new employee, Akash, to weld the ingots of same length with each other. But Akash forgot that he had to weld the ingots of same length, instead he welded the ingots in a random manner.
# Later Ramesh found out what he had done. He then ordered Akash to cut the welded ingot such that a cuboid with the largest volume from the welded gold ingot is obtained.
# Find the volume of summation of gold ingots minus volume of the largest cuboid.

# Constraints
# 0 < G < 10^5

# Input
# First Line contains one integer G, denoting number of gold ingots
# Second line contains two space separated integers B and H, where B denotes the breadth and H denotes the height of individual ingot
# Third line contains G space separated integers, denoting the length of the individual gold ingots that are welded together in adjacent manner

# Output
# An integer corresponding to the volume of summation of gold ingots minus volume of the largest cuboid, mod 10^9+7.

# Example 1
# Input
# 7
# 1 1
# 6 7 3 4 5 1 3
# Output
# 14

def largest_rect(heights):    
    stack=[]
    area=0
    i=0
    while i<len(heights):

        if not stack or heights[stack[-1]]<=heights[i]:
            stack.append(i)
            i+=1

        else:
            top=stack.pop()
            area=max(area,heights[top]*(i-stack[-1]-1 if stack else i))

    while stack:
        top=stack.pop()
        area=max(area,heights[top]*(i-stack[-1]-1 if stack else i))

    return area


def final_answer(max_height, total_volume):
    answer = total_volume - max_height
    return answer

n = int(input()) 
params = list(map(int, input().split()))
b = params[0]
h = params[1]
heights = list(map(int, input().split()))
max_height = largest_rect(heights)
summ = 0
for i in range(len(heights)):
    summ = summ + heights[i]
    
     
total_volume = summ
print((final_answer(max_height, total_volume) * b * h) % 1000000007, end = "")


