import numpy as np
import json

class grid:
    def __init__(self):
        self.grid = [
    [[0,0,0,0],
     [1,1,1,0],
     [1,0,0,0]],
    [[1,1,1,1],
     [1,1,1,1],
     [0,1,1,1]], #1
    [[1,0,0,1],
     [1,1,0,1],
     [0,0,0,1]],
    [[0,1,1,1],
     [1,1,1,1],
     [1,1,1,1]], #2
    [[0,0,1,0],
     [1,0,0,0],
     [0,1,0,0]], #3
]
        self.start = (0,0,0)
        self.goal = unknownGoal(self.grid)

def unknownGoal(grid):
     k = len(grid[0][0]) #x
     p = len(grid[0]) #y
     r = len(grid) #z
     goal = (k-1, p-1, r-1)
     print(k, p, r)
     return goal

def save_grid(g):
    grid_data = {
        "grid": g.grid,
        "start": g.start,
        "goal": g.goal
    }
    with open("3D_grid.json", "w") as f:
        json.dump(grid_data, f)
    print("3D_grid.json에 저장됨")

def print_g(grid):
    for row in grid:
        for layer in row:
            print(' '.join(['⬜️' if cell == 0 else '⬛️' if cell == 1 else '🟩' for cell in layer]))
        print()

if __name__=='__main__':
    g = grid()
    save_grid(g)
    print_g(g.grid)
    print(g.start)
    print(g.goal)