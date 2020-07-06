# Finding power sets of the given string

def power_sets(s, m, n):
    arr = []
    for i in range(m):
        for j in range(n):
            if (i & (1<<j))!=0:
                print(s[j], end = '')
        print()
                
s = str(input())
n  = len(s)
m = 2**n
power_sets(s, m, n)
