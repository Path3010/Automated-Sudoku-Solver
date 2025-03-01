import pyautogui as ui
import time

grid =[]

while True:
    row = list(input("Row: "))
    ints = []
    
    for n in row:
        ints.append(int(n))
    grid.append(ints)
    
    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')
    
time.sleep(3)

def possible(x,y,n):
    pass

def Print(matrix):
    pass

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    Print(grid)
    
solve()