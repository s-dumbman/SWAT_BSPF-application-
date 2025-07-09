import json

class grid:
    def __init__(self):
        self.grid = [
    [0, 0, 1],
    [1, 1, 0],
    [0, 1, 0]
]
        self.start = (0,0)
        self.goal = unknownGoal(self.grid)

def unknownGoal(grid):
     k = len(grid)
     p = len(grid[0])
     goal = (k-1, p-1)
     return goal

def save_grid(g):
    grid_data = {
        "grid": g.grid,
        "start": g.start,
        "goal": g.goal
    }
    with open("grid.json", "w") as f:
        json.dump(grid_data, f)
    print("grid.json에 저장됨")

def print_g(grid):
    for row in grid:
        print(' '.join(['⬜️' if cell == 0 else '⬛️' if cell == 1 else '🟩' for cell in row]))

if __name__=='__main__':
    g = grid()
    save_grid(g)
    print_g(g.grid)
    print(g.start)
    print(g.goal)