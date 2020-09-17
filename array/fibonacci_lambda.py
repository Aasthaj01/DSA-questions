def fib_list(count):
    fib_lst = [0, 1]
    any(map(lambda _:fib_lst.append(sum(fib_lst[-2:])), 
                                    range(2, count)))
    return fib_lst[:count]
     
n = int(input("Enter the number upto which you want the fibonacci series:"))  
print(fib_list(n))  
