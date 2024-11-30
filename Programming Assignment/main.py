cages = [[[-1, -1] for _ in range(4)] for _ in range(9)]
clues = []
operations = []

grid_size = int(input("Enter size of the grid: "))
number_of_blocks = int(input("Enter number of blocks: "))

for i in range(number_of_blocks):
    cell_positions = []
    
    clue = input(f"Clue for block {i + 1}: ")
    if clue[0] in "+-":
        operations.append(clue[0])
        clues.append(int(clue[1:]))
    else:
        operations.append(clue[1])
        clues.append(int(clue[0]))
    
    cell_position = input(f"Cell positions for block {i + 1}")
    cell_position = list(map(int, cell_position.split()))
    
    for a in range(0, len(cell_position), 2):
        cell_positions.append([(cell_position[a])-1, (cell_position[a + 1]) -1]
                              )
    
    position_index = 0
    for j in range(4):
        if position_index < len(cell_positions):
            cages[i][j] = cell_positions[position_index]
            position_index += 1
        else:
            cages[i][j] = [-1, -1]

# Check if a number can be safely placed in the cell
def is_safe(grid, row, col, num):
    # Check row and column
    for i in range(N):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

# Check if a cage satisfies its constraint
def is_cage_satisfied(grid, cage_index):
    values = [0, 0, 0, 0]
    count = 0

    # Extract values from cage cells
    for x, y in cages[cage_index]:
        if x == -1 or y == -1:
            break  # No more cells in this cage
        if grid[x][y] == 0:
            return True  # Skip incomplete cages
        values[count] = grid[x][y]
        count += 1

    # Check operation
    op = operations[cage_index]
    clue = clues[cage_index]

    if op == '+':
        return sum(values[:count]) == clue
    elif op == '-':
        if count != 2:
            return False
        diff = abs(values[0] - values[1])
        return diff == clue
    return False

# Check if all cages are valid
def are_cages_valid(grid):
    for i in range(9):
        if not is_cage_satisfied(grid, i):
            return False
    return True

# Backtracking function
def solve_calcudoku(grid, row, col):
    if col == N:
        row += 1
        col = 0
    if row == N:
        return are_cages_valid(grid)

    if grid[row][col] != 0:
        return solve_calcudoku(grid, row, col + 1)

    for num in range(1, N + 1):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_calcudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0  # Backtrack
    return False  # No solution exists

# Main
def main():
    grid = [[0] * N for _ in range(N)]  # Initialize grid with zeros

    if solve_calcudoku(grid, 0, 0):
        print("Solution:")
        for row in grid:
            print(" ".join(map(str, row)))
    else:
        print("No Solution Exists")

if __name__ == "__main__":
    main()
