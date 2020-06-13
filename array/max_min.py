def get_max(lst, num):
    maxi = lst[0]
    for i in range(1, num):
        maxi = max(maxi, lst[i])
    return maxi
    
def get_min(lst, num):
    mini = lst[0]
    # maxi = 0
    for i in range(1, num):
        mini = min(mini, lst[i])
    return mini
    
    
num = int(input("Enter the length of array you want: "))
for i in range(num):
    lst = list(map(int, input("Enter the numbers with space: ").split()))
    print(lst)
    print("The minimum number in the given array is:", get_min(lst, num))
    print("The maximum number in the given array is:",get_max(lst, num))
    
    
 
