# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Using dictionary we are soring count:index values 

def findMaxLength(nums, n):
    if not nums or len(nums)==1:
            return 0
    if len(nums)==2:
        if nums[0]==nums[1]:
            return 0
        return 2

    if nums.count(1)==nums.count(0):
        return len(nums)

    dic = {0:-1}
    maxlen=0
    count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            count-=1

        if count in dic:
            maxlen = max(maxlen,i-dic[count])
        else:
            dic[count] = i

    return maxlen
    
arr = list(map(int, input("Enter the array elements:").split()))    
n = len(arr)
print("Max length of subarray with equal 1 and 0 is:")
print(findMaxLength(arr, n))
