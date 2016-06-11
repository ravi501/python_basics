def print_grid(grid_array):
    inner_index = 0
    while inner_index < len(grid_array[0]):
        outer_index = 0
        while outer_index < len(grid_array):
            print(grid_array[outer_index][inner_index], end = "")
            outer_index += 1
        print()
        inner_index += 1

grid = [['.', '.', '.', '.', '.', '.'],
['.', '0', '0', '.', '.', '.'],
['0', '0', '0', '0', '.', '.'],
['0', '0', '0', '0', '0', '.'],
['.', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '0', '.'],
['0', '0', '0', '0', '.', '.'],
['.', '0', '0', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

print_grid(grid)