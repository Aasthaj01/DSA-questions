#The term symmetric difference indicates those values that exist in either listta or listtb but do not exist in both.
a = int(input())
listta = set(list(map(int, input().split())))
b = int(input())
listtb = set(list(map(int, input().split())))
p=listta.difference(listtb)
q =listtb.difference(listta)
r =sorted(p.union(q))

for i in r:
    print(i)
