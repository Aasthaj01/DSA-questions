# suppose the string contains various words, the function should return reversed words but in same sequence as given in sentence
#example: hello world --> olleh dlrow

def reverseString(string):
    arr = string.split()
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
        print(arr[i], end = " ")

    
string = str(input())
reverseString(string)
