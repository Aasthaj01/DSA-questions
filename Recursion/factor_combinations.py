# gives all possible combinations of factors of a number
# one possible way is to make separate list of factors and include all the lists in an array

def individual_factor(first, prod, num, factor_list):
    if (first>num or prod>num):
        return
    if prod == num:
        print(*factor_list)
        # return
    else:
        for i in  range(first, num):
            if (i*prod>num):
                break
            if (num%i == 0):
                factor_list.append(i)
                individual_factor(i, i*prod, num, factor_list)
                factor_list.remove(factor_list[-1])
        
def final_list(num):
    factor_list = []
    individual_factor(2, 1, num, factor_list)
    
    
num = int(input("Enter the number whose factors you want:"))
print(final_list(num))
