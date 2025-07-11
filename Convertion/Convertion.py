import heapq

# f(평가함수) = g(지나온 거리) + h(가야할 거리)

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
     return goal

g = grid()
print(g.start)
print(g.goal)

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

grid = g.grid
s = g.start
g = g.goal

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

def search(grid, s, g): # A* 알고리즘
    OL = [] # Open List
    CL = set() # Close List

    s_node = Node(s[0], s[1], s[2]) # 시작 노드 설정
    g_node = Node(g[0], g[1], g[2]) # 목표 노드 설정

    heapq.heappush(OL, s_node) # 첫 OL을 시작 노드로 설정 -> 알고리즘 시작
    while OL: # OL의 원소가 존재하는 경우에 (공집합이 아닌 경우에)
        c_node = heapq.heappop(OL) 
        CL.add((c_node.x, c_node.y, c_node.z))
        print(f"Add Close List: {c_node.x}, {c_node.y}, {c_node.z} (f={c_node.f}, g={c_node.g}, h={c_node.h})")

        if c_node.x == g_node.x and c_node.y == g_node.y and c_node.z == g_node.z:
            print(f"Completed Node: {c_node.x}, {c_node.y}, {c_node.z} (f={c_node.f}, g={c_node.g}, h={c_node.h})")
            return reconstruct(c_node)

        for dx, dy, dz in direction_list: # 3*3*3 이동 가짓수
            n_x = c_node.x + dx # 이동할 노드의 x좌표
            n_y = c_node.y + dy # 이동할 노드의 y좌표
            n_z = c_node.z + dz # 이동할 노드의 z좌표
            d_node = Node(n_x, n_y, n_z)  # 이동할 노드 설정
            k = distanceGenerate(d_node, c_node) # 이동할 노드와 도착 노드까지의 거리 계산 (가중치로 활용할 k)

            xlen = len(grid[0][0]) # 공간의 x축 거리 (행)
            ylen = len(grid[0]) # 공간의 y축 거리 (열)
            zlen = len(grid) # 공간의 z축 거리 (층)

            if (0 <= n_x < xlen) and (0 <= n_y < ylen) and (0 <= n_z < zlen) and grid[n_z][n_y][n_x] != 1: # 이동할 노드가 공간 밖에 없는지 확인 + 막힌 공간이 아닌지 확인
                if (n_x, n_y, n_z) in CL: # 이동할 노드가 CL에 없는지 확인
                    continue

                n = Node(n_x, n_y, n_z) # 이동할 노드 설정
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

def reconstruct(end_node): # 마지막 경로 작성 함수
    path = [] 
    c = end_node # 도착 노드
    while c is not None: # 불가능한 경우가 아니라면
        path.append((c.x, c.y, c.z)) # 새로운 자료형 Path(리스트)에 경로 저장
        c = c.parent # 지나온 길 탐색
        print(f"Reconstructing: {c.x if c else 'None'}, {c.y if c else 'None'}, {c.z if c else 'None'}")
    path.reverse() # 마지막 위치 -> 처음 위치 에서 처음 위치 -> 마지막 위치 순으로 경로를 작성
    return path

def mark_path_on_grid(grid, path):
    for x, y, z in path:
        grid[z][y][x] = 2 
    return grid

if __name__ == "__main__":
    path = search(grid, s, g)
    if path:
        grid_with_path = mark_path_on_grid(grid, path)
        print("경로:", path, f"{len(path)} 번")
    else:
        print("불가능한 경우")
    

    
