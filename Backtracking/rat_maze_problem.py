# rat maze problem, where rat has to eat the cheese which is at the end of the maze.
# 1 and 0 are present in maze, 0 is the block point. Rat can move in right and bottom postion i.e (i, j+1), (i+1, j)


def printSolution(sol): 
    for i in sol: 
        for j in i: 
            print(str(j) + " ", end ="") 
        print("") 

def isSafe( maze, x, y ): 
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1: 
        return True
    return False
    
def solve(maze):
    sol = [ [ 0 for j in range(N) ] for i in range(N) ] 
    if solveMaze(maze, 0, 0, sol) == False: 
        print("Solution doesn't exist"); 
        return False
    printSolution(sol) 
    return True

def solveMaze(maze, x, y, sol): 
    if x == N - 1 and y == N - 1 and maze[x][y]== 1: 
        sol[x][y] = 1
        return True

    if isSafe(maze, x, y) == True:
        sol[x][y] = 1
        if solveMaze(maze, x + 1, y, sol) == True: 
            return True
        if solveMaze(maze, x, y + 1, sol) == True: 
            return True
        sol[x][y] = 0
        return False
  
  
N = int(input("Enter the dimension of the matrix:")) 
maze = [[int(input()) for i in range(N)]for j in range(N)]
solve(maze) 
