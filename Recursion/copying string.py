def copy_string(str_1, str_2, index):
    str_2[index] = str_1[index]
    if index == len(str_1)-1 :
        return
    else:
        copy_string(str_1, str_2, index+1)

    
str_1 = str(input("Enter string 1: "))
st = ""
str_2 = [0]*len(str_1)
index = 0
copy_string(str_1, str_2, index)
print("The copies string is: ", st.join(str_2))

