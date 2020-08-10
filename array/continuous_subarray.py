# L = [1,2,3]
# OUTPUT -- > [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]


def continuous_subarray(L, n):
    for i in range(0,len(L)):
        for j in range(1,(len(L)-i)+1):
            
            print(L[i:i+j])
L = list(map(int, input("Enter the array elements:").split())) 
n = len(L)
continuous_subarray(L, n)
