import numpy as np

# Input the sudoku 
grid = [[0,0,0,0,0,0,0,8,5],
        [8,7,0,0,0,4,9,0,2],
        [1,6,0,0,0,0,0,7,0],
        [4,8,0,2,0,6,5,0,0],
        [0,0,2,0,0,8,6,0,9],
        [0,0,6,0,0,0,0,0,0],
        [2,0,0,0,0,1,0,0,0],
        [0,9,0,4,0,2,0,5,3],
        [0,4,0,0,0,3,0,0,8]]
        
print(np.matrix(grid))

def possible(y,x,n):
    global grid
    
    # Check vertical
    for i in range(0,9):
        if grid[y][i] == n:
            return False
            
    # Check horizontal
    for i in range(0,9):
        if grid[i][x] == n:
            return False
            
    # Check box         
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
                
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return

    print(np.matrix(grid))
    raw_input("Alternate:")

print("Solution:")
print(solve())
