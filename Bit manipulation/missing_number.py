# Find the missing numberfrom the input list if the list contains numbers from 1 to n+1

def missing_number(listt, arr, m, n):
    result = 0
    r = 0
    for i in range(0, n):
        result = result^arr[i]
    for i in range(0, m):
        r = r^listt[i]
    answer = result^r
    print(answer)
         
            
n = int(input("Enter a number till which you want to consider the array:"))
listt = list(map(int, input("Enter the numbers in the list:").split()))
m = len(listt)
arr = []
for i in range(1, n+1):
    arr.append(i) 
   
print("Missing number is:")
missing_number(listt, arr, m, n)


