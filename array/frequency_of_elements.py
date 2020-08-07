# frequency of elements in array
#Example ==> [1, 1, 2, 2, 2, 3]
# output  1 2   2 3   3 1



# using builtin and dictionary
def find_freq(arr):
    freq = {}
    for item in arr:
        freq[item] = arr.count(item)
    for key, value in freq.items():
        print("% s% d" % (key, value))
        
        
# nlogn solution 
def find_freq_naive(arr, n):
    arr.sort()
    i = 1
    freq = 1
    while i<=n:
        while i<n and (arr[i] ==arr[i-1]):
            freq+=1
            i +=1
        print(arr[i-1], end = " ")    
        print(freq)
        i +=1
        freq = 1
arr = list(map(int, input("Enter the array elements:").split()))
n = len(arr)
find_freq(arr)
find_freq_naive(arr, n)
