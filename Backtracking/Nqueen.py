# N queen problem
# no queen should clash
# zip is a function which clubs 2 tuples

def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print(board[i][j], end =" ") 
        print(" ") 
       
def isSafe(board, x, y): 
    # x, y are row and column
    for i in range(y): 
        if board[x][i] == 1: 
            return False
  
    for i, j in zip(range(x, -1, -1),  
                    range(y, -1, -1)): 
        if board[i][j] == 1: 
            return False
 
    for i, j in zip(range(x, N, 1),  
                    range(y, -1, -1)): 
        if board[i][j] == 1: 
            return False
  
    return True
    
    
def solveQueen(board, col):
    if col>=N:
        return True
    for i in range(N):
        if isSafe(board, i, col) :
            board[i][col] = 1
            if solveQueen(board, col + 1) == True: 
                return True
            board[i][col] = 0
    return False
      
N = int(input("Enter the dimension of the matrix:")) 
board = [ [ 0 for j in range(N) ] for i in range(N) ] 
if solveQueen(board, 0) == False: 
    print("Solution doesn't exist")
printSolution(board) 

 
