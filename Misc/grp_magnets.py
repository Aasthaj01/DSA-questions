# magents are either repesented by 01 or 10, 1 is north pole and 0 is south pole
#If magnets attract, they do not form group i.e 01, 01 will not form a group but 10, 01 will.
#return count of groups

def count_groups(n, m):
    count = 1
    for i in range(1, n):
        if m[i] == m[i-1]:
            continue
        else:
            count+=1
    return count        

m = []
n = int(input())
for i in range(n):
    m.append(str(input()))
print(count_groups(n, m))    
