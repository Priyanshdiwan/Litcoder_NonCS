def is_grid_sorted(input_str):
    parts = input_str.split(',')
    grid_size = list(map(int, parts[1].split()))
    rows, cols = grid_size
    characters = parts[2:]
    grid = [list(characters[i]) for i in range(rows)]
    for row in grid:
        row.sort()
    for col in range(cols):
        for row in range(rows - 1):
            if grid[row][col] > grid[row + 1][col]:
                return "NO"
    return "YES"
in_str = input()
output_1 = is_grid_sorted(in_str)
print(output_1)