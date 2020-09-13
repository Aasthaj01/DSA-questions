# A strict superset has at least one element that does not exist in its subset.
#Set is([1, 3, 4])a strict superset of set ([1, 4]).
set1 = set(map(int, input().split()))
print(all([set1.issuperset(set(map(int, input().split()))) for i in range(int(input()))]))
