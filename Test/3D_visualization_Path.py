import json

def load_grid(filename="3D_grid.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data["grid"], data["start"], data["goal"]
def load_path(filename="path.json"):
    with open(filename, "r") as w:
        data = json.load(w)
    return data["path"]
map, start, goal = load_grid()
path = load_path()

print(map)
print(start)
print(goal)
print(path)