#Finding permutations of a string in lexicographical order

def permuteRec(string, n, index = -1, curr = ""): 
    # base case where n is length of the string
    if index == n: 
        return
  
    if len(curr) > 0: 
        print(curr) 
  
    for i in range(index + 1, n): 
        curr += string[i] 
        permuteRec(string, n, i, curr) 

        curr = curr[:len(curr) - 1] 
 
def powerSet(string): 
    string = ''.join(sorted(string)) 
    permuteRec(string, len(string)) 
  
if __name__ == "__main__": 
    string = str(input("Enter a string:"))
    powerSet(string) 
