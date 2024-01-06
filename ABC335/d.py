def create_snake_grid(n):
    grid = [[0] * n for _ in range(n)]

    current_number = 1
    direction = 1
    i, j = 0, 0

    for _ in range(n*n):
        grid[i][j] = current_number
        current_number += 1

        if direction == 1:
            if j + 1 < n and grid[i][j + 1] == 0:
                j += 1
            else:
                direction = 2
                i += 1
        elif direction == 2:
            if i + 1 < n and grid[i + 1][j] == 0:
                i += 1
            else:
                direction = 3
                j -= 1
        elif direction == 3:
            if j - 1 >= 0 and grid[i][j - 1] == 0:
                j -= 1
            else:
                direction = 4
                i -= 1
        elif direction == 4:
            if i - 1 >= 0 and grid[i - 1][j] == 0:
                i -= 1
            else:
                direction = 1
                j += 1

    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

N = int(input())
snake_grid = create_snake_grid(N)
cen = ((N + 1) // 2) - 1

snake_grid[cen][cen] = "T"

print_grid(snake_grid)
