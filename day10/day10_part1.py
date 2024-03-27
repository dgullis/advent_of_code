with open("day10/day10_test_input.txt", "r") as f:
    rows = f.readlines()

rows = [row.strip() for row in rows]
# for row in rows:
#     print(row)

pipe_tiles = "|", "-", "L", "J", "7", "F", ".", "S"
up_down_tiles = "|", "L"

#relationships

# |, F(ifabove), L(ifbelow), J if below, 7 if above
# -, F(ifleft), 7(if right), J if right, L if left
# 7, -(ifleft), | if below, J if below, L if below
# J, | if above, & if above, F if above, - if left
# L, - if right, | if above, 




def get_next_tile_with_coords(puzzle, row, col, tile):
    if tile == "F":
        if puzzle[row][col+1] == "-":
            row = row
            col = col+1
            tile == "-"
    return row, col, tile




    

