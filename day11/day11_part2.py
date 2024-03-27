import networkx as nx
from itertools import combinations

with open("day11/day11_test_input.txt", "r") as f:
    rows = f.readlines()

rows = [row.strip() for row in rows]
rows = [list(row) for row in rows]

empty_rows = []
for idx, row in enumerate(rows):
    if '#' not in row:
        empty_rows.append(idx)

columns = list(zip(*rows))

empty_columns = []
for idx, col in enumerate(columns):
    if '#' not in col:
        empty_columns.append(idx)


empty_coordinates = []


for row in empty_rows:
    for i in range(len(rows[0])):
        empty_coordinates.append((row, i))

for col in empty_columns:
    for i in range(len(rows)):
        empty_coordinates.append((i,col))
    

print("empty", empty_coordinates)
grid = rows

print(empty_columns)
print(empty_rows)

def get_coords_for_hash(grid):
    hashes = []
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                hashes.append((i,j))
    return hashes

def create_graph(grid, empty_coorindates):
    G = nx.Graph()
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            G.add_node((i,j))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    weight = 1
                    if (i, j) in empty_coordinates or (ni, nj) in empty_coordinates:
                        weight = 100
                    G.add_edge((i, j), (ni, nj), weight=weight)

    return G

def dijkstra_shortest_path(graph, start, end):
    try:
        return nx.shortest_path_length(graph, source=start, target=end, weight='weight')
    except nx.NetworkXNoPath:
        return -1
    
def get_sum_shortest_paths(pairs, grid):
    sum = 0
    count = 0
    for pair in pairs:
        path = dijkstra_shortest_path(grid, pair[0], pair[1])
        sum += path
        count +=1
        print(count)
    return sum

G = create_graph(grid, empty_coordinates)
hashes = get_coords_for_hash(grid)
pairs = list(combinations(hashes,2))
result = get_sum_shortest_paths(pairs, G)
print(result)



