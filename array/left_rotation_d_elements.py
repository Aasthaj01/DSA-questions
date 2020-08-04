# A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. 
#Given an array of n integers and a number, d, perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.

#Time complexity of slicingO(n + d)
nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))
for value in (a[d:] + a[0:d]): 
    print(value, end = " ")
#========================================================================================================
#recursive solution-  O(nd)
def left_rotate_d(a, n, d):
    
    for i in range(d):
        rotate_left(a, n)
        
    
def rotate_left(a, n):
    temp = a[0]
    for i in range(1, n):
        a[i-1] = a[i]
    a[n-1] = temp
    return a


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    left_rotate_d(a, n, d)
    for i in range(n):
        print(a[i], end =" ")
