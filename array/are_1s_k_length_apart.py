# Given a string of 0 and1 return True if distance between 2 1s is equal to or greater than k else return False.

def distance_between_one(nums, n, k):
    if 1 in nums:
            indx = nums.index(1)
            count = 0
            result = True
            for i in range(indx+1, (len(nums))):
                if nums[i] == 0:
                    count += 1
                elif nums[i] == 1:
                    if count < k:
                        result = False
                    count = 0
    else:
        return True
    return result
    
    
nums = list(map(int, input("Enter 0s or 1s in array:").split()))
k = int(input("Enter the value for k:"))
n = len(nums)
print(distance_between_one(nums, n, k))
