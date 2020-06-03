def check_palindrome(string):
    if string == string[::-1]:
        print("String is a palindrome")
    else:
        print("string is not a palindrome")

string = input("Enter the string which you want to check: ")
check_palindrome(string)
