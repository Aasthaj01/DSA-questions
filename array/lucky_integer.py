# Find lucky number or lucky integer i.e given an array of numbers, find the number whose frequency matches the number itself
from collections import Counter

def lucky_number(arr):
    cnt = Counter(arr)
    maxi=-1
    for i in cnt.values():
        
        if cnt[i] == i:
            maxi=max(i,maxi)
    return maxi
    
    
arr = list(map(int, input("Enter the numbers in array:").split()))
print(lucky_number(arr))
