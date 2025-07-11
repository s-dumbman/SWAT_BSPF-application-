import heapq
import json

def distanceGenerate(node1, node2):
    return ((node1.x-node2.x)**2+(node1.y-node2.y)**2+(node1.z-node2.z)**2)**(1/2)

direction_list = []
def action_list(L):
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            for c in [-1,0,1]:
                if (a!=0 or b!=0 or c!=0): 
                    L.append((a,b,c))
                else:
                    continue
action_list(direction_list)
def load_grid(filename="3D_grid.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data["grid"], data["start"], data["goal"]

grid, s, g = load_grid()

class Node:
    def __init__(self, x, y, z, g=0, h=0):
        self.x = x 
        self.y = y 
        self.z = z
        self.g = g  
        self.h = h 
        self.f = g + h  
        self.parent = None  

    def __lt__(self, other):
        return self.f < other.f
    
def search(grid, s, g):
    OL = []
    CL = set()

    s_node = Node(s[0], s[1], s[2])
    g_node = Node(g[0], g[1], g[2])

    heapq.heappush(OL, s_node)
    while OL:
        c_node = heapq.heappop(OL)
        CL.add((c_node.x, c_node.y, c_node.z))
        print(f"Add Close List: {c_node.x}, {c_node.y}, {c_node.z} (f={c_node.f}, g={c_node.g}, h={c_node.h})")

        if c_node.x == g_node.x and c_node.y == g_node.y and c_node.z == g_node.z:
            print(f"Completed Node: {c_node.x}, {c_node.y}, {c_node.z} (f={c_node.f}, g={c_node.g}, h={c_node.h})") 
            return reconstruct(c_node)
        
        for dx, dy, dz in direction_list:
            n_x = c_node.x + dx
            n_y = c_node.y + dy
            n_z = c_node.z + dz
            # 예외확인 필요
            d_node = Node(n_x, n_y, n_z)
            k = distanceGenerate(d_node, c_node)
            xlen = len(grid[0][0])
            ylen = len(grid[0])
            zlen = len(grid)

            if (0 <= n_x < xlen) and (0 <= n_y < ylen) and (0 <= n_z < zlen) and grid[n_z][n_y][n_x] != 1:
                if (n_x, n_y, n_z) in CL:
                    continue

                n = Node(n_x, n_y, n_z)
                n.g = c_node.g + k
                n.h = distanceGenerate(n, g_node)
                n.f = n.g + n.h
                n.parent = c_node

                in_open = False
                for open_node in OL:
                    if (n.x, n.y, n.z) == (open_node.x, open_node.y, open_node.z) and n.g >= open_node.g:
                        in_open = True
                        break

                if not in_open:
                    heapq.heappush(OL, n)
                    print(f"Add Open List: {n.x}, {n.y}, {n.z} (f={n.f}, g={n.g}, h={n.h})")

    return None

def reconstruct(end_node):
    path = []
    c = end_node
    while c is not None:
        path.append((c.x, c.y, c.z))
        c = c.parent
        print(f"Reconstructing: {c.x if c else 'None'}, {c.y if c else 'None'}, {c.z if c else 'None'}")
    path.reverse()
    return path

def mark_path_on_grid(grid, path):
    for x, y, z in path:
        grid[z][y][x] = 2 
    return grid

def print_grid(grid):
    for row in grid:
        for layer in row:
            print(' '.join(['⬜️' if cell == 0 else '⬛️' if cell == 1 else '🟩' for cell in layer]))
        print()

if __name__ == "__main__":
    path = search(grid, s, g)
    if path:
        grid_with_path = mark_path_on_grid(grid, path)
        print_grid(grid_with_path)
        print("경로:", path, f"{len(path)} 번")
    else:
        print("불가능한 경우")
    

    
