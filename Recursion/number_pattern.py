# prints pattern like -- number, number-5...number+5, number


def pattern(number, current_num, flag):
    print(current_num)
    if(flag == False and current_num == number):
        return
    
    if flag == True:
        if current_num-5 >0:
            pattern(number, current_num-5, True)
        else:
            pattern(number, current_num-5, False)
            
    else:    
        pattern(number, current_num+5, False)



number = int(input("Enter the number:"))
flag = True

pattern(number, number, flag)
