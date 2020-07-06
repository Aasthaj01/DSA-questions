# swap all odd and even bits

def swap(n):
    # arr = []
    even_bits = n&0xAAAAAAAA
    odd_bits = n&0x55555555
    even_bits>>=1
    odd_bits<<=1
    return(even_bits|odd_bits)
    

    

t = int(input())
arr =[]

for i in range(t):
    n = int(input())
    ans = swap(n)
    arr.append(ans)
for i in range(len(arr)):
        print(arr[i], end = " ")    
    
    
