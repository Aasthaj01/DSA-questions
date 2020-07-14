# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
def summ(nums, target):
    
    listt = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target and i!=j:
                listt.append(i)
                listt.append(j)
                return listt
            else:
                continue
            
            
def summi(nums, target):        
    complements = {}
    for i,num in enumerate(nums):
	    if target - num in complements:
		    return[complements[target - num], i]
	    complements[num] = i
    return [] 

	
target = int(input())
nums = list(map(int, input().split()))
print(summi(nums, target))
print(summ(nums, target))
