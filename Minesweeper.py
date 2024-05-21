import os
import random

rows, columns = 5, 6
grid = [[0] * columns for _ in range(rows)]
display_grid = [['-'] * columns for _ in range(rows)]

num_mines = 6
mine_positions = random.sample(range(rows * columns), num_mines)
for pos in mine_positions:
    row, col = divmod(pos, columns)
    grid[row][col] = 9

def count_adjacent_mines(x, y):
    return sum(1 for i in range(max(0, x - 1), min(rows, x + 2)) 
               for j in range(max(0, y - 1), min(columns, y + 2)) 
               if grid[i][j] == 9)

def reveal_cell(x, y):
    if grid[x][y] == 9:
        return 'M'
    adjacent_mines = count_adjacent_mines(x, y)
    grid[x][y] = adjacent_mines
    return adjacent_mines

def display_grid_to_user():
    os.system('cls')
    for row in display_grid:
        print(' '.join(map(str, row)))

while True:
    display_grid_to_user()
    row = int(input('Enter row (0-4): '))
    col = int(input('Enter column (0-5): '))
    cell = reveal_cell(row, col)
    display_grid[row][col] = cell

    if cell == 'M':
        display_grid_to_user()
        print('You found a mine! Game over!')
        break
    elif all(display_grid[i][j] != '-' for i in range(rows) for j in range(columns) if grid[i][j] != 9):
        display_grid_to_user()
        print('Congratulations! You have revealed all safe cells!')
        break

input('Press ENTER to reveal all mines...')

# Reveal all mines at the end
for row in range(rows):
    for col in range(columns):
        if grid[row][col] == 9:
            display_grid[row][col] = 'M'
display_grid_to_user()
