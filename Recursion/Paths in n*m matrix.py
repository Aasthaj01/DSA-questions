def path_finder(r, c):
    if r == 1 or c ==1:
        return 1
    
    return(path_finder(r-1, c) + path_finder(r, c-1))
    
    
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
answer = path_finder(n, m)
print(answer)
