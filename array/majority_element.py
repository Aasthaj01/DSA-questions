# Majority elements are those which have frequency greater than n/2, where n is size of array.

def majority_element(arr, n):
         
    freq = {}
    for item in arr:
        freq[item] = arr.count(item)
    for key, value in freq.items():
        if value> n//2:
            req_key = key
            print("The element and its frequency are:")
            print("% s% d" % (key, value))
            for i in range(0, n):
                if req_key == arr[i]:
                    print("position of the key is: ", i)
        else:
            print(-1)
            break
    
# Code to find max freq out of all the elements  
# for i in range(n):
    #     res = 0
    #     count = arr.count(arr[i])
    #     if count>= n//2:
    #         res = max(res, count)
    # return res         

arr= list(map(int, input("Enter the numbers:").split()))
n = len(arr)
majority_element(arr, n)
