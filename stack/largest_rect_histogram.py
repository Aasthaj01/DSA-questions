# Given an array of integers h of size n. A represents a histogram i.e h[i] denotes height of
# the ith histogram’s bar. Width of each bar is 1.
#Find the area of largest rectangle in the histogram.




def largest_rect(h):    
    stack=[]
    area=0
    i=0
    while i<len(h):

        if not stack or h[stack[-1]]<=h[i]:
            stack.append(i)
            i+=1

        else:
            top=stack.pop()
            area=max(area,h[top]*(i-stack[-1]-1 if stack else i))

    while stack:
        top=stack.pop()
        area=max(area,h[top]*(i-stack[-1]-1 if stack else i))

    return area
        
h = list(map(int, input().split()))
ans = largest_rect(h)
print(ans)    
