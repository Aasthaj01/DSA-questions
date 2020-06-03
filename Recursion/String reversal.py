def reverse(str):
    if len(str) == 0:
        return str
    else:
        return reverse(str[1:]) + str[0]


string = input("Enter the string: ")

print("The Given String  is: ", string)

print("Reversed String is: ", reverse(string))
