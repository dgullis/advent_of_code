import networkx as nx
from itertools import combinations

with open("day11/day11_input.txt", "r") as f:
    rows = f.readlines()

rows = [row.strip() for row in rows]

new_rows = []
for row in rows:
    if '#' in row:
        new_rows.append(row)
    else:
        new_rows.extend([row] * 2)

columns = list(zip(*new_rows))

new_columns = []
for col in columns:
    if '#' in col:
        new_columns.append(col)
    else:
        new_columns.extend([col]*2)

grid = list(zip(*new_columns))

def get_coords_for_hash(grid):
    hashes = []
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                hashes.append((i,j))
    return hashes

def create_graph(grid):
    G = nx.Graph()
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            G.add_node((i,j))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols:
                    G.add_edge((i, j), (ni, nj))

    return G

def dijkstra_shortest_path(graph, start, end):
    try:
        return nx.shortest_path_length(graph, source=start, target=end)
    except nx.NetworkXNoPath:
        return -1
    
def get_sum_shortest_paths(pairs, grid):
    sum = 0
    for pair in pairs:
        path = dijkstra_shortest_path(grid, pair[0], pair[1])
        sum += path
    return sum

G = create_graph(grid)
hashes = get_coords_for_hash(grid)
pairs = list(combinations(hashes,2))
result = get_sum_shortest_paths(pairs, G)
print(result)


