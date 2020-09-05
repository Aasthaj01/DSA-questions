# There are 5 people in a team, one of them should be made the leader.
# Leader is one whose name length is max (removing all the duplicates and spaces. Also, if there is one small alphabet and one capital then it is considered as same)
# Input 5 names and return leader's name 


from collections import OrderedDict 
def team_lead(name1, name2, name3, name4, name5):
    listt = []
    arr = []
    listt.extend([name1, name2, name3, name4, name5])
    
    for word in listt:
        new = "".join(OrderedDict.fromkeys(word))
        arr.append(new)
    
    res = max(arr, key = len) 
    return listt[arr.index(res)]

name1 = str(input())
name2 = str(input())
name3 = str(input())
name4 = str(input())
name5 = str(input())
print(team_lead(name1, name2, name3, name4, name5))
