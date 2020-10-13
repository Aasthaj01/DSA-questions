# Given a array of both positive and negative integers ‘arr[]’, sort square of the numbers of the array.

# O(n log n) solution
arr = list(map(int, input().split()))
n = len(arr)
for i in range(n):
	arr.append(arr[i]*arr[i])
del arr[:n]
arr.sort()
print(arr)
