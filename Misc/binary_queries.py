# Today Aakash is stuck in a range query problem. He has been given an array with only numbers 0 and 1. There are two types of queries -
0 L R : Check whether the number formed from the array elements L to R is even or odd and print EVEN or ODD respectively. Number formation is the binary number from the bits status in the array L to R
1 X : Flip the Xth bit in the array
Indexing is 1 based

Input
First line contains a number N and Q as input. Next line contains N space separated 0 or 1. Next Q lines contain description of each query

Output
Output for only query type 0 L R whether the number in range L to R is "EVEN" or "ODD" (without quotes).

Constraints
1≤ N ≤ 10^6
1≤ L ≤ R ≤ 10^6
1≤ Q ≤ 10^6

1≤ X ≤ N
#-------------------------------------------------------------------------------------------------------------------------------------
def solve_prob(case, s):
    if case[0]==0:
        case_0(case, s)
        print()
    else:
        case_1(case, s)
        print()
        
def case_0(case, s):
    l = int(case[1])
    r = int(case[2])
    # for i in range(l, r+1):
    if s[r-1] == 1:
        print('ODD')
    elif s[r-1] == 0:
        print('EVEN')
def case_1(case, s):
    pos = case[1]
    if s[pos-1] == 0:
        del s[pos-1]
        s.insert(pos-1, 1)
    elif s[pos-1] == 1:
        del s[pos-1]
        s.insert(pos-1, 0)
    for i in range(len(s)):
        print(s[i], end="")
            
listt = list(map(int, input("enter number of bits and test cases: ").split()))
number_of_bits = listt[0]
test_cases = listt[1]
s = list(map(int, input("Enter the binary string:").split()))
for i in range(test_cases):
    case = list(map(int, input("Enter your query: ").split()))
    solve_prob(case, s)
    
    
