# Rob likes chocolate, he finds N chocolates in refridgerator. He gives special value to them. 
# He loves maths and thus he takes 1 or more chocolate at a time in continuous manner and fins minimum value out of each group and adds them.
# The task is to find that sum.


def chocolate_problem(L):
    listt = []
    summ = 0
    for i in range(0,len(L)):
        for j in range(1,(len(L)-i)+1):
            
            listt.append(min(L[i:i+j]))
            
    for i in range(0, len(listt))  :     
        summ+=  listt[i] 
    return summ
L = list(map(int, input("Enter the value of chocolates:").split())) 
print(chocolate_problem(L))
