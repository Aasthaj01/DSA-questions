def printTriangle(arr, num): 
          
        # Base case 
        if (num < 1): 
            return
        temp = [0] * (num - 1) 
        for i in range(0, num-1): 
            x = arr[i] + arr[i + 1] 
            temp[i] = x 
        # Make a recursive call and pass 
        printTriangle(temp, num-1) 
        print(arr) 
     
num = int(input("Enter the number of elements you want in your array: "))
for i in range(num):
    arr = list(map(int, input("Enter the numbers:  ").split()))
    # print(arr)
    printTriangle(arr, num) 
  
