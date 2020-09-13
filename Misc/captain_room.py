# Hackerrank problem 
# The Captain was given a separate room, and the rest were given one room per group.
# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists.
# The room numbers will appear  times per group except for the Captain's room.
# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of  and the room number list.

# Input Format
# The first line consists of an integer, , the size of each group.
# The second line contains the unordered elements of the room number list.
#====================================================================================================================
from collections import Counter 
k = int(input())
tourists = list(map(int, input().split()))
listt = tourists.copy()
listt = list(set(listt))
x = Counter(tourists)
for i in listt:
    if x[i] == 1:
        print(i)

